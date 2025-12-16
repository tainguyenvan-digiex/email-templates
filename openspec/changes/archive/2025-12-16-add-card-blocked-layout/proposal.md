# Change: Add Card-Blocked Specific Postmark Layout

## Why

The current common layout only contains footer and unsubscribe sections. For card-blocked type emails (security alerts, notifications), there are additional shared components (logo row, heading pattern, greeting, social media promotion section) that should be centralized in a layout to reduce duplication and ensure consistency. Welcome emails have different structure and will continue using the existing layout.

## What Changes

- Add new Postmark layout file `layouts/card-blocked-layout.html` specifically for card-blocked type emails
- Add new content file `content/card-blocked-content-v2.html` that works with the new layout (only contains card-specific body content)
- The new layout includes:
  - Logo row (top-right logo placement)
  - Header background with gradient
  - Heading section with template variables
  - Greeting section (`{{greeting}} {{first_name}},`)
  - `{{{ @content }}}` placeholder for template-specific body content
  - Social Media Promotion section (title, social icons, hashtags)
  - Footer section (wave, logo, chatbox, social icons, copyright, legal)
  - Unsubscribe section
- **No modification to existing files** - all new files created alongside existing ones

## Impact

- Affected specs: `email-templates`
- Affected code:
  - New: `layouts/card-blocked-layout.html`
  - New: `content/card-blocked-content-v2.html`
  - Existing files remain unchanged: `layouts/common-layout.html`, `content/card-blocked-content.html`, `content/welcome-content.html`
