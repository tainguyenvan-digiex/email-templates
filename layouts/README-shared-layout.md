# Shared Layout

A shared Postmark layout for emails that require a header with gradient background, social media promotion section, and standard footer structure.

## Purpose

This layout centralizes common components for multiple email types:

- Logo row (Green Nation logo, top-right placement)
- Header section with gradient background
- Heading section (multipart with emoji)
- Greeting section
- Social Media Promotion section
- Footer section (wave, logo, chatbox, social icons, copyright, legal)
- Unsubscribe section

## When to Use

Use `shared-layout.html` for:

- Card blocked notifications
- Transfer failed notifications
- Security warnings
- Account-related notifications
- Any email type that needs header gradient and social media promotion

Use `common-layout.html` for:

- Welcome emails
- Other email types with different structures (simpler layout without header gradient)

## Required Template Variables

### Layout Variables (provided by layout, required in config)

| Variable                       | Description                        | Example                                                                   |
| ------------------------------ | ---------------------------------- | ------------------------------------------------------------------------- |
| `lang_code`                    | Language code                      | `en`, `fr`                                                                |
| `title`                        | Email title for browser tab        | `Your card has been blocked - Green Nation`                               |
| `preheader`                    | Preview text in email clients      | `⚠️ Your Green Nation card has been blocked...`                           |
| `primary_color`                | Fallback header background color   | `#3651F3`                                                                 |
| `header_gradient`              | Header gradient background         | `linear-gradient(181deg, #3651F3 -4.19%, rgba(255, 255, 255, 0) 65.81%)`  |
| `heading`                      | Heading text (plain text)                   | `YOUR CARD HAS BEEN BLOCKED, PLEASE CHECK YOUR ACCOUNT 🔔` |
| `greeting`                     | Greeting word                      | `Hello`                                                                   |
| `first_name`                   | Recipient's first name             | `John`                                                                    |
| `social_title`                 | Social media section title         | `Don't miss out on our latest updates!`                                   |
| `social_hashtags_part1`        | First line of hashtags             | `#CLEANTECH #MONEY #PLANET...`                                            |
| `social_hashtags_part2`        | Second part of hashtags            | `AND ABOVE ALL...`                                                        |
| `social_hashtags_part3`        | Third part of hashtags             | `EXCLUSIVE UPDATES!`                                                      |
| `company_registration_part1`   | Company registration text (part 1) | Registration details                                                      |
| `company_registration_part2`   | Company registration text (part 2) | Additional details                                                        |
| `company_registration_part3`   | Company registration text (part 3) | Additional details                                                        |
| `legal_text`                   | Legal disclaimer text              | Visa card issuer info                                                     |
| `footer_unsubscribe_link_text` | Unsubscribe link text              | `To unsubscribe, click here.`                                             |
| `unsubscribe_url`              | Unsubscribe URL                    | Unsubscribe link                                                          |

### Static Values (Hardcoded in Layout)

The following values are hardcoded in the layout file and do not need to be provided in JSON config:

- `sent_to_text`: `Sent to:` (hardcoded)
- `recipient_email`: `c.garreau@greennation.green` (hardcoded)
- `company_address`: `205 – 50 Lonsdale Ave #2630, Vancouver, BC V6M 2E6, Canada.` (hardcoded)
- `company_address_url`: `205+–+50+Lonsdale+Ave+%232630,+Vancouver,+BC+V6M+2E6,+Canada.` (hardcoded)

### Content Variables (used in content files)

Content variables depend on the specific content file being used:

**For `card-blocked-content-v2.html`:**
- `card_info_prefix` - Text before card number
- `card_last_four` - Last 4 digits of card
- `card_info_suffix` - Text after card number
- `security_warning` - Security warning text
- `security_signature` - Signature

**For `transfer-failed-content.html`:**
- `transaction_failed_intro` - Introduction text
- `amount_label` - Amount label text
- `amount` - Transaction amount
- `transaction_type_label` - Transaction type label
- `transaction_type` - Transaction type
- `failure_reason_label` - Failure reason label
- `failure_reason` - Failure reason
- `action_message` - Action message
- `signature` - Signature

## How to Upload to Postmark

1. **Upload the Layout**:

   - Go to Postmark → Server → Templates → Layouts
   - Create a new layout named `shared-layout`
   - Paste the contents of `layouts/shared-layout.html`
   - Save

2. **Create Template with Content**:

   - Go to Postmark → Server → Templates
   - Create a new template
   - Select `shared-layout` as the layout
   - Paste the contents of your content file (e.g., `content/card-blocked-content-v2.html` or `content/transfer-failed-content.html`) in the content section
   - Configure the template alias (e.g., `card-block-email` or `transfer-failed-email`)
   - Save

3. **Test**:
   - Use Postmark's preview feature with test data from config files
   - Send test emails to verify rendering

## File Structure

```
layouts/
├── common-layout.html           # General layout (for welcome emails, etc.)
├── shared-layout.html           # Shared layout with header gradient and social media (this file)
└── README-shared-layout.md      # This documentation

content/
├── card-blocked-content.html    # Original content (works with common-layout)
├── card-blocked-content-v2.html # Card blocked content (works with shared-layout)
├── transfer-failed-content.html # Transfer failed content (works with shared-layout)
└── welcome-content.html         # Welcome email content

templates/config/
├── card-blocked/                # Config files for card-blocked templates
└── transfer-failed/             # Config files for transfer-failed templates
```

## Migration Notes

- Existing templates using `common-layout.html` + `card-blocked-content.html` continue to work
- New templates can use `shared-layout.html` + appropriate content file
- The shared layout reduces duplication for similar notification emails
- Multiple email types (card-blocked, transfer-failed) can use the same layout
