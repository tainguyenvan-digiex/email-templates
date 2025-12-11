## ADDED Requirements

### Requirement: Postmark Layout System

The system SHALL provide a reusable Postmark layout file that contains common components shared across all email templates.

#### Scenario: Layout contains common CSS styles
- **WHEN** the layout file is created
- **THEN** it includes:
  - Common CSS reset styles (body, table, td, img)
  - Responsive media queries for mobile devices
  - Footer-specific CSS classes (footer-text, footer-social-icon)
  - Unsubscribe-specific CSS classes (unsubscribe-text)
  - Common utility classes (mobile-padding, mobile-stack, mobile-center)

#### Scenario: Layout contains footer section
- **WHEN** the layout file is created
- **THEN** it includes the complete footer section with:
  - Wave decoration image
  - Footer logo (Green Nation logo-footer.png)
  - Chatbox/automated email notice image (via `{{chatbox_image_url}}` variable)
  - Horizontal separator line (#43e8b3 color)
  - Social media icons (Instagram, TikTok, LinkedIn)
  - Copyright text ("© Green Nation 2025")
  - Company registration information (via `{{company_registration_part1}}`, `{{company_registration_part2}}`, `{{company_registration_part3}}` variables)
  - Legal text (via `{{legal_text}}` variable)

#### Scenario: Layout contains unsubscribe section
- **WHEN** the layout file is created
- **THEN** it includes the complete unsubscribe section with:
  - "Sent to" text with recipient email (via `{{recipient_email}}` variable)
  - Unsubscribe link (via `{{footer_unsubscribe_link_text}}` and `{{unsubscribe_url}}` variables)
  - Company address with map link (via `{{company_address}}` and `{{company_address_url}}` variables)

#### Scenario: Layout uses Postmark content placeholder
- **WHEN** the layout file is created
- **THEN** it includes `{{{ content }}}` placeholder (triple braces) where template-specific content will be inserted
- **AND** the placeholder is positioned between header structure and footer section

#### Scenario: Layout can be uploaded to Postmark
- **WHEN** the layout file is ready
- **THEN**:
  - It follows Postmark layout format requirements
  - It can be uploaded to Postmark server via UI or API
  - Templates can be associated with the layout in Postmark
  - All template variables used in layout are documented

#### Scenario: Content files reference layout
- **WHEN** content files are created for templates
- **THEN**:
  - Content files contain only template-specific content (header, body sections)
  - Content files do not include footer, unsubscribe, or common CSS
  - Content files are designed to be inserted into layout's `{{{ content }}}` placeholder
  - Original template files (`templates/welcome.html`, `templates/card-blocked.html`) remain unchanged for backward compatibility
  - Content files are uploaded to Postmark as templates and associated with the layout

### Requirement: Template Content Files

The system SHALL provide content-only files for email templates that contain only template-specific sections, designed to be used with Postmark layouts.

#### Scenario: Welcome content file contains only template-specific sections
- **WHEN** the welcome content file is created
- **THEN** `content/welcome-content.html` contains:
  - Header section (logo, heading, greeting, account active message, welcome button, iPhone background)
  - Features section (features title, 4 feature items with icons and descriptions)
  - Impact title section
  - Personalized support section (image and text)
  - Partnership section (text and carbon offset image)
  - Need assistance section (title, book call CTA, FAQ CTA, sign-off)
- **AND** it does NOT contain:
  - Footer section
  - Unsubscribe section
  - CSS styles in `<head>`
  - HTML document structure (`<!DOCTYPE>`, `<html>`, `<head>`, `<body>` tags)

#### Scenario: Card-blocked content file contains only template-specific sections
- **WHEN** the card-blocked content file is created
- **THEN** `content/card-blocked-content.html` contains:
  - Header section (logo, heading with card blocked message, greeting, card information, security message)
  - Social media promotion section (title, social icons, hashtags)
- **AND** it does NOT contain:
  - Footer section
  - Unsubscribe section
  - CSS styles in `<head>`
  - HTML document structure (`<!DOCTYPE>`, `<html>`, `<head>`, `<body>` tags)

#### Scenario: Content files preserve template variables
- **WHEN** content files are created
- **THEN**:
  - All template variables from original templates are preserved
  - Variables used in layout (footer, unsubscribe) are documented but not included in content files
  - Content files can be combined with layout to produce complete email templates
  - Variable replacement works correctly when content is inserted into layout

#### Scenario: Original template files remain unchanged
- **WHEN** content files are created
- **THEN**:
  - `templates/welcome.html` remains unchanged (preserved for backward compatibility and reference)
  - `templates/card-blocked.html` remains unchanged (preserved for backward compatibility and reference)
  - Content files are separate files in `content/` directory
  - Original templates can still be used independently if needed

## MODIFIED Requirements

### Requirement: Card Blocked Email Template

The system SHALL provide a generic, reusable HTML email template for notifying users when their card has been blocked, supporting multiple variants through configuration and multiple languages. The template SHALL use a Postmark layout for common components (footer, unsubscribe, CSS).

#### Scenario: Template renders in French language
- **WHEN** the template is used with French language configuration
- **THEN** it displays:
  - French title: "Votre carte a été bloquée - Green Nation"
  - French heading: "VOTRE CARTE A ÉTÉ BLOQUÉE, VÉRIFIEZ VOTRE COMPTE 🔔"
  - French greeting: "Bonjour {{first_name}},"
  - French card information text
  - French security message
  - French social media section text
  - French footer text (rendered via Postmark layout)
  - All text content in French

#### Scenario: Template renders in English language
- **WHEN** the template is used with English language configuration
- **THEN** it displays:
  - English title: "Your card has been blocked - Green Nation"
  - English heading: "YOUR CARD HAS BEEN BLOCKED, VERIFY YOUR ACCOUNT 🔔"
  - English greeting: "Hello {{first_name}},"
  - English card information text
  - English security message
  - English social media section text
  - English footer text (rendered via Postmark layout)
  - All text content in English

#### Scenario: Language can be selected at email send time
- **WHEN** an email is sent with a specific language parameter
- **THEN**:
  - The template uses the specified language file (fr.json or en.json)
  - All text content is replaced with translations from the selected language
  - The HTML `lang` attribute matches the selected language
  - User-specific variables ({{first_name}}, {{card_last_four}}) are still replaced correctly
  - Footer and unsubscribe sections are rendered via Postmark layout with language-specific variables

#### Scenario: Template variables are replaced correctly with language content
- **WHEN** template variables are replaced with language file values
- **THEN**:
  - All `{{lang.*}}` placeholders are replaced with translated text
  - HTML structure remains valid
  - Email client compatibility is maintained
  - No hardcoded language-specific text remains
  - Layout variables (footer, unsubscribe) are provided by template configuration

#### Scenario: Card-blocked content file uses Postmark layout
- **WHEN** the card-blocked content file is created
- **THEN**:
  - Content file (`content/card-blocked-content.html`) contains only template-specific content (header with card info, social media section)
  - Content file does not include footer, unsubscribe, or CSS
  - Footer section is rendered via Postmark layout
  - Unsubscribe section is rendered via Postmark layout
  - Common CSS styles are provided by Postmark layout
  - Content file is uploaded to Postmark as a template and associated with common layout
  - Original template file (`templates/card-blocked.html`) remains unchanged

### Requirement: Welcome Email Template

The system SHALL provide a generic, reusable HTML email template for welcoming new users when their account is activated, supporting multiple variants through configuration and multiple languages via template variables. The template SHALL use a Postmark layout for common components (footer, unsubscribe, CSS).

#### Scenario: Template uses variables for all text content

- **WHEN** the welcome email template is created
- **THEN** all text content SHALL be template variables using `{{variable_name}}` syntax:
  - Page metadata: `{{title}}`, `{{preheader}}`, `{{lang_code}}`
  - Welcome section: `{{heading}}`, `{{greeting}}`, `{{first_name}}`, `{{account_active_message}}`
  - Features section: `{{features_title}}`, `{{feature_1_title}}`, `{{feature_1_description}}`, `{{feature_2_title}}`, `{{feature_2_description}}`, `{{feature_3_title}}`, `{{feature_3_description}}`, `{{feature_4_title}}`, `{{feature_4_description}}`
  - Impact section: `{{impact_title}}`, `{{impact_description}}`, `{{partnership_text}}`
  - Support section: `{{support_title}}`, `{{support_description}}`, `{{chat_button_text}}`
  - Assistance section: `{{assistance_title}}`, `{{book_call_text}}`, `{{book_call_url}}`, `{{faq_text}}`, `{{faq_url}}`, `{{signoff}}`
  - Footer section variables (provided to layout): `{{chatbox_image_url}}`, `{{company_registration_part1}}`, `{{company_registration_part2}}`, `{{company_registration_part3}}`, `{{legal_text}}`
  - Unsubscribe section variables (provided to layout): `{{footer_unsubscribe_link_text}}`, `{{unsubscribe_url}}`, `{{company_address}}`, `{{company_address_url}}`, `{{recipient_email}}`

#### Scenario: Template renders welcome content in English language

- **WHEN** the template is used with English language configuration
- **THEN** it displays:
  - English title: "Welcome to Green Nation – Your account is active"
  - English welcome heading: "WELCOME TO GREEN NATION"
  - English greeting: "Hello {{first_name}},"
  - English account activation message
  - English feature descriptions (SEPA & SWIFT transfers, Multi-currency accounts, Physical & virtual cards, Real-time tracking)
  - English impact section text
  - English personalized support section
  - English need assistance section
  - English footer text (rendered via Postmark layout)

#### Scenario: Template supports future multilanguage addition

- **WHEN** a new language needs to be added in the future (e.g., French)
- **THEN**:
  - New configuration files can be created with translated text values
  - All `{{variable}}` placeholders are replaced with translated content
  - No template HTML changes are required for language addition
  - The HTML `lang` attribute uses `{{lang_code}}` variable
  - Layout footer/unsubscribe variables are provided in language-specific configuration

#### Scenario: Template includes features overview section

- **WHEN** the welcome email is rendered
- **THEN** it displays a features grid with:
  - SEPA & SWIFT transfers feature with icon and description
  - Multi-currency accounts feature with icon and description
  - Physical & virtual cards feature with icon and description
  - Real-time tracking feature with icon and description

#### Scenario: Template includes impact/partnership section

- **WHEN** the welcome email is rendered
- **THEN** it displays:
  - Section title about making impact grow
  - Partnership information with Veritree
  - Carbon offset information based on subscription

#### Scenario: Template includes personalized support section

- **WHEN** the welcome email is rendered
- **THEN** it displays:
  - Personalized support heading
  - Information about Account Manager communication
  - Chat with Charlie option

#### Scenario: Template includes need assistance section

- **WHEN** the welcome email is rendered
- **THEN** it displays:
  - Need assistance heading
  - Book a call CTA button with link
  - FAQ access CTA button with link
  - Sign-off from Green Nation team

#### Scenario: Template reuses header structure from card-blocked

- **WHEN** the welcome email is rendered
- **THEN** it displays:
  - Same gradient header background (configurable via `{{header_gradient}}`)
  - Same logo placement in top-right corner
  - Same Poppins font family styling

#### Scenario: Template reuses footer structure via Postmark layout

- **WHEN** the welcome email is rendered
- **THEN** it displays (via Postmark layout):
  - Same wave decoration image
  - Same dark blue footer background (#0E174C)
  - Same footer logo placement
  - Same chatbox/automated email notice image (via `{{chatbox_image_url}}`)
  - Same horizontal separator line
  - Same social media icons (Instagram, TikTok, LinkedIn)
  - Same copyright text
  - Same company registration information (via variables)
  - Same legal text (via `{{legal_text}}`)

#### Scenario: Template reuses unsubscribe section via Postmark layout

- **WHEN** the welcome email is rendered
- **THEN** it displays (via Postmark layout):
  - Sent to email address (via `{{recipient_email}}`)
  - Unsubscribe link (via `{{footer_unsubscribe_link_text}}`, `{{unsubscribe_url}}`)
  - Company address with map link (via `{{company_address}}`, `{{company_address_url}}`)

#### Scenario: Welcome content file uses Postmark layout
- **WHEN** the welcome content file is created
- **THEN**:
  - Content file (`content/welcome-content.html`) contains only template-specific content (header, features, impact, support, assistance sections)
  - Content file does not include footer, unsubscribe, or CSS
  - Footer section is rendered via Postmark layout
  - Unsubscribe section is rendered via Postmark layout
  - Common CSS styles are provided by Postmark layout
  - Content file is uploaded to Postmark as a template and associated with common layout
  - Original template file (`templates/welcome.html`) remains unchanged

