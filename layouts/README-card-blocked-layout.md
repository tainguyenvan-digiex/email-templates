# Card Blocked Layout

A specialized Postmark layout for card-blocked type emails (security notifications, alerts).

## Purpose

This layout centralizes common components for card-blocked type emails:

- Logo row (Green Nation logo, top-right placement)
- Header section with gradient background
- Heading section (multipart with emoji)
- Greeting section
- Social Media Promotion section
- Footer section (wave, logo, chatbox, social icons, copyright, legal)
- Unsubscribe section

## When to Use

Use `card-blocked-layout.html` for:

- Card blocked notifications
- Suspicious login alerts
- Security warnings
- Account-related security notifications

Use `common-layout.html` for:

- Welcome emails
- Other email types with different structures

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
| `sent_to_text`                 | "Sent to" label                    | `Sent to:`                                                                |
| `recipient_email`              | Recipient's email address          | `user@example.com`                                                        |
| `footer_unsubscribe_link_text` | Unsubscribe link text              | `To unsubscribe, click here.`                                             |
| `unsubscribe_url`              | Unsubscribe URL                    | Unsubscribe link                                                          |
| `company_address`              | Company address                    | `48 Rue de la Bienfaisance, 75008 Paris, France`                          |
| `company_address_url`          | URL-encoded address for maps       | `48+Rue+de+la+Bienfaisance,+75008+Paris,+France`                          |

### Content Variables (used in content file)

For `card-blocked-content-v2.html`:

| Variable             | Description                    | Example                                      |
| -------------------- | ------------------------------ | -------------------------------------------- |
| `card_info_prefix`   | Text before card number        | `The card ending in`                         |
| `card_last_four`     | Last 4 digits of card          | `1234`                                       |
| `card_info_suffix`   | Text after card number         | `has been blocked via the Green Nation app.` |
| `security_warning`   | Security warning text (plain text) | `👉 If you didn't initiate this action, please contact our support immediately.` |
| `security_signature` | Signature                      | `The Security Team.`                         |

## How to Upload to Postmark

1. **Upload the Layout**:

   - Go to Postmark → Server → Templates → Layouts
   - Create a new layout named `card-blocked-layout`
   - Paste the contents of `layouts/card-blocked-layout.html`
   - Save

2. **Create Template with Content**:

   - Go to Postmark → Server → Templates
   - Create a new template
   - Select `card-blocked-layout` as the layout
   - Paste the contents of `content/card-blocked-content-v2.html` in the content section
   - Configure the template alias (e.g., `card-block-email`)
   - Save

3. **Test**:
   - Use Postmark's preview feature with test data from config files
   - Send test emails to verify rendering

## File Structure

```
layouts/
├── common-layout.html           # General layout (for welcome emails, etc.)
├── card-blocked-layout.html     # Card-blocked specific layout (this file)
└── README-card-blocked-layout.md # This documentation

content/
├── card-blocked-content.html    # Original content (works with common-layout)
├── card-blocked-content-v2.html # New content (works with card-blocked-layout)
└── welcome-content.html         # Welcome email content

templates/config/card-blocked/
├── b2b-european.json            # English config
└── b2b-european-fr.json         # French config
```

## Migration Notes

- Existing templates using `common-layout.html` + `card-blocked-content.html` continue to work
- New templates can use `card-blocked-layout.html` + `card-blocked-content-v2.html`
- Both approaches produce the same visual result
- The new approach has less duplication for similar notification emails
