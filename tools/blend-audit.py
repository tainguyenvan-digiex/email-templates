"""
Audit the Oxen email templates for the two ways the Gmail dark-mode hack fails.

The hack is a pair of wrappers — `gmail-blend-screen` (black, mix-blend-mode: screen) around
`gmail-blend-difference` (black, mix-blend-mode: difference) — switched on in the Gmail app by the
layout's `u + .body …` rules. It composites a group against black, which is an identity only for
content that is LIGHT. Two failure modes follow:

  A  DARK text INSIDE the wrappers   -> Gmail app LIGHT mode inverts nothing, so the group (dark text
                                        on the wrapper's own black background) stays black and is
                                        then screened away against its light pill: invisible.
                                        This is the OTP bug reported 2026-09-28.
  B  LIGHT text OUTSIDE the wrappers -> Gmail DARK mode inverts it to dark on the pinned dark
                                        background: invisible. This is what the hack was added for.

Judged per TEXT NODE, not per element: these templates declare `color` on a `<td>` and put the blend
wrappers INSIDE it, so asking "is this coloured element wrapped" answers the wrong question. For each
piece of visible text we walk the ancestor chain for the nearest declared colour, the nearest declared
background, and whether a wrapper is open.
"""

import glob
import re
import sys
from html.parser import HTMLParser

LUMA_DARK = 90.0
LUMA_LIGHT = 150.0
VOID = {'br', 'img', 'input', 'meta', 'link', 'hr', 'source', 'area', 'base', 'col', 'embed'}
# Text that is punctuation or a separator carries no information either way.
IGNORE = {'·', '|', '—', '-', '•', '&nbsp;', ''}


def luma(hex_colour: str) -> float:
    h = hex_colour.lstrip('#')
    if len(h) == 3:
        h = ''.join(c * 2 for c in h)
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def prop(style: str, name: str):
    # `(?<![-\w])` or plain `color:` also matches `background-color:` — which silently read every
    # card's background as its text colour on the first run of this audit.
    m = re.search(r'(?<![-\w])' + name + r'\s*:\s*(#[0-9a-fA-F]{3,6})', style)
    return m.group(1) if m else None


class Audit(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.findings = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        style = a.get('style', '') or ''
        cls = a.get('class', '') or ''
        frame = {
            'tag': tag,
            'blend': 'gmail-blend-difference' in cls or 'gmail-blend-screen' in cls,
            'colour': prop(style, 'color'),
            # bgcolor attr, background-color, or the linear-gradient(#x, #x) anti-inversion trick
            'bg': a.get('bgcolor') or prop(style, 'background-color') or prop(style, 'background-image') or prop(style, 'background'),
            'line': self.getpos()[0],
        }
        if tag not in VOID:
            self.stack.append(frame)

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i]['tag'] == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        text = re.sub(r'\s+', ' ', data).strip()
        if text in IGNORE or not text:
            return
        blend = any(f['blend'] for f in self.stack)
        colour = next((f['colour'] for f in reversed(self.stack) if f['colour']), None)
        bg = next((f['bg'] for f in reversed(self.stack) if f['bg']), None)
        if colour is None:
            return
        l = luma(colour)
        line = self.stack[-1]['line'] if self.stack else 0
        # screen(backdrop, group) = backdrop + C - backdrop*C: on a LIGHT pill a dark C lands back on
        # the pill's own value and disappears; over the dark body the same C still reads.
        if blend and l < LUMA_DARK:
            if bg and luma(bg) > LUMA_LIGHT:
                self.findings.append(('A', line, colour, bg, text[:44]))
            elif not text.startswith('{{#') and not text.startswith('{{/'):
                self.findings.append(('a', line, colour, bg, text[:44]))
        elif not blend and l > LUMA_LIGHT and (bg is None or luma(bg) < LUMA_DARK):
            self.findings.append(('B', line, colour, bg, text[:44]))


def run(paths):
    total = {'A': 0, 'a': 0, 'B': 0}
    for p in sorted(paths):
        a = Audit()
        a.feed(open(p).read())
        a.close()
        if a.findings:
            print(f'\n=== {p.split("/")[-1]}')
            for kind, line, colour, bg, text in a.findings:
                total[kind] += 1
                where = {'A': 'Gmail LIGHT mode', 'a': 'low contrast (dark on dark)', 'B': 'Gmail DARK mode'}[kind]
                print(f'  [{kind}] L{line:<4} {colour} on {bg or "(inherited)":<9} invisible in {where}  "{text}"')
    print(f'\nTOTAL  A (dark text on a LIGHT pill inside blend — breaks): {total["A"]}'
          f'   a (dark on dark, review): {total["a"]}   B (light text outside blend): {total["B"]}')


if __name__ == '__main__':
    run(sys.argv[1:] or glob.glob('templates/content/*.html'))
