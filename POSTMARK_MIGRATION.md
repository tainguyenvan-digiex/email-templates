# Postmark Email Template Migration Guide

This document provides instructions for the backend team on how to use the new Postmark email templates with the common layout system.

## Overview

Email templates have been restructured to use a **common layout** in Postmark, which centralizes shared components (footer, unsubscribe section, CSS) and reduces duplication.

## Layout

**Layout Name:** `green-nation-common-layout`

This layout contains:
- Common CSS styles (reset, responsive, utility classes)
- Footer section (wave decoration, logo, chatbox, social icons, copyright, company registration, legal text)
- Unsubscribe section (sent to email, unsubscribe link, company address)

## Template Mappings

### Old Template Names → New Template Names

| Old Template Name | New Template Name | Description |
|-------------------|-------------------|-------------|
| `gn-b2b-onboarding-completed-en` | `welcome-email` | Welcome email template (account activation) |
| `gn-b2b-card-blocked-en` | `card-block-email` | Card blocked notification email |

## Using the Templates

### 1. Template Structure

Each template is associated with the `green-nation-common-layout` layout. The template content is automatically inserted into the layout's `{{{ @content }}}` placeholder.

### 2. Sending Emails

When sending emails via Postmark API, use the new template names:

```json
{
  "TemplateAlias": "welcome-email",
  "TemplateModel": {
    // Template variables (see below)
  }
}
```

or

```json
{
  "TemplateAlias": "card-block-email",
  "TemplateModel": {
    // Template variables (see below)
  }
}
```

## Required Template Variables

### Common Variables (Required by Layout)

All templates require these variables for the layout:

#### Page Metadata
- `lang_code` - Language code (e.g., "en", "fr")
- `title` - Email subject line
- `preheader` - Hidden preview text

#### Footer Variables
- `chatbox_image_url` - URL to chatbox/automated email notice image
- `company_registration_part1` - First line of company registration
- `company_registration_part2` - Second line of company registration
- `company_registration_part3` - Third line of company registration
- `legal_text` - Legal disclaimer text

#### Unsubscribe Variables
- `sent_to_text` - Text before recipient email (e.g., "Sent to:")
- `recipient_email` - Recipient email address
- `footer_unsubscribe_link_text` - Unsubscribe link text
- `unsubscribe_url` - Unsubscribe URL (provided by server)
- `company_address` - Company address text
- `company_address_url` - URL-encoded company address for map link

### Welcome Email Variables

In addition to common variables, the welcome email requires:

#### Dynamic Variables (Provided by Server)
- `first_name` - User's first name
- `welcome_button_url` - URL for welcome button
- `book_call_url` - URL for booking a call
- `faq_url` - URL to FAQ page
- `unsubscribe_url` - Unsubscribe URL

#### Content Variables
- `header_gradient` - CSS gradient for header background
- `primary_color` - Primary brand color
- `feature_icon_background` - Background for feature icons
- `heading` - Main heading text
- `greeting` - Greeting text (e.g., "Hello")
- `account_active_message` - Account activation message
- `features_title` - Features section title
- `feature_1_title` through `feature_4_title` - Feature titles
- `feature_1_description` through `feature_4_description` - Feature descriptions
- `feature_1_icon_url` through `feature_4_icon_url` - Feature icon URLs
- `impact_title` - Impact section title
- `impact_description_part1` through `impact_description_part4` - Impact description parts
- `impact_description_bold1` through `impact_description_bold3` - Bold text within impact description
- `partnership_title` - Partnership section title
- `support_title` - Support section title
- `support_description_part1`, `support_description_part2` - Support description parts
- `support_description_bold` - Bold text within support description
- `assistance_title` - Assistance section title
- `book_call_label` - Book call label text
- `book_call_text` - Book call button text
- `faq_label` - FAQ label text
- `faq_text` - FAQ button text
- `signoff_part1`, `signoff_part2` - Sign-off text parts

### Card Blocked Email Variables

In addition to common variables, the card blocked email requires:

#### Dynamic Variables (Provided by Server)
- `first_name` - User's first name
- `card_last_four` - Last 4 digits of blocked card
- `unsubscribe_url` - Unsubscribe URL

#### Content Variables
- `header_gradient` - CSS gradient for header background
- `primary_color` - Primary brand color
- `heading_part1`, `heading_part2`, `heading_part3` - Heading parts
- `greeting` - Greeting text (e.g., "Hello", "Bonjour")
- `card_info_prefix` - Text before card number
- `card_info_suffix` - Text after card number
- `security_warning_part1`, `security_warning_part2` - Security warning parts
- `security_signature` - Security team signature
- `social_title` - Social media section title
- `social_hashtags_part1`, `social_hashtags_part2`, `social_hashtags_part3` - Hashtag parts

## Configuration Files Reference

Template variable values can be found in the configuration files:

- **Welcome Email (B2B):** `templates/config/welcome/b2b.json`
- **Welcome Email (B2C):** `templates/config/welcome/b2c.json`
- **Card Blocked (B2B France):** `templates/config/card-blocked/b2b-france.json`
- **Card Blocked (B2B European):** `templates/config/card-blocked/b2b-european.json`
- **Card Blocked (B2B International):** `templates/config/card-blocked/b2b-international.json`
- **Card Blocked (B2C France):** `templates/config/card-blocked/b2c-france.json`
- **Card Blocked (B2C European):** `templates/config/card-blocked/b2c-european.json`
- **Card Blocked (B2C International):** `templates/config/card-blocked/b2c-international.json`

## Important Notes

### Dynamic Fields (Bottom of Config Files)

The following fields are **always provided by the server** at runtime and should not be hardcoded:

**Welcome Email:**
- `first_name`
- `welcome_button_url`
- `book_call_url`
- `faq_url`
- `unsubscribe_url`
- All `*_icon_url` fields
- `chatbox_image_url`
- `company_address_url`

**Card Blocked Email:**
- `first_name`
- `card_last_four`
- `unsubscribe_url`
- `chatbox_image_url`
- `company_address_url`

### Image URLs

All image URLs are hosted on GitHub Raw Content CDN:
- Base URL: `https://raw.githubusercontent.com/tainguyenvan-digiex/email-templates/main/assets/`
- See `POSTMARK_MIGRATION.md` (this file) for complete list of image URLs

### Template Variables Order

When sending template variables, ensure:
1. All common layout variables are included
2. Template-specific variables are included
3. Dynamic variables (URLs, user data) are provided at runtime

## Migration Checklist

- [ ] Update Postmark API calls to use new template names
- [ ] Ensure all required template variables are being sent
- [ ] Verify dynamic variables are populated from server data
- [ ] Test email rendering in different email clients
- [ ] Verify unsubscribe links work correctly
- [ ] Confirm all image URLs are accessible

## Support

For questions or issues with the new template system, refer to:
- Layout file: `layouts/common-layout.html`
- Content files: `content/welcome-content.html`, `content/card-blocked-content.html`
- Configuration examples: `templates/config/`

