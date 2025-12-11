## 1. Create Postmark Layout Structure

- [x] 1.1 Create `layouts/` directory for Postmark layout files
- [x] 1.2 Create `layouts/common-layout.html` with Postmark layout structure
- [x] 1.3 Extract common CSS styles from templates into layout `<head>` section
- [x] 1.4 Extract footer section (wave decoration, logo, chatbox, social icons, copyright, company registration, legal text) into layout
- [x] 1.5 Extract unsubscribe section (sent to email, unsubscribe link, company address) into layout
- [x] 1.6 Add `{{{ @content }}}` placeholder in layout where template-specific content will be inserted
- [x] 1.7 Ensure layout maintains email client compatibility (table-based structure, inline styles)

## 2. Create Welcome Content File

- [x] 2.1 Create `content/` directory for content-only files
- [x] 2.2 Create `content/welcome-content.html` with only template-specific content
- [x] 2.3 Extract welcome-specific sections from `templates/welcome.html`:
  - Header section (logo, heading, greeting, account active message, welcome button, iPhone background)
  - Features section (features title, 4 feature items)
  - Impact title section
  - Personalized support section
  - Partnership section
  - Need assistance section
- [x] 2.4 Exclude footer, unsubscribe, and CSS from content file
- [x] 2.5 Wrap content appropriately for insertion into layout's `{{{ @content }}}` placeholder
- [x] 2.6 Verify all template variables still work correctly
- [x] 2.7 Ensure `templates/welcome.html` remains unchanged

## 3. Create Card Blocked Content File

- [x] 3.1 Create `content/card-blocked-content.html` with only template-specific content
- [x] 3.2 Extract card-blocked-specific sections from `templates/card-blocked.html`:
  - Header section (logo, heading, greeting, card information, security message)
  - Social media promotion section (title, icons, hashtags)
- [x] 3.3 Exclude footer, unsubscribe, and CSS from content file
- [x] 3.4 Wrap content appropriately for insertion into layout's `{{{ @content }}}` placeholder
- [x] 3.5 Verify all template variables still work correctly
- [x] 3.6 Ensure `templates/card-blocked.html` remains unchanged

## 4. Documentation and Validation

- [x] 4.1 Document how to upload layout to Postmark
- [x] 4.2 Document how to associate templates with layout in Postmark
- [x] 4.3 Document template variable requirements for layout
- [ ] 4.4 Validate HTML structure and email client compatibility
- [ ] 4.5 Test visual rendering in email clients (Gmail, Outlook, Apple Mail)
- [ ] 4.6 Verify all template variables are properly passed to layout
