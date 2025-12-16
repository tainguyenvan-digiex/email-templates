## ADDED Requirements

### Requirement: Card-Blocked Postmark Layout

The system SHALL provide a specialized Postmark layout file for card-blocked type emails (security notifications) that contains common header components (logo, heading, greeting) and footer components (social media promotion, footer, unsubscribe).

#### Scenario: Layout contains logo row section

- **WHEN** the card-blocked layout is created
- **THEN** it includes a logo row section with:
  - Green Nation logo image (top-right placement)
  - Logo image URL: `https://referral-dev.greennation.green/b2b/emails/assets/logo.png`
  - Padding and styling consistent with card-blocked email design

#### Scenario: Layout contains header with gradient background

- **WHEN** the card-blocked layout is created
- **THEN** it includes a header section with:
  - Configurable gradient background via `{{header_gradient}}` variable
  - Primary color fallback via `{{primary_color}}` variable
  - Space for heading and greeting sections

#### Scenario: Layout contains heading section

- **WHEN** the card-blocked layout is created
- **THEN** it includes a heading section with:
  - Template variable `{{heading_part1}}` (first part of heading)
  - Template variable `{{heading_part2}}` (second part, different styling)
  - Template variable `{{heading_part3}}` (third part with emoji)
  - Centered text with uppercase styling
  - Text shadow for readability

#### Scenario: Layout contains greeting section

- **WHEN** the card-blocked layout is created
- **THEN** it includes a greeting section with:
  - Template variable `{{greeting}}` (e.g., "Hello", "Bonjour")
  - Template variable `{{first_name}}` (user's first name)
  - Format: `{{greeting}} {{first_name}},`
  - Proper styling (font size, weight, color)

#### Scenario: Layout contains content placeholder

- **WHEN** the card-blocked layout is created
- **THEN** it includes:
  - Postmark content placeholder `{{{ @content }}}` (triple braces)
  - Placeholder positioned after greeting, before social media section
  - Template-specific body content is inserted at this placeholder

#### Scenario: Layout contains social media promotion section

- **WHEN** the card-blocked layout is created
- **THEN** it includes a social media promotion section with:
  - Section title via `{{social_title}}` variable
  - Social media icons (Instagram, TikTok, LinkedIn) with links
  - Hashtags via `{{social_hashtags_part1}}`, `{{social_hashtags_part2}}`, `{{social_hashtags_part3}}` variables
  - White background styling

#### Scenario: Layout contains footer section

- **WHEN** the card-blocked layout is created
- **THEN** it includes the footer section with:
  - Wave decoration image
  - Footer logo (Green Nation logo-footer.png)
  - Chatbox/automated email notice image via `{{chatbox_image_url}}`
  - Horizontal separator line (#43e8b3 color)
  - Social media icons (small version)
  - Copyright text ("© Green Nation 2025")
  - Company registration via `{{company_registration_part1}}`, `{{company_registration_part2}}`, `{{company_registration_part3}}`
  - Legal text via `{{legal_text}}`

#### Scenario: Layout contains unsubscribe section

- **WHEN** the card-blocked layout is created
- **THEN** it includes the unsubscribe section with:
  - "Sent to" text with recipient email via `{{sent_to_text}}`, `{{recipient_email}}`
  - Unsubscribe link via `{{footer_unsubscribe_link_text}}`, `{{unsubscribe_url}}`
  - Company address with map link via `{{company_address}}`, `{{company_address_url}}`

#### Scenario: Layout can be uploaded to Postmark

- **WHEN** the layout file is ready
- **THEN**:
  - It follows Postmark layout format requirements
  - It can be uploaded to Postmark server via UI or API
  - Templates can be associated with the layout in Postmark
  - All template variables are documented

### Requirement: Card-Blocked Content File V2

The system SHALL provide a content file version 2 for card-blocked emails that contains only template-specific body content (card information and security message), designed to work with the card-blocked layout.

#### Scenario: Content file contains only card-specific sections

- **WHEN** `content/card-blocked-content-v2.html` is created
- **THEN** it contains only:
  - Card Information section (card_info_prefix, card_last_four, card_info_suffix)
  - Security Message section (security_warning_part1, security_warning_part2, security_signature)

#### Scenario: Content file does not duplicate layout sections

- **WHEN** `content/card-blocked-content-v2.html` is created
- **THEN** it does NOT contain:
  - Logo row (provided by layout)
  - Heading section (provided by layout)
  - Greeting section (provided by layout)
  - Social Media Promotion section (provided by layout)
  - Footer section (provided by layout)
  - Unsubscribe section (provided by layout)
  - CSS styles (provided by layout)
  - HTML document structure (provided by layout)

#### Scenario: Original content file remains unchanged

- **WHEN** the new content file is created
- **THEN**:
  - `content/card-blocked-content.html` remains unchanged
  - `content/card-blocked-content-v2.html` is a new separate file
  - Both files can coexist
  - Existing templates using original file continue to work

