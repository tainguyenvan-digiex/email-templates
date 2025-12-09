# Change: Add Welcome Email Template

## Why

New users need a welcome email upon account activation to confirm their account is active and introduce them to key features of Green Nation banking services. This template follows the same design system and structure as the card-blocked template.

## What Changes

- Add new `welcome.html` template file
- Add configuration files for B2B and B2C variants (France, European, International)
- Reuse existing footer structure and header gradient styling from card-blocked template
- Add new welcome-specific content sections:
  - Hero welcome message with account activation confirmation
  - Features overview grid (SEPA/SWIFT, Multi-currency, Physical/virtual cards, Real-time tracking)
  - Impact/Partnership section (carbon offset with Veritree)
  - Personalized support section (Account Manager chat)
  - Need assistance section with CTAs (Book a call, FAQ access)

## Impact

- Affected specs: `email-templates`
- Affected code:
  - `templates/welcome.html` (new)
  - `templates/config/welcome/` (new directory with 2 config files: b2c.json, b2b.json)

## Design Reference

- Figma: https://www.figma.com/design/5jRNseCsJriU3OYJsJsFqX/Mail?node-id=123-191&m=dev
