# Postmark Layout Usage Guide

This directory contains the common layout file for Postmark email templates.

## Overview

The `common-layout.html` file is a Postmark layout that contains:

- Common CSS styles (reset, responsive, utility classes)
- Footer section (wave decoration, logo, chatbox, social icons, copyright, company registration, legal text)
- Unsubscribe section (sent to email, unsubscribe link, company address)

Template-specific content is inserted into the `{{{ @content }}}` placeholder.

## Template Variables Required by Layout

The layout requires the following template variables to be provided:

### Page Metadata

- `{{lang_code}}` - Language code (e.g., "en", "fr")
- `{{title}}` - Email title
- `{{preheader}}` - Hidden preview text

### Footer Variables

- Chatbox image URL is automatically generated from `lang_code`: `https://referral-dev.greennation.green/b2b/emails/assets/chatbox_{{lang_code}}.png`
- `{{company_registration_part1}}` - First line of company registration
- `{{company_registration_part2}}` - Second line of company registration
- `{{company_registration_part3}}` - Third line of company registration
- `{{legal_text}}` - Legal disclaimer text

### Unsubscribe Variables

- `{{sent_to_text}}` - Text before recipient email (e.g., "Sent to:")
- `{{recipient_email}}` - Recipient email address
- `{{footer_unsubscribe_link_text}}` - Unsubscribe link text
- `{{unsubscribe_url}}` - Unsubscribe URL
- `{{company_address}}` - Company address text
- `{{company_address_url}}` - URL-encoded company address for map link

## Uploading to Postmark

1. **Upload Layout**:

   - Go to your Postmark server
   - Navigate to Templates → Layouts
   - Click "Add layout"
   - Copy and paste the contents of `common-layout.html`
   - Save the layout (name it "Common Layout" or similar)

2. **Upload Content Files as Templates**:

   - Go to Templates → Templates
   - Create a new template (or edit existing)
   - Select the layout you just created from the Layout dropdown
   - Copy and paste the contents of `content/welcome-content.html` or `content/card-blocked-content.html`
   - Save the template

3. **Associate Template with Layout**:
   - When creating/editing a template, select the layout from the Layout dropdown
   - Postmark will automatically insert the template content into the layout's `{{{ @content }}}` placeholder

## Content Files

Content files in the `../content/` directory contain only template-specific sections:

- **welcome-content.html**: Header, features, impact, support, assistance sections
- **card-blocked-content.html**: Header with card info, social media section

These files do NOT include:

- Footer section
- Unsubscribe section
- CSS styles
- HTML document structure

## Notes

- The layout uses `{{{ @content }}}` (triple braces with @ symbol) to prevent HTML escaping and reference Postmark's content placeholder
- All template variables from content files are preserved and work with the layout
- Original template files (`templates/welcome.html`, `templates/card-blocked.html`) remain unchanged for backward compatibility
- When updating footer or unsubscribe sections, update only the layout file
