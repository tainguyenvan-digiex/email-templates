# Add sign_off and signature defaults to oxen-layout Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Render `sign_off` and `signature` as HTML once in `oxen-layout.html` so all templates get them automatically. Remove the rendering from all individual content HTML files. Variable _values_ stay in each template's config (they are dynamic per email); the layout just renders them.

**Architecture:**

- `layouts/oxen-layout.html` gains a sign-off HTML block between `{{{ @content }}}` and the footer divider.
- `oxen-layout/en.json` and `oxen-layout/fr.json` provide default values (already done).
- All 48 individual content HTML files lose their sign_off/signature table row blocks.
- Config JSONs with alias keys (`sign_off_prefix`, `security_signature`) are renamed to `sign_off` / `signature` so they resolve correctly from the layout variable.

**Tech Stack:** HTML (email-safe table layout), JSON config files, Handlebars-style `{{variable}}` templating via Postmark.

---

## File Map

| Action                | File                                                                             |
| --------------------- | -------------------------------------------------------------------------------- |
| ✅ Done               | `templates/config/oxen-layout/en.json` — `sign_off` + `signature` defaults added |
| ✅ Done               | `templates/config/oxen-layout/fr.json` — `sign_off` + `signature` defaults added |
| Modify                | `layouts/oxen-layout.html` — add sign-off HTML block                             |
| Modify (remove block) | All 48 content HTML files listed in Task 2                                       |
| Modify (rename key)   | 9 config JSONs: `sign_off_prefix` → `sign_off`                                   |
| Modify (rename key)   | 4 config JSONs: `security_signature` → `signature`                               |

---

### Task 1: Add sign-off HTML block to oxen-layout.html

The layout injects each template's body at `{{{ @content }}}` (line 186). The sign-off block must go immediately after that injection, before the `<!-- ========== FOOTER ========== -->` comment.

**File:** `layouts/oxen-layout.html`

- [ ] **Step 1: Insert the sign-off block after `{{{ @content }}}`**

Find this exact section in `layouts/oxen-layout.html`:

```html
<!-- ========== BODY CONTENT (injected by each template) ========== -->
{{{ @content }}}

<!-- ========== FOOTER ========== -->
```

Replace with:

```html
<!-- ========== BODY CONTENT (injected by each template) ========== -->
{{{ @content }}}

<!-- ========== SIGN-OFF ========== -->
<tr>
  <td style="padding: 0 40px 20px 40px" class="mobile-padding">
    <table
      role="presentation"
      cellspacing="0"
      cellpadding="0"
      border="0"
      width="100%"
    >
      <tr>
        <td align="center">
          <p
            style="
                          margin: 0 0 4px 0;
                          font-family: 'DM Sans', Arial, sans-serif;
                          font-size: 18px;
                          font-weight: 500;
                          line-height: 22px;
                          color: #F5F0EB;
                          text-align: center;
                        "
            class="body-text"
          >
            {{sign_off}}
          </p>
          <p
            style="
                          margin: 0;
                          font-family: 'DM Sans', Arial, sans-serif;
                          font-size: 18px;
                          font-weight: 500;
                          line-height: 22px;
                          color: #F5F0EB;
                          text-align: center;
                        "
            class="body-text"
          >
            {{signature}}
          </p>
        </td>
      </tr>
    </table>
  </td>
</tr>

<!-- ========== FOOTER ========== -->
```

- [ ] **Step 2: Verify the block was inserted correctly**

Run: `grep -n "sign_off\|signature\|SIGN-OFF\|@content\|FOOTER" layouts/oxen-layout.html`

Expected: `{{{ @content }}}` appears before `SIGN-OFF`, which appears before `FOOTER`.

---

### Task 2: Remove sign-off/signature blocks from all content HTML files

Each of the 48 content files below has one or more sections rendering `{{sign_off}}`, `{{signature}}`, `{{sign_off_prefix}}`, or `{{security_signature}}`. Each section consists of an optional HTML comment (`<!-- Signature -->`, `<!-- Sign-off -->`, etc.) followed by an outer `<tr>` that wraps a `<td>` → `<table>` → inner `<tr>` structure. The entire outer block — comment through closing outer `</tr>` — must be removed.

Run this Python script from the repo root. It uses a line-by-line depth counter to correctly identify and remove the full outer `<tr>` block (not just the inner one):

- [ ] **Step 1: Run the removal script**

