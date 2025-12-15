## 1. Create Card-Blocked Layout

- [x] 1.1 Create `layouts/card-blocked-layout.html` with:
  - [x] HTML document structure (DOCTYPE, html, head, body)
  - [x] CSS styles (reset, responsive, utility classes)
  - [x] Logo row section (Green Nation logo, top-right placement)
  - [x] Header section with gradient background (`{{header_gradient}}`, `{{primary_color}}`)
  - [x] Heading section with template variables (`{{heading_part1}}`, `{{heading_part2}}`, `{{heading_part3}}`)
  - [x] Greeting section (`{{greeting}} {{first_name}},`)
  - [x] Content placeholder `{{{ @content }}}`
  - [x] Social Media Promotion section (title, icons, hashtags)
  - [x] Footer section (wave, logo, chatbox, social icons, copyright, legal)
  - [x] Unsubscribe section

## 2. Create New Content File

- [x] 2.1 Create `content/card-blocked-content-v2.html` containing only:
  - [x] Card Information section (card_info_prefix, card_last_four, card_info_suffix)
  - [x] Security Message section (security_warning_part1, security_warning_part2, security_signature)

## 3. Documentation

- [x] 3.1 Create `layouts/README-card-blocked-layout.md` documenting:
  - [x] Layout purpose and usage
  - [x] Required template variables
  - [x] How to upload to Postmark
  - [x] Which email types should use this layout

## 4. Update Configuration Documentation

- [x] 4.1 Update `POSTMARK_MIGRATION.md` noting:
  - [x] Two layout options available
  - [x] When to use card-blocked-layout vs common-layout
