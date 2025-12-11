# Change: Extract Common Layout for Postmark

## Why

The welcome and card-blocked email templates share significant common components (footer, unsubscribe section, CSS styles, header structure). Currently, these components are duplicated across templates, making maintenance difficult. When footer content or styling needs to change, it must be updated in multiple places, increasing the risk of inconsistencies and errors.

Postmark supports Layouts that allow reusable components to be shared across templates. By extracting common components into a Postmark layout, we can:

- Reduce code duplication
- Ensure consistency across all email templates
- Simplify maintenance (update footer once, affects all templates)
- Enable easier upload to Postmark's template system

## What Changes

- **BREAKING**: Template structure changes to use Postmark layout system
- Create a Postmark layout file (`layouts/common-layout.html`) containing:
  - Common CSS styles from `<head>` section
  - Footer section (wave decoration, logo, chatbox, social icons, copyright, company registration, legal text)
  - Unsubscribe section (sent to email, unsubscribe link, company address)
  - `{{{ content }}}` placeholder for template-specific content
- Create content files (template-specific content only, no footer/unsubscribe/CSS):
  - `content/welcome-content.html` - Contains only welcome-specific content (header, features, impact, support, assistance sections)
  - `content/card-blocked-content.html` - Contains only card-blocked-specific content (header with card info, social media section)
- **Preserve existing template files**: `templates/welcome.html` and `templates/card-blocked.html` remain unchanged for backward compatibility
- Update documentation to explain how to use layouts with Postmark and how content files work with layouts

## Impact

- Affected specs: `email-templates` capability
- Affected code:
  - `templates/welcome.html` - **unchanged** (preserved for backward compatibility)
  - `templates/card-blocked.html` - **unchanged** (preserved for backward compatibility)
  - New file: `layouts/common-layout.html` (Postmark layout)
  - New file: `content/welcome-content.html` (content-only version for Postmark)
  - New file: `content/card-blocked-content.html` (content-only version for Postmark)
- Migration: Templates will need to be re-uploaded to Postmark with the layout association
- Benefits: Single source of truth for footer/unsubscribe, easier maintenance, Postmark-native structure