```bash
python3 - << 'PYEOF'
import glob, re

SIGNOFF_VARS = re.compile(r'{{(?:sign_off|signature|sign_off_prefix|security_signature)}}', re.IGNORECASE)
COMMENT_SIGNOFF = re.compile(r'<!--[^>]*(Sign-?off|Signature)[^>]*-->', re.IGNORECASE)
OPEN_TR = re.compile(r'^\s*<tr[\s>]')
CLOSE_TR = re.compile(r'^\s*</tr>')

def remove_signoff_blocks(lines):
    result = []
    i = 0
    while i < len(lines):
        # Check for optional leading comment
        comment_line = None
        j = i
        if COMMENT_SIGNOFF.search(lines[j]):
            comment_line = j
            j += 1
            # Skip blank lines between comment and <tr>
            while j < len(lines) and lines[j].strip() == '':
                j += 1

        # Expect an outer <tr> at position j
        if j < len(lines) and OPEN_TR.match(lines[j]):
            # Collect the full outer <tr>...</tr> block
            depth = 0
            block_lines = []
            k = j
            while k < len(lines):
                line = lines[k]
                block_lines.append(line)
                depth += len(re.findall(r'<tr[\s>]', line))
                depth -= len(re.findall(r'</tr>', line))
                k += 1
                if depth == 0:
                    break
            # Check if this block contains a sign-off variable
            block_text = ''.join(block_lines)
            if SIGNOFF_VARS.search(block_text):
                # Drop comment + blank lines + entire block
                i = k  # skip past the block
                continue
            else:
                # Not a sign-off block — keep comment (if any) and move on
                if comment_line is not None:
                    result.append(lines[comment_line])
                result.append(lines[j])
                i = j + 1
                continue

        # No matching <tr> after comment — keep comment as-is
        if comment_line is not None:
            result.append(lines[i])
        else:
            result.append(lines[i])
        i += 1
    return result

files = glob.glob('templates/content/*-content.html')
for path in sorted(files):
    with open(path) as f:
        lines = f.readlines()
    cleaned = remove_signoff_blocks(lines)
    if cleaned != lines:
        with open(path, 'w') as f:
            f.writelines(cleaned)
        print(f'Updated: {path}')
    else:
        print(f'No change: {path}')
PYEOF
```

- [ ] **Step 2: Verify no sign-off variables remain in any content file**

Run: `grep -rn "{{sign_off}}\|{{signature}}\|{{sign_off_prefix}}\|{{security_signature}}" templates/content/`

Expected: no output (zero matches).

- [ ] **Step 3: Spot-check two files to confirm structure is intact**

Run: `tail -20 templates/content/compliance-request-approved-content.html`
Run: `tail -20 templates/content/account-closed-content.html`

Expected: files end with `</tr>` (closing the last content row), not a sign-off block. No dangling `<td>` or `<table>` tags.

---

### Task 3: Rename alias keys in config JSONs

Config JSONs that used `sign_off_prefix` or `security_signature` must be renamed to `sign_off` / `signature` so the layout's `{{sign_off}}` and `{{signature}}` placeholders resolve the correct per-template values.

**Affected configs:**

`sign_off_prefix` → `sign_off` (9 template pairs):

- `templates/config/invite-kyc/`
- `templates/config/subscription-invoice/`
- `templates/config/monthly-statement-ready/`
- `templates/config/expense-report/`
- `templates/config/subscription-collection-remind-24-hours/`
- `templates/config/subscription-account-suspend/`
- `templates/config/subscription-collection-remind-3-days/`
- `templates/config/automatic-account-closure-final-remind/`
- `templates/config/kyb-process-started/`

`security_signature` → `signature` (2 template pairs):

- `templates/config/card-blocked/`
- `templates/config/card-unblocked/`

- [ ] **Step 1: Rename `sign_off_prefix` → `sign_off` in 9 config pairs**

```bash
for dir in \
  templates/config/invite-kyc \
  templates/config/subscription-invoice \
  templates/config/monthly-statement-ready \
  templates/config/expense-report \
  templates/config/subscription-collection-remind-24-hours \
  templates/config/subscription-account-suspend \
  templates/config/subscription-collection-remind-3-days \
  templates/config/automatic-account-closure-final-remind \
  templates/config/kyb-process-started; do
  for f in "$dir/en.json" "$dir/fr.json"; do
    python3 -c "
import json, collections
with open('$f') as fh:
    data = json.load(fh, object_pairs_hook=collections.OrderedDict)
if 'sign_off_prefix' in data:
    data['sign_off'] = data.pop('sign_off_prefix')
with open('$f', 'w') as fh:
    json.dump(data, fh, indent=4, ensure_ascii=False)
    fh.write('\n')
print('Updated $f')
"
  done
done
```

- [ ] **Step 2: Rename `security_signature` → `signature` in 2 config pairs**

```bash
for dir in templates/config/card-blocked templates/config/card-unblocked; do
  for f in "$dir/en.json" "$dir/fr.json"; do
    python3 -c "
import json, collections
with open('$f') as fh:
    data = json.load(fh, object_pairs_hook=collections.OrderedDict)
if 'security_signature' in data:
    data['signature'] = data.pop('security_signature')
with open('$f', 'w') as fh:
    json.dump(data, fh, indent=4, ensure_ascii=False)
    fh.write('\n')
print('Updated $f')
"
  done
done
```

- [ ] **Step 3: Verify no alias keys remain in any config JSON**

Run: `grep -rn "sign_off_prefix\|security_signature" templates/config/ --include="*.json"`

Expected: no output.

---

### Task 4: Final verification

- [ ] **Step 1: Confirm oxen-layout.html renders sign_off and signature**

Run: `grep -n "sign_off\|signature" layouts/oxen-layout.html`

Expected: 2 matches inside the new `<!-- SIGN-OFF -->` block.

- [ ] **Step 2: Confirm no content file renders sign_off or signature**

Run: `grep -rn "sign_off\|signature" templates/content/`

Expected: no output.

- [ ] **Step 3: Confirm all config JSONs are valid JSON**

Run: `find templates/config/ -name "*.json" | xargs -I{} python3 -c "import json; json.load(open('{}'))" && echo "All JSON valid"`

Expected: `All JSON valid`
