# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A static collection of Postmark email templates (transactional/notification emails for Oxen/Green Nation). There is no build system, package manager, or test runner — everything is plain HTML and JSON, uploaded to Postmark by hand or via the Postmark UI/API. There are no lint/build/test commands to run; verification is visual (render the merged layout+content+config HTML and check it).

## Architecture: layout + content + config

Each template is assembled from three pieces that live in three different directories, keyed by the same template slug:

1. **`layouts/*.html`** — Postmark *Layout* files. Contain the shared HTML shell: `<head>`/CSS, header, footer, unsubscribe block, and a content placeholder (`{{{ content }}}` or `{{{ @content }}}`) where the template body is injected. Current canonical layout is `layouts/oxen-layout.html`; `shared-layout.html` and `common-layout.html` (plus `.lapkipay` variants) are older/alternate layouts still referenced by some older templates. Per `docs/POSTMARK_LAYOUT_MIGRATION.md`, templates are being migrated to `oxen-layout`.
2. **`templates/content/<slug>-content.html`** — Postmark *Template* body for one email, uploaded to Postmark and associated with a layout. Contains ONLY the template-specific body (no `<html>`/`<head>`, no footer, no unsubscribe, no CSS — those come from the layout).
3. **`templates/config/<slug>/{en,fr}.json`** — per-template, per-language variable values used to fill in `{{variable}}` placeholders in both the content file and the layout. The `"layout"` key inside each config names which layout file this template renders with (almost all templates now use `"oxen-layout"`).
4. **`templates/config/oxen-layout/{en,fr}.json`** (and similarly `common-layout/`) — base config for the layout itself (footer text, legal text, URLs, sign-off/signature). These values are shared across all templates using that layout and are conceptually merged with the per-template config when composing a send.

So to fully render one email you combine: layout HTML (from `layouts/`) + content HTML (from `templates/content/`) + language config for the layout (`templates/config/<layout-name>/<lang>.json`) + language config for the template (`templates/config/<slug>/<lang>.json`).

`oxen-emails/*.html` is a separate, older set of fully self-contained, single-file HTML emails (no layout/content split, no config files) — treat these as standalone/legacy references, not part of the layout+content+config system.

## Variables & language files

- Placeholders use `{{variable_name}}` (Postmark/Mustache-style); the layout's content injection point uses triple braces (`{{{ content }}}`).
- Every template has parallel `en.json`/`fr.json` config files with identical key structure — when adding a template or a field, update both languages.
- **`templates/config/` must match the PHP service's config exactly — they are one and the same.** The PHP
  service (the backend that sends these emails) keeps its own copy of every `templates/config/<slug>/{en,fr}.json`
  (and the layout configs). Any change here — a new template, a new/renamed/removed key, a changed value — must
  be applied identically to the PHP service's config in the same change, and vice versa. Never edit one side
  without the other; a mismatch means Postmark gets a placeholder with no value (or a value nobody sees).
- **be-b2b is the source of truth.** The PHP service is `greennation-be-b2b`
  (`../php/greennation-be-b2b/config/email-template-params/oxen/<slug>/{en,fr}.json`). Its configs and
  templates are the latest; this repo follows them, not the other way round. Before changing a template or
  config here, read the be-b2b version first, and when the two disagree, take be-b2b's keys/values.
- **Write Postmark syntax only.** Everything in this repo is uploaded to Postmark, so it must use Postmark's
  Mustachio syntax: `{{var}}`, `{{{ @content }}}`, `{{#section}}…{{/section}}`, `{{^section}}…{{/section}}`,
  `{{#each list}}…{{/each}}`. be-b2b's own `templates/emails/*.html.twig` are Twig — when porting from them,
  translate the logic into Postmark syntax; never copy Twig (`{% … %}`, `{{ var|filter }}`) in here.
- Some fields are filled by the backend at send time (e.g. `first_name`, `cta_url`, OTP codes) rather than being static in the config — see `TEMPLATES_TABLE.md` for the authoritative per-template list of server-provided dynamic fields, their Postmark alias, and CSV/DB mapping, and `docs/POSTMARK_LAYOUT_MIGRATION.md` for the fields the backend must inject per template during the `oxen-layout` migration.

## Adding or changing a template

1. Add/edit `templates/content/<slug>-content.html` with only the body markup, referencing `{{variable}}` placeholders.
2. Add/edit `templates/config/<slug>/en.json` and `fr.json` with matching keys (include `"layout"`, `"title"`, `"subject"`, and any content variables).
   Mirror the exact same change into the PHP service's config (see "Variables & language files") — the two must stay identical.
3. If new variables are introduced, document them in `TEMPLATES_TABLE.md` (dynamic fields table) so backend integrators know what to supply.
4. Run `python3 tools/blend-audit.py $(ls templates/content/*.html | grep -v lapkipay)` and require
   **A = 0 and B = 0**. Verification here is visual, and this particular defect is invisible on a
   desktop: it only shows in the Gmail app, and only in one of its two modes.

### The Gmail blend wrappers — the rule that keeps being broken

`oxen-layout` renders text inside `gmail-blend-screen` / `gmail-blend-difference` against black so
Gmail's **dark** mode cannot invert it. That is an identity only for **light** text.

- **Light text on the dark ground → WRAP it.** Unwrapped, Gmail dark mode turns it dark: invisible.
- **Dark text on a light pill (buttons, the OTP box) → do NOT wrap it.** Wrapped, the Gmail app's
  **light** mode (which inverts nothing) leaves the group black and screens it back into the pill:
  invisible. Unwrapped, Gmail inverts pill and label together, so either mode keeps its contrast.

Both mistakes have shipped more than once — the OTP box came back empty on Gmail iOS on 2026-09-28 —
which is what `tools/blend-audit.py` exists to catch. It reads the templates as a tree and judges each
text node by its inherited colour, its nearest background, and whether a wrapper is open.
