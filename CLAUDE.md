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
- Some fields are filled by the backend at send time (e.g. `first_name`, `cta_url`, OTP codes) rather than being static in the config — see `TEMPLATES_TABLE.md` for the authoritative per-template list of server-provided dynamic fields, their Postmark alias, and CSV/DB mapping, and `docs/POSTMARK_LAYOUT_MIGRATION.md` for the fields the backend must inject per template during the `oxen-layout` migration.

## Adding or changing a template

1. Add/edit `templates/content/<slug>-content.html` with only the body markup, referencing `{{variable}}` placeholders.
2. Add/edit `templates/config/<slug>/en.json` and `fr.json` with matching keys (include `"layout"`, `"title"`, `"subject"`, and any content variables).
3. If new variables are introduced, document them in `TEMPLATES_TABLE.md` (dynamic fields table) so backend integrators know what to supply.
