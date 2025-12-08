# Change: Refactor Card Blocked Template to Generic Reusable System

## Why

We have 6 variants of the card blocked email template with the same layout but minor differences in text and background colors:

| Variant           | Segment  | Region        | Background Color |
| ----------------- | -------- | ------------- | ---------------- |
| B2B France        | Business | France        | Blue (#3651F3)   |
| B2C France        | Consumer | France        | Green (#2CCA97)  |
| B2B European      | Business | Europe        | Blue (#3651F3)   |
| B2C European      | Consumer | Europe        | Green (#2CCA97)  |
| B2B International | Business | International | Blue (#3651F3)   |
| B2C International | Consumer | International | Green (#2CCA97)  |

Creating a generic template system will reduce code duplication (avoid 6 separate HTML files), improve maintainability, and allow easy creation of new variants by configuring variables rather than duplicating HTML.

## What Changes

- Refactor `card-blocked.html` into a generic template with configurable variables
- Create configuration system for variant-specific values:
  - Background colors/gradients (header gradient)
  - Text content (addresses, legal text, region-specific wording)
  - Branding (if different per region)
- Support all 6 variants through configuration files
- **BREAKING**: Template structure changes from static HTML to template with variables
- Add template configuration files for each variant

## Impact

- Affected specs: `email-templates` capability (MODIFIED)
- Affected code:
  - `templates/card-blocked.html` → Refactored to generic template
  - New: `templates/config/card-blocked/` directory with 6 config files:
    - `b2b-france.json`
    - `b2c-france.json`
    - `b2b-european.json`
    - `b2c-european.json`
    - `b2b-international.json`
    - `b2c-international.json`
  - New: Template variable system for styling and content
- Design sources: Figma designs for each variant
