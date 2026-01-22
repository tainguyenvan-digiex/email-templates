# email-templates Specification

## Purpose
TBD - created by archiving change add-card-blocked-email-template. Update Purpose after archive.
## Requirements
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

### Requirement: Template Configuration System
The system SHALL provide configuration files that define variant-specific values for email templates.

#### Scenario: Configuration file defines all variant values
- **WHEN** a configuration file is created for a template variant
- **THEN** it includes:
  - Color values (primary, footer background, separator color)
  - Gradient definitions (header gradient)
  - Address information (company address)
  - Asset URLs (logo, social media icons)
  - Text content (if variant-specific)

#### Scenario: Configuration schema is documented
- **WHEN** a developer wants to create a new variant
- **THEN** they can reference documentation that explains:
  - All available configuration options
  - Required vs optional values
  - Example configuration files
  - How to use the configuration with the template

### Requirement: Multi-Language Support System
The system SHALL provide language files that define all translatable text content for email templates.

#### Scenario: Language file contains all translatable content
- **WHEN** a language file is created (e.g., `fr.json`, `en.json`)
- **THEN** it includes:
  - Language code identifier
  - Page title and preheader text
  - All heading text (main title parts)
  - Greeting word
  - Card information text (prefix, suffix)
  - Security message text
  - Social media section text
  - Footer text (copyright, unsubscribe)
  - Image alt text translations

#### Scenario: Language files have consistent structure
- **WHEN** multiple language files exist (fr.json, en.json)
- **THEN**:
  - All files have the same key structure
  - All keys are present in all language files
  - Missing translations are clearly identified
  - Structure supports adding new languages easily

#### Scenario: Language selection works with variant configuration
- **WHEN** a variant configuration specifies a language
- **THEN**:
  - The template uses the specified language file
  - Variant-specific content (addresses, legal text) can still be customized
  - Language can be overridden at email send time if needed
  - Both language and variant configurations work together

#### Scenario: New languages can be added easily
- **WHEN** a new language needs to be supported (e.g., Spanish)
- **THEN**:
  - A new language file can be created following the same schema
  - No template HTML changes are required
  - The new language works with all existing variants
  - Translation process is straightforward

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
  - Unsubscribe section variables (provided to layout): `{{footer_unsubscribe_link_text}}`, `{{unsubscribe_url}}`
  - Note: `sent_to_text`, `recipient_email`, `company_address`, and `company_address_url` are hardcoded in the layout

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
  - Sent to email address (hardcoded as `Sent to: c.garreau@greennation.green`)
  - Unsubscribe link (via `{{footer_unsubscribe_link_text}}`, `{{unsubscribe_url}}`)
  - Company address with map link (hardcoded as `205 – 50 Lonsdale Ave #2630, Vancouver, BC V6M 2E6, Canada.`)

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

### Requirement: Welcome Email Configuration System

The system SHALL provide configuration files that define all text content and variant-specific values for the welcome email template.

#### Scenario: B2C configuration exists

- **WHEN** B2C welcome emails need to be sent
- **THEN** a configuration file `b2c.json` exists with:
  - English language (`lang_code: "en"`)
  - B2C primary color (#2CCA97 - turquoise/green)
  - B2C header gradient
  - All text content in English
  - Company details and legal text

#### Scenario: B2B configuration exists

- **WHEN** B2B welcome emails need to be sent
- **THEN** a configuration file `b2b.json` exists with:
  - English language (`lang_code: "en"`)
  - B2B primary color (#3651F3 - blue electric)
  - B2B header gradient
  - All text content in English
  - Company details and legal text

#### Scenario: Configuration includes all template variables

- **WHEN** a configuration file is created for the welcome template
- **THEN** it includes values for all template variables:
  - Styling: `lang_code`, `header_gradient`, `primary_color`
  - User data: `first_name`
  - Page metadata: `title`, `preheader`
  - Welcome section: `heading`, `greeting`, `account_active_message`
  - Features section: `features_title`, `feature_1_title`, `feature_1_description`, `feature_2_title`, `feature_2_description`, `feature_3_title`, `feature_3_description`, `feature_4_title`, `feature_4_description`
  - Impact section: `impact_title`, `impact_description`, `partnership_text`
  - Support section: `support_title`, `support_description`, `chat_button_text`
  - Assistance section: `assistance_title`, `book_call_text`, `book_call_url`, `faq_text`, `faq_url`, `signoff`
  - Footer: `chatbox_image_url`, `company_registration_part1`, `company_registration_part2`, `company_registration_part3`, `legal_text`
  - Unsubscribe: `footer_unsubscribe_link_text`, `unsubscribe_url`
  - Note: `sent_to_text`, `recipient_email`, `company_address`, and `company_address_url` are hardcoded in the layout

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
  - "Sent to" text with recipient email (hardcoded as `Sent to: c.garreau@greennation.green`)
  - Unsubscribe link (via `{{footer_unsubscribe_link_text}}` and `{{unsubscribe_url}}` variables)
  - Company address with map link (hardcoded as `205 – 50 Lonsdale Ave #2630, Vancouver, BC V6M 2E6, Canada.`)

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
  - "Sent to" text with recipient email (hardcoded as `Sent to: c.garreau@greennation.green`)
  - Unsubscribe link via `{{footer_unsubscribe_link_text}}`, `{{unsubscribe_url}}`
  - Company address with map link (hardcoded as `205 – 50 Lonsdale Ave #2630, Vancouver, BC V6M 2E6, Canada.`)

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

### Requirement: Team Invitation Email Template

The system SHALL provide a reusable HTML email template for inviting users to join a Green Nation Business team, supporting English and French languages via configuration files and using the shared-layout.html layout.

#### Scenario: Template renders team invitation in English

- **WHEN** the template is used with English language configuration
- **THEN** it displays:
  - English heading: "✉️ You've been invited to join Green Nation"
  - English subject: "✉️ You've been invited to join Green Nation"
  - English invitation message
  - English CTA button text: "Click here to accept your invitation"
  - English signature: "The Green Nation Team."

#### Scenario: Template renders team invitation in French

- **WHEN** the template is used with French language configuration
- **THEN** it displays:
  - French heading: "✉️ Vous avez été invité(e) à rejoindre Green Nation"
  - French subject: "✉️ Vous avez été invité(e) à rejoindre Green Nation"
  - French invitation message
  - French CTA button text: "Cliquez ici pour accepter votre invitation"
  - French signature: "L'équipe Green Nation."

#### Scenario: Template includes CTA button

- **WHEN** the team invitation email is rendered
- **THEN** it displays a prominent call-to-action button with:
  - Configurable button text via `{{cta_text}}` variable
  - Configurable button URL via `{{cta_url}}` variable
  - Proper button styling (background color, padding, border-radius)
  - Button is clickable and links to invitation acceptance page

### Requirement: Subscription Updated Email Template

The system SHALL provide a reusable HTML email template for notifying users when their subscription plan has been updated, supporting English and French languages and displaying previous/new plan comparison.

#### Scenario: Template displays subscription plan comparison

- **WHEN** the subscription updated email is rendered
- **THEN** it displays:
  - Previous plan name (bolded) via `{{previous_plan}}` variable
  - New plan name (bolded) via `{{new_plan}}` variable
  - Effective date (bolded) via `{{effective_date}}` variable
  - All values are displayed with labels (Previous plan:, New plan:, Effective date:)

#### Scenario: Template renders in English and French

- **WHEN** the template is used with language-specific configuration
- **THEN** all text content (heading, labels, messages, signature) is displayed in the selected language

### Requirement: Unusual Login Alert Email Template

The system SHALL provide a reusable HTML email template for alerting users about suspicious login attempts, displaying IP address, location, and time information.

#### Scenario: Template displays security details

- **WHEN** the unusual login alert email is rendered
- **THEN** it displays:
  - IP address (bolded) via `{{ip_address}}` variable
  - Location (bolded) via `{{location}}` variable
  - Time (bolded) via `{{time}}` variable
  - All values are displayed with labels (IP address:, Location:, Time:)

#### Scenario: Template includes security warning

- **WHEN** the unusual login alert email is rendered
- **THEN** it displays a security warning message with instructions to change password and contact support if unauthorized

### Requirement: Team Member Removed Email Template

The system SHALL provide a reusable HTML email template for notifying team administrators when a team member has been removed.

#### Scenario: Template displays removed user information

- **WHEN** the team member removed email is rendered
- **THEN** it displays:
  - User information (name or email) via `{{removed_user_info}}` variable
  - Message indicating the user has been removed from the company
  - Link to view change history in Team dashboard

### Requirement: New Device Login Email Template

The system SHALL provide a reusable HTML email template for alerting users when their account is accessed from a new device.

#### Scenario: Template displays device information

- **WHEN** the new device login email is rendered
- **THEN** it displays:
  - Device name (bolded) via `{{device_name}}` variable
  - Location (bolded) via `{{location}}` variable
  - Time (bolded) via `{{time}}` variable
  - Security message if unauthorized

### Requirement: Failed Login Attempts Email Template

The system SHALL provide a reusable HTML email template for alerting users about multiple failed login attempts.

#### Scenario: Template displays failed attempt details

- **WHEN** the failed login attempts email is rendered
- **THEN** it displays:
  - Number of failed attempts (bolded) via `{{attempt_count}}` variable
  - Email address where attempts occurred (bolded) via `{{email_address}}` variable
  - Security warning message

### Requirement: Receipt Reminder Email Template

The system SHALL provide a reusable HTML email template for reminding users to upload a receipt for an expense.

#### Scenario: Template displays expense information

- **WHEN** the receipt reminder email is rendered
- **THEN** it displays:
  - Expense amount (bolded) via `{{amount}}` variable
  - Merchant name (bolded) via `{{merchant}}` variable
  - Expense date via `{{expense_date}}` variable
  - Reminder message with CTA to upload receipt

### Requirement: Receipt Final Reminder Email Template

The system SHALL provide a reusable HTML email template for final reminder about missing receipt with prominent CTA button.

#### Scenario: Template includes prominent CTA button

- **WHEN** the receipt final reminder email is rendered
- **THEN** it displays:
  - Number of days since expense via `{{days_since}}` variable
  - Expense amount (bolded) via `{{amount}}` variable
  - Prominent CTA button with text like "Upload my receipt" / "Ajouter mon reçu"
  - Warning message about potential alerts

### Requirement: Missing Receipts Summary Email Template

The system SHALL provide a reusable HTML email template for weekly summary of expenses without receipts.

#### Scenario: Template displays expense list

- **WHEN** the missing receipts summary email is rendered
- **THEN** it displays:
  - List of expenses with format: "Name – Amount – Merchant – Date"
  - Each expense item shows user name, amount, merchant, and date
  - Link to dashboard for follow-up

### Requirement: Maintenance Extended Email Template

The system SHALL provide a reusable HTML email template for notifying users about extended maintenance with new ETA.

#### Scenario: Template displays maintenance ETA

- **WHEN** the maintenance extended email is rendered
- **THEN** it displays:
  - New estimated time of resolution (bolded) via `{{eta}}` variable
  - Message about maintenance taking longer than expected
  - Notification that user will be informed when resolved

### Requirement: Technical Incident Email Template

The system SHALL provide a reusable HTML email template for notifying users about ongoing technical incidents.

#### Scenario: Template displays incident information

- **WHEN** the technical incident email is rendered
- **THEN** it displays:
  - Description of affected services via `{{affected_services}}` variable
  - Message that teams are working on resolution
  - Notification that user will be informed when resolved

### Requirement: Terms Updated Email Template

The system SHALL provide a reusable HTML email template for notifying users about Terms of Service updates.

#### Scenario: Template includes terms review CTA

- **WHEN** the terms updated email is rendered
- **THEN** it displays:
  - Update date via `{{update_date}}` variable
  - CTA button to review terms via `{{cta_text}}` and `{{cta_url}}` variables
  - Deadline message for accepting new terms

### Requirement: Monthly Summary Email Template

The system SHALL provide a reusable HTML email template for monthly account summary with statistics.

#### Scenario: Template displays account statistics

- **WHEN** the monthly summary email is rendered
- **THEN** it displays:
  - Month and year via `{{month}}` and `{{year}}` variables
  - Bulleted list of statistics:
    - Transaction count via `{{transaction_count}}` variable
    - Active users count via `{{active_users}}` variable
    - Total spending (bolded) via `{{total_spending}}` variable
    - Expenses without receipts count via `{{missing_receipts_count}}` variable
  - CTA link to view full details in dashboard

### Requirement: Update Personal Information Email Template

The system SHALL provide a reusable HTML email template for requesting users to update their personal information for compliance.

#### Scenario: Template displays compliance request

- **WHEN** the update personal information email is rendered
- **THEN** it displays:
  - Message about regulatory requirements
  - Request to update identity document or proof of address
  - Instructions to do it in Green Nation app
  - Compliance team signature

### Requirement: KYB Process Started Email Template

The system SHALL provide a reusable HTML email template for notifying users that company verification (KYB) process has started.

#### Scenario: Template includes KYB tracking CTA

- **WHEN** the KYB process started email is rendered
- **THEN** it displays:
  - Message that KYB process has started
  - Instructions to complete required documents
  - CTA button to access KYB tracking via `{{cta_text}}` and `{{cta_url}}` variables
  - Message about tracking progress in company space

### Requirement: Company Verified Email Template

The system SHALL provide a reusable HTML email template for notifying users that their company verification has been completed successfully.

#### Scenario: Template displays success message in English

- **WHEN** the company verified email is rendered with English language configuration
- **THEN** it displays:
  - Success message: "Good news! Your company verification has been successfully completed."
  - Message: "You can now access all features of your Green Nation Business account."
  - Signature: "The Green Nation Team"

#### Scenario: Template displays success message in French

- **WHEN** the company verified email is rendered with French language configuration
- **THEN** it displays:
  - Success message: "Bonne nouvelle ! Votre vérification d'entreprise a été validée avec succès."
  - Message: "Vous avez désormais accès à toutes les fonctionnalités de votre compte Green Nation Business."
  - Signature: "L'équipe Green Nation."

### Requirement: Document Resubmit Required Email Template

The system SHALL provide a reusable HTML email template for requesting users to resubmit a document that failed validation.

#### Scenario: Template displays rejection reason and CTA in English

- **WHEN** the document resubmit required email is rendered with English language configuration
- **THEN** it displays:
  - Message: "The document you submitted could not be validated for the following reason:"
  - Rejection reason (bolded) via `{{rejection_reason}}` variable (e.g., "unreadable / invalid format / expired" - input the relevant one only)
  - CTA message: "👉 Please upload a valid version in your Green Nation Business account to complete verification."
  - CTA button to upload valid document via `{{cta_text}}` and `{{cta_url}}` variables
  - Signature: "The Compliance Team – Green Nation"

#### Scenario: Template displays rejection reason and CTA in French

- **WHEN** the document resubmit required email is rendered with French language configuration
- **THEN** it displays:
  - Message: "Le document que vous avez soumis n'a pas pu être validé pour la raison suivante :"
  - Rejection reason (bolded) via `{{rejection_reason}}` variable (e.g., "illisible / format invalide / expiré" - input the relevant one only)
  - CTA message: "👉 Merci de téléverser une version valide dans votre compte Green Nation Business afin de finaliser la vérification."
  - CTA button to upload valid document via `{{cta_text}}` and `{{cta_url}}` variables
  - Signature: "L'équipe Conformité – Green Nation"

### Requirement: ID Update Required Email Template

The system SHALL provide a reusable HTML email template for requesting users to update their ID document.

#### Scenario: Template displays update request with CTA

- **WHEN** the ID update required email is rendered
- **THEN** it displays:
  - Message about ID being expired or missing
  - CTA button to upload valid document
  - Warning about service interruption

### Requirement: Monthly Statement Ready Email Template

The system SHALL provide a reusable HTML email template for notifying users that their monthly statement is available.

#### Scenario: Template displays statement download CTA

- **WHEN** the monthly statement ready email is rendered
- **THEN** it displays:
  - Month name via `{{month}}` variable
  - CTA button to download statement via `{{cta_text}}` and `{{cta_url}}` variables

### Requirement: Card Temporarily Disabled Email Template

The system SHALL provide a reusable HTML email template for notifying users that their card has been temporarily disabled for security reasons.

#### Scenario: Template displays security message in English

- **WHEN** the card temporarily disabled email is rendered with English language configuration
- **THEN** it displays:
  - Message: "Due to suspicious activity, your card has been disabled."
  - CTA message: "👉 Contact our support to reactivate it."
  - Signature: "The Green Nation Team."

#### Scenario: Template displays security message in French

- **WHEN** the card temporarily disabled email is rendered with French language configuration
- **THEN** it displays:
  - Message: "Suite à une activité suspecte, votre carte a été désactivée."
  - CTA message: "👉 Contactez notre support pour la réactiver."
  - Signature: "L'équipe Green Nation."

### Requirement: Payment Approval Pending Email Template

The system SHALL provide a reusable HTML email template for notifying users that a payment is awaiting approval.

#### Scenario: Template displays payment amount and CTA in English

- **WHEN** the payment approval pending email is rendered with English language configuration
- **THEN** it displays:
  - Message: "A draft payment of {{amount}} is pending approval."
  - Payment amount (bolded) via `{{amount}}` variable (e.g., "€2,300")
  - CTA message: "👉 [Approve or decline in dashboard]"
  - CTA button/link to approve or decline in dashboard via `{{cta_text}}` and `{{cta_url}}` variables
  - Signature: "The Green Nation Team."

#### Scenario: Template displays payment amount and CTA in French

- **WHEN** the payment approval pending email is rendered with French language configuration
- **THEN** it displays:
  - Message: "Un paiement de {{amount}} est en attente de validation."
  - Payment amount (bolded) via `{{amount}}` variable (e.g., "2 300 €")
  - CTA message: "👉 [Valider ou refuser dans votre interface]"
  - CTA button/link to approve or decline in dashboard via `{{cta_text}}` and `{{cta_url}}` variables
  - Signature: "L'équipe Green Nation."

### Requirement: Account Opened Email Template

The system SHALL provide a reusable HTML email template for notifying customers when their account has been opened.

#### Scenario: Template displays account opened message in English

- **WHEN** the account opened email is rendered with English language configuration
- **THEN** it displays:
  - Greeting: "Hi {{first_name}}," (using `{{first_name}}` variable)
  - Welcome message: "Your Green Nation account has been successfully opened. You're now part of a community committed to a more responsible and rewarding future."
  - Information: "You can now access the app, order your card, and start enjoying your benefits."
  - Sign-off: "See you soon,"
  - Signature: "The Green Nation Team"

#### Scenario: Template displays account opened message in French

- **WHEN** the account opened email is rendered with French language configuration
- **THEN** it displays:
  - Greeting: "Bonjour {{first_name}}," (using `{{first_name}}` variable)
  - Welcome message: "Votre compte Green Nation a bien été ouvert. Vous faites désormais partie d'une communauté engagée pour un avenir plus responsable et plus performant."
  - Information: "Vous pouvez dès maintenant accéder à l'app, commander votre carte, et commencer à profiter de tous vos avantages."
  - Sign-off: "À très vite,"
  - Signature: "L'équipe Green Nation"

### Requirement: Account Closed Email Template

The system SHALL provide a reusable HTML email template for confirming that a user's account has been closed.

#### Scenario: Template displays closure confirmation

- **WHEN** the account closed email is rendered
- **THEN** it displays:
  - Confirmation message about account closure
  - Message about returning in the future
  - Thank you message

### Requirement: Password Updated Email Template

The system SHALL provide a reusable HTML email template for confirming that a user's password or PIN has been updated.

#### Scenario: Template displays security confirmation

- **WHEN** the password updated email is rendered
- **THEN** it displays:
  - Confirmation message about password/PIN update
  - Security warning if unauthorized
  - Instructions to contact support if needed

### Requirement: Preferences Updated Email Template

The system SHALL provide a reusable HTML email template for confirming that user preferences have been updated.

#### Scenario: Template displays confirmation message

- **WHEN** the preferences updated email is rendered
- **THEN** it displays:
  - Confirmation about notification/email preferences update
  - Instructions to update preferences from profile in app

### Requirement: Unsubscribed Email Template

The system SHALL provide a reusable HTML email template for confirming that a user has been unsubscribed.

#### Scenario: Template displays unsubscribe confirmation

- **WHEN** the unsubscribed email is rendered
- **THEN** it displays:
  - Confirmation about successful unsubscribe
  - Message about re-subscribing from app or emails
  - Thank you message

### Requirement: Payment Confirmed Email Template

The system SHALL provide a reusable HTML email template for confirming that a payment transaction was successful.

#### Scenario: Template displays payment details in English

- **WHEN** the payment confirmed email is rendered with English language configuration
- **THEN** it displays:
  - Heading: "💸 Payment of {{amount}} to {{merchant}} confirmed"
  - Greeting: "Hi {{first_name}},"
  - Payment message: "Your payment of {{amount}} at {{merchant}} was successful." (with amount and merchant bolded)
  - CTA message: "👉 View transaction history in your app."
  - Security warning: "If this wasn't you, please contact our support immediately."
  - Signature: "The Green Nation Team"

#### Scenario: Template displays payment details in French

- **WHEN** the payment confirmed email is rendered with French language configuration
- **THEN** it displays:
  - Heading: "💸 Paiement de {{amount}} chez {{merchant}} confirmé"
  - Greeting: "Bonjour {{first_name}},"
  - Payment message: "Votre paiement de {{amount}} chez {{merchant}} a bien été effectué." (with amount and merchant bolded)
  - CTA message: "👉 Consultez l'historique de vos transactions dans l'application."
  - Security warning: "Si ce n'était pas vous, contactez notre support immédiatement."
  - Signature: "L'équipe Green Nation."

### Requirement: Transfer Sent Email Template

The system SHALL provide a reusable HTML email template for confirming that a transfer was successfully sent.

#### Scenario: Template displays transfer details in English

- **WHEN** the transfer sent email is rendered with English language configuration
- **THEN** it displays:
  - Heading: "✅ Transfer of {{amount}} sent to {{recipient_name}}"
  - Greeting: "Hi {{first_name}},"
  - Transfer message: "Your transfer of {{amount}} was succesfully sent to {{recipient_name}}." (with amount and recipient_name bolded)
  - CTA message: "👉 View transaction history in your app."
  - Security warning: "If this operation wasn't made by you, please contact our support immediately."
  - Signature: "The Green Nation Team"

#### Scenario: Template displays transfer details in French

- **WHEN** the transfer sent email is rendered with French language configuration
- **THEN** it displays:
  - Heading: "✅ Virement de {{amount}} envoyé à {{recipient_name}}"
  - Greeting: "Bonjour {{first_name}},"
  - Transfer message: "Votre virement de {{amount}} à été envoyé avec succès à {{recipient_name}}." (with amount and recipient_name bolded)
  - CTA message: "👉 Consultez l'historique de vos transactions dans l'application."
  - Security warning: "Si cette opération n'a pas été effectué par vous, contactez notre support immédiatement."
  - Signature: "L'équipe Green Nation."

### Requirement: Card Shipping Email Template

The system SHALL provide a reusable HTML email template for notifying users that their card is being shipped.

#### Scenario: Template displays shipping information in English

- **WHEN** the card shipping email is rendered with English language configuration
- **THEN** it displays:
  - Heading: "📨 Your Green Nation card is on the way"
  - Greeting: "Hi {{first_name}},"
  - Card ordered message: "Your new Green Nation card has been successfully ordered."
  - Delivery info: "It will be delivered to your registered address within 5 to 7 business days."
  - CTA message: "👉 You can track your delivery in the app."
  - Signature: "The Green Nation Team."

#### Scenario: Template displays shipping information in French

- **WHEN** the card shipping email is rendered with French language configuration
- **THEN** it displays:
  - Heading: "📨 Votre carte Green Nation est en cours d'expédition"
  - Greeting: "Bonjour {{first_name}},"
  - Card ordered message: "Votre nouvelle carte Green Nation a bien été commandée."
  - Delivery info: "Elle sera livrée à votre adresse enregistrée sous 5 à 7 jours ouvrés."
  - CTA message: "👉 Vous pouvez suivre la livraison dans l'application."
  - Signature: "L'équipe Green Nation"

### Requirement: Payment Approval Required Email Template

The system SHALL provide a reusable HTML email template for requesting approval of a payment with detailed information.

#### Scenario: Template displays detailed payment information in English

- **WHEN** the payment approval required email is rendered with English language configuration
- **THEN** it displays:
  - Heading: "✅ Approval required: payment of {{amount}}"
  - Greeting: "Hi {{first_name}},"
  - Approval message: "A new payment has been initiated and requires your approval:"
  - Payment amount (bolded) via `{{amount}}` variable
  - Initiated by (bolded) via `{{initiated_by}}` variable
  - Beneficiary (bolded) via `{{beneficiary}}` variable
  - IBAN (masked, bolded) via `{{iban}}` variable
  - CTA message: "👉 You can validate or reject this payment in your Green Nation Business account."
  - Signature: "The Green Nation Team"

#### Scenario: Template displays detailed payment information in French

- **WHEN** the payment approval required email is rendered with French language configuration
- **THEN** it displays:
  - Heading: "✅ Validation requise : paiement de {{amount}}"
  - Greeting: "Bonjour {{first_name}},"
  - Approval message: "Un nouveau paiement a été initié et nécessite votre validation :"
  - Payment amount (bolded) via `{{amount}}` variable
  - Initiated by (bolded) via `{{initiated_by}}` variable
  - Beneficiary (bolded) via `{{beneficiary}}` variable
  - IBAN (masked, bolded) via `{{iban}}` variable
  - CTA message: "👉 Vous pouvez valider ou refuser ce paiement dans votre compte Green Nation Business."
  - Signature: "L'équipe Green Nation"

### Requirement: Account Opening Incomplete Email Template

The system SHALL provide a reusable HTML email template for reminding users to complete their account opening process.

#### Scenario: Template displays completion reminder in English

- **WHEN** the account opening incomplete email is rendered with English language configuration
- **THEN** it displays:
  - Heading: "📝 Complete your Green Nation account opening"
  - Message: "You started creating your Green Nation Business account but didn't complete the process."
  - CTA message: "👉 It only takes a few minutes to finish and unlock all features."
  - App instruction: "Open the Green Nation App to finish opening your account."
  - Signature: "The Green Nation Team"

#### Scenario: Template displays completion reminder in French

- **WHEN** the account opening incomplete email is rendered with French language configuration
- **THEN** it displays:
  - Heading: "📝 Finalisez l'ouverture de votre compte Green Nation"
  - Message: "Vous avez commencé l'ouverture de votre compte Green Nation Business mais n'avez pas terminé le processus."
  - CTA message: "👉 Cela ne prend que quelques minutes pour finaliser et accéder à toutes les fonctionnalités."
  - App instruction: "Ouvre l'app Green Nation pour finaliser l'ouverture de votre compte."
  - Signature: "L'équipe Green Nation"

### Requirement: Call Confirmed Email Template

The system SHALL provide a reusable HTML email template for confirming an Account Manager appointment.

#### Scenario: Template displays appointment details in English

- **WHEN** the call confirmed email is rendered with English language configuration
- **THEN** it displays:
  - Heading: "Your call with your Account Manager is confirmed"
  - Greeting: "Hi {{first_name}},"
  - Confirmation message: "Your appointment with your Green Nation Account Manager is confirmed."
  - Appointment date (with 📅 emoji) via `{{appointment_date}}` variable
  - Appointment time (with 🕒 emoji) via `{{appointment_time}}` variable
  - Location (with 📍 emoji) via `{{location}}` variable (e.g., "[Video call link / phone / details]")
  - Call details message: "During the call, you can ask your questions and get support with your account, transactions, or any specific needs."
  - Reschedule message: "Need to reschedule or cancel? You can do it anytime within the app."
  - Sign-off: "Speak to you soon,"
  - Signature: "The Green Nation Team"

#### Scenario: Template displays appointment details in French

- **WHEN** the call confirmed email is rendered with French language configuration
- **THEN** it displays:
  - Heading: "Votre appel avec votre Account Manager est confirmé"
  - Greeting: "Bonjour {{first_name}},"
  - Confirmation message: "Votre rendez-vous avec votre Account Manager Green Nation a bien été confirmé."
  - Appointment date (with 📅 emoji) via `{{appointment_date}}` variable
  - Appointment time (with 🕒 emoji) via `{{appointment_time}}` variable
  - Location (with 📍 emoji) via `{{location}}` variable (e.g., "[Lien visio / téléphone / précisions]")
  - Call details message: "Lors de cet échange, vous pourrez poser toutes vos questions et être accompagné sur l'usage de votre compte, vos opérations, ou vos besoins spécifiques."
  - Reschedule message: "Besoin de modifier ou annuler ce rendez-vous ? Vous pouvez le faire directement dans votre app."
  - Sign-off: "À très bientôt,"
  - Signature: "L'équipe Green Nation"

### Requirement: Call Rescheduled Email Template

The system SHALL provide a reusable HTML email template for notifying users that their Account Manager appointment has been rescheduled.

#### Scenario: Template displays updated appointment details in English

- **WHEN** the call rescheduled email is rendered with English language configuration
- **THEN** it displays:
  - Heading: "Update – Your call with your Account Manager has been rescheduled"
  - Greeting: "Hi {{first_name}},"
  - Rescheduled message: "Your upcoming call with your Green Nation Account Manager has been rescheduled."
  - Updated details label: "Here are the updated details:"
  - New appointment date (with 📅 emoji) via `{{new_date}}` variable
  - New appointment time (with 🕒 emoji) via `{{new_time}}` variable
  - Location (with 📍 emoji) via `{{location}}` variable
  - Reschedule message: "If this new time still doesn't work for you, feel free to reschedule directly from your app."
  - Signature: "The Green Nation Team"

#### Scenario: Template displays updated appointment details in French

- **WHEN** the call rescheduled email is rendered with French language configuration
- **THEN** it displays:
  - Heading: "Mise à jour de votre rendez-vous avec votre Account Manager"
  - Greeting: "Bonjour {{first_name}},"
  - Rescheduled message: "Votre appel avec votre Account Manager Green Nation a été modifié."
  - Updated details label: "Voici les nouvelles informations :"
  - New appointment date (with 📅 emoji) via `{{new_date}}` variable
  - New appointment time (with 🕒 emoji) via `{{new_time}}` variable
  - Location (with 📍 emoji) via `{{location}}` variable
  - Reschedule message: "Si ce nouvel horaire ne vous convient toujours pas, vous pouvez reprogrammer l'appel à tout moment via votre app."
  - Signature: "L'équipe Green Nation"

### Requirement: Call Cancelled Email Template

The system SHALL provide a reusable HTML email template for notifying users that their Account Manager appointment has been cancelled.

#### Scenario: Template displays cancellation notification in English

- **WHEN** the call cancelled email is rendered with English language configuration
- **THEN** it displays:
  - Heading: "Your call with Green Nation has been cancelled"
  - Greeting: "Hi {{first_name}},"
  - Cancellation message: "Your appointment with your Green Nation Account Manager has been cancelled."
  - Book new call message: "If you'd like to book a new call, you can do so at any time via the app."
  - Support message: "We're here if you need support."
  - Sign-off: "Best regards,"
  - Signature: "The Green Nation Team"

#### Scenario: Template displays cancellation notification in French

- **WHEN** the call cancelled email is rendered with French language configuration
- **THEN** it displays:
  - Heading: "Votre appel avec Green Nation a été annulé"
  - Greeting: "Bonjour {{first_name}},"
  - Cancellation message: "Votre rendez-vous avec votre Account Manager Green Nation a été annulé."
  - Book new call message: "Si vous souhaitez fixer un nouveau rendez-vous, vous pouvez le faire à tout moment depuis l'application."
  - Support message: "Nous restons à votre disposition si vous avez besoin d'assistance."
  - Sign-off: "Cordialement,"
  - Signature: "L'équipe Green Nation"

### Requirement: Call Reminder Email Template

The system SHALL provide a reusable HTML email template for reminding users about an upcoming Account Manager appointment.

#### Scenario: Template displays reminder with appointment details in English

- **WHEN** the call reminder email is rendered with English language configuration
- **THEN** it displays:
  - Heading: "Reminder – Your call with Green Nation is in 1 hour"
  - Greeting: "Hi {{first_name}},"
  - Reminder message: "Just a quick reminder: your call with your Green Nation Account Manager is in 1 hour."
  - Appointment date (with 📅 emoji) via `{{appointment_date}}` variable
  - Appointment time (with 🕒 emoji) via `{{appointment_time}}` variable
  - Join link (with 📍 emoji) via `{{call_link}}` variable
  - Prepare questions message: "Feel free to prepare any questions you may have."
  - Sign-off: "Talk to you soon,"
  - Signature: "The Green Nation Team"

#### Scenario: Template displays reminder with appointment details in French

- **WHEN** the call reminder email is rendered with French language configuration
- **THEN** it displays:
  - Heading: "Rappel – votre appel avec Green Nation dans 1 heure"
  - Greeting: "Bonjour {{first_name}},"
  - Reminder message: "Petit rappel : votre appel avec votre Account Manager Green Nation aura lieu dans une heure."
  - Appointment date (with 📅 emoji) via `{{appointment_date}}` variable
  - Appointment time (with 🕒 emoji) via `{{appointment_time}}` variable
  - Join link (with 📍 emoji) via `{{call_link}}` variable
  - Prepare questions message: "Pensez à préparer vos éventuelles questions pour optimiser l'échange."
  - Sign-off: "À tout à l'heure,"
  - Signature: "L'équipe Green Nation"

### Requirement: Additional Templates Configuration System

The system SHALL provide configuration files for all 35 new email templates, following the established pattern with layout variables at top and dynamic content variables at bottom.

#### Scenario: All templates have English and French configurations

- **WHEN** configuration files are created for new templates
- **THEN** each template has:
  - `en.json` file with English content
  - `fr.json` file with French content
  - Both files follow the same structure (layout vars top, blank line, dynamic vars bottom)
  - Both files include `subject` field matching `heading` field

#### Scenario: Configuration files include all required variables

- **WHEN** a configuration file is created for a new template
- **THEN** it includes:
  - All layout variables (lang_code, header_gradient, primary_color, title, preheader, heading, subject, greeting, social variables, footer variables)
  - All template-specific dynamic content variables
  - Proper JSON structure with blank line separator between sections

### Requirement: Invite Director Access Email Template

The system SHALL provide an email template for inviting users to join a company's Business account as a director, supporting English and French languages.

#### Scenario: Template renders with inviter and company information
- **WHEN** the invite-director-access template is rendered
- **THEN** it displays:
  - Subject line in configured language ("Join the team" / "Rejoignez l'équipe")
  - Inviter's name (`{{inviter_name}}`)
  - Company name (`{{company_name}}`)
  - Invitation message explaining the invitation
  - CTA button to accept the invitation (`{{cta_url}}`)
  - Signature from "The Oxen Team 🌱"

#### Scenario: Template renders in English
- **WHEN** the template is used with English configuration
- **THEN** it displays:
  - Heading: "Join the team"
  - Message: "{{inviter_name}} has invited you to Oxen's {{company_name}} Business account"
  - Greeting: "Hi there,"
  - Description: "Great news! Thanks to {{inviter_name}}, joining Oxen's {{company_name}} Business account is just a click away."
  - Instruction: "Use the button below to accept the invite and get started."

#### Scenario: Template renders in French
- **WHEN** the template is used with French configuration
- **THEN** it displays:
  - Heading: "Rejoignez l'équipe"
  - Message: "{{inviter_name}} vous a invité à rejoindre son compte professionnel {{company_name}} de Oxen"
  - Greeting: "Salut,"
  - Description: "Excellente nouvelle ! Grâce à {{inviter_name}}, rejoindre le compte professionnel {{company_name}} de Oxen se fait en un clic."
  - Instruction: "Utilisez le bouton ci-dessous pour accepter l'invitation et commencer."

#### Scenario: Template uses common layout
- **WHEN** the invite-director-access template is rendered
- **THEN**:
  - It uses common-layout.html for header, footer, and styling
  - Content is defined in content/invite-director-access-content.html
  - Common layout variables are loaded from templates/config/common-layout/[lang].json
  - Template-specific variables are loaded from templates/config/invite-director-access/[lang].json

---

### Requirement: Invite Admin Email Template

The system SHALL provide an email template for inviting users to join the Oxen Platform as an Admin, supporting English and French languages.

#### Scenario: Template renders with admin invitation details
- **WHEN** the invite-admin template is rendered
- **THEN** it displays:
  - Subject line in configured language ("Join the team" / "Rejoignez l'équipe")
  - Recipient's first name (`{{first_name}}`)
  - Admin role specification
  - Account activation CTA button (`{{cta_url}}`)
  - 30-day expiration notice (hardcoded)
  - Signature from "The Oxen Team 🌱"

#### Scenario: Template renders in English
- **WHEN** the template is used with English configuration
- **THEN** it displays:
  - Heading: "Join the team"
  - Greeting: "Hello {{first_name}}"
  - Message: "You have been invited to join the Oxen Platform as an Admin."
  - Instruction: "To get started, please click the link below to activate your account:"
  - Security notice: "This invitation will expire in 30 days for security purposes."

#### Scenario: Template renders in French
- **WHEN** the template is used with French configuration
- **THEN** it displays:
  - Heading: "Rejoignez l'équipe"
  - Greeting: "Bonjour {{first_name}}"
  - Message: "Vous avez été invité à rejoindre la plateforme Oxen en tant qu'administrateur."
  - Instruction: "Pour commencer, veuillez cliquer sur le lien ci-dessous pour activer votre compte :"
  - Security notice: "Cette invitation expirera dans 30 jours pour des raisons de sécurité"

#### Scenario: Template uses common layout
- **WHEN** the invite-admin template is rendered
- **THEN**:
  - It uses common-layout.html for header, footer, and styling
  - Content is defined in content/invite-admin-content.html
  - Common layout variables are loaded from templates/config/common-layout/[lang].json
  - Template-specific variables are loaded from templates/config/invite-admin/[lang].json

---

### Requirement: Approve KYB Email Template

The system SHALL provide an email template for notifying admins about pending KYB (Know Your Business) approval requests, supporting English and French languages.

#### Scenario: Template renders with KYB approval request details
- **WHEN** the approve-kyb template is rendered
- **THEN** it displays:
  - Subject line in configured language ("Submit KYB" / "Submit KYB")
  - Company name requiring approval (`{{company_name}}`)
  - Link to admin console for review (`{{cta_url}}`)
  - Clear call-to-action for approval process
  - Signature from "The Oxen Team 🌱"

#### Scenario: Template renders in English
- **WHEN** the template is used with English configuration
- **THEN** it displays:
  - Heading: "Submit KYB"
  - Greeting: "Hi there,"
  - Message: "A new KYB request Business Name {{company_name}} has been submitted and is waiting for your approval."
  - Instruction: "Please log in to the Oxen Admin Console to review the KYB documentation and complete the approval process"

#### Scenario: Template renders in French
- **WHEN** the template is used with French configuration
- **THEN** it displays:
  - Heading: "Submit KYB"
  - Greeting: "Bonjour,"
  - Message: "Une nouvelle demande KYB pour l'entreprise {{company_name}} été soumise et est en attente de votre approbation."
  - Instruction: "Veuillez vous connecter au Oxen Admin Console pour examiner la documentation KYB et finaliser le processus d'approbation."

#### Scenario: Template uses common layout
- **WHEN** the approve-kyb template is rendered
- **THEN**:
  - It uses common-layout.html for header, footer, and styling
  - Content is defined in content/approve-kyb-content.html
  - Common layout variables are loaded from templates/config/common-layout/[lang].json
  - Template-specific variables are loaded from templates/config/approve-kyb/[lang].json

---

### Requirement: Invite KYC Email Template

The system SHALL provide an email template for inviting users to complete the KYC (Know Your Customer) verification process, supporting English and French languages.

#### Scenario: Template renders with KYC invitation details
- **WHEN** the invite-kyc template is rendered
- **THEN** it displays:
  - Subject line in configured language ("KYC Invitation" / "KYC Invitation")
  - Recipient's first name (`{{first_name}}`)
  - Explanation of KYC purpose
  - CTA button to start verification (`{{cta_url}}`)
  - Signature from "The Oxen Team 🌱"

#### Scenario: Template renders in English
- **WHEN** the template is used with English configuration
- **THEN** it displays:
  - Heading: "KYC Invitation"
  - Message: "{{first_name}} You have been invited to complete the KYC process. This verification ensures secure access to our services."

#### Scenario: Template renders in French
- **WHEN** the template is used with French configuration
- **THEN** it displays:
  - Heading: "KYC Invitation"
  - Message: "Bonjour {{first_name}} Vous êtes invité(e) à compléter la procédure KYC . Cette vérification garantit un accès sécurisé à nos services."

#### Scenario: Template uses common layout
- **WHEN** the invite-kyc template is rendered
- **THEN**:
  - It uses common-layout.html for header, footer, and styling
  - Content is defined in content/invite-kyc-content.html
  - Common layout variables are loaded from templates/config/common-layout/[lang].json
  - Template-specific variables are loaded from templates/config/invite-kyc/[lang].json

---

### Requirement: Verify Email Template

The system SHALL provide an email template for email verification using OTP codes, supporting English and French languages.

#### Scenario: Template renders with OTP code
- **WHEN** the verify-email template is rendered
- **THEN** it displays:
  - Subject line in configured language ("Verify your email" / "Verify your email")
  - OTP code prominently displayed (`{{otp_code}}`)
  - Code validity duration (1 minute, hardcoded)
  - Clear verification instructions
  - Signature from "The Oxen Team 🌱"

#### Scenario: Template renders in English
- **WHEN** the template is used with English configuration
- **THEN** it displays:
  - Heading: "Verify your email"
  - Instruction: "To verify your email for Oxen, please use the OTP below:"
  - OTP code display: "{{otp_code}}"
  - Validity notice: "This code is valid for 1 minute."

#### Scenario: Template renders in French
- **WHEN** the template is used with French configuration
- **THEN** it displays:
  - Heading: "Verify your email"
  - Instruction: "Pour vérifier votre adresse e-mail pour Oxen, veuillez utiliser le code OTP ci-dessous:"
  - OTP code display: "{{otp_code}}"
  - Validity notice: "Ce code est valable pour 1 minute."

#### Scenario: Template uses common layout
- **WHEN** the verify-email template is rendered
- **THEN**:
  - It uses common-layout.html for header, footer, and styling
  - Content is defined in content/verify-email-content.html
  - Common layout variables are loaded from templates/config/common-layout/[lang].json
  - Template-specific variables are loaded from templates/config/verify-email/[lang].json

#### Scenario: OTP code is displayed as prominent text
- **WHEN** the verify-email template renders the OTP code
- **THEN**:
  - OTP code is displayed in a prominent, easy-to-read format
  - Code is large enough to be easily readable
  - Code uses monospace or similar font for clarity
  - Code has sufficient spacing and contrast
  - No CTA button is present (code display only)

### Requirement: Subscription Collection Reminder Email Templates (7-day, 3-day, 24-hour)

The system SHALL provide three progressive subscription renewal reminder email templates that notify users at 7 days, 3 days, and 24 hours before their subscription renewal date, supporting English and French languages via configuration files.

#### Scenario: 7-day reminder displays renewal notice in English

- **WHEN** the subscription-collection-remind-7-days template is rendered with English language configuration
- **THEN** it displays:
  - Heading: "Your Oxen plan will owe soon – Ensure you have funds 💳"
  - Subject: "Your Oxen plan will owe soon – Ensure you have funds 💳"
  - Greeting: "Dear {{first_name}},"
  - Message: "Your Oxen subscription is due soon! 🌍"
  - Instruction: "Make sure you have sufficient funds in your account to keep enjoying all your benefits."
  - Renewal notice: "📅 Renewal in 7 days"
  - Action item: "💡 Check your balance now to avoid any disruption."
  - CTA: "👉 Access your account" (via `{{cta_url}}`)
  - Sign-off: "Thank you,"
  - Signature: "The Oxen Team 🌱"

#### Scenario: 7-day reminder displays renewal notice in French

- **WHEN** the subscription-collection-remind-7-days template is rendered with French language configuration
- **THEN** it displays:
  - Heading: "Votre abonnement Oxen sera bientôt renouvelé – Assurez-vous d'avoir des fonds 💳"
  - Subject: "Votre abonnement Oxen sera bientôt renouvelé – Assurez-vous d'avoir des fonds 💳"
  - Greeting: "Bonjour {{first_name}},"
  - Message: "Votre abonnement Oxen arrive bientôt à échéance ! 🌍"
  - Instruction: "Assurez-vous d'avoir suffisamment de fonds sur votre compte pour continuer à profiter de tous vos avantages."
  - Renewal notice: "📅 Renouvellement prévu dans 7 jours"
  - Action item: "💡 Vérifiez votre solde dès maintenant pour éviter toute interruption."
  - CTA: "👉 Accédez à votre compte" (via `{{cta_url}}`)
  - Sign-off: "Cordialement,"
  - Signature: "L'équipe Oxen 🌱"

#### Scenario: 3-day reminder displays urgent renewal notice in English

- **WHEN** the subscription-collection-remind-3-days template is rendered with English language configuration
- **THEN** it displays:
  - Heading: "Only 3 days left before your Oxen plan renewal ⏳"
  - Subject: "Only 3 days left before your Oxen plan renewal ⏳"
  - Message: "Your Oxen subscription is renewing soon! 🌍"
  - Instruction: "Make sure you have sufficient funds in your account to keep enjoying all your benefits."
  - Renewal notice: "📅 Renewal in 3 days"
  - Action item: "💡 Check your balance now to avoid any disruption."
  - CTA: "👉 Access your account" (via `{{cta_url}}`)

#### Scenario: 3-day reminder displays urgent renewal notice in French

- **WHEN** the subscription-collection-remind-3-days template is rendered with French language configuration
- **THEN** it displays:
  - Heading: "Plus que 3 jours avant le renouvellement de votre abonnement Oxen ⏳"
  - Subject: "Plus que 3 jours avant le renouvellement de votre abonnement Oxen ⏳"
  - Message: "Votre abonnement Oxen sera bientôt renouvelé ! 🌍"
  - Instruction: "Assurez-vous d'avoir suffisamment de fonds sur votre compte pour continuer à profiter de tous vos avantages."
  - Renewal notice: "📅 Renouvellement dans 3 jours"
  - Action item: "💡 Vérifiez votre solde dès maintenant pour éviter toute interruption."
  - CTA: "👉 Accédez à votre compte" (via `{{cta_url}}`)

#### Scenario: 24-hour reminder displays immediate action notice in English

- **WHEN** the subscription-collection-remind-24-hours template is rendered with English language configuration
- **THEN** it displays:
  - Heading: "Your Oxen plan renews tomorrow – Check your balance!"
  - Subject: "Your Oxen plan renews tomorrow – Check your balance!"
  - Message: "Your Oxen subscription renews tomorrow! 🚀"
  - Instruction: "Ensure your account is funded to keep enjoying all your benefits."
  - Renewal notice: "📅 Renewal tomorrow"
  - Action item: "💡 Avoid any disruption, check your balance now."
  - CTA: "👉 Access your account" (via `{{cta_url}}`)

#### Scenario: 24-hour reminder displays immediate action notice in French

- **WHEN** the subscription-collection-remind-24-hours template is rendered with French language configuration
- **THEN** it displays:
  - Heading: "Votre abonnement Oxen est renouvelé demain – Vérifiez votre solde !"
  - Subject: "Votre abonnement Oxen est renouvelé demain – Vérifiez votre solde !"
  - Message: "Votre abonnement Oxen sera renouvelé demain ! 🚀"
  - Instruction: "Assurez-vous que votre compte est suffisamment approvisionné pour continuer à profiter de tous vos avantages."
  - Renewal notice: "📅 Renouvellement demain"
  - Action item: "💡 Évitez toute interruption, vérifiez votre solde maintenant."
  - CTA: "👉 Accédez à votre compte" (via `{{cta_url}}`)

#### Scenario: Reminder templates use shared layout pattern

- **WHEN** subscription reminder templates are created
- **THEN**:
  - Templates use the shared-layout.html pattern for common footer/header elements
  - Configuration files include all layout variables (lang_code, header_gradient, primary_color, etc.)
  - All text content is defined via template variables for language flexibility
  - Templates are email-client compatible (Outlook, Gmail, Apple Mail)

### Requirement: Subscription Payment Failed Warning Email Template

The system SHALL provide an email template for notifying users when subscription payment has failed, with a configurable defer period before service suspension.

#### Scenario: Payment failed warning displays in English with defer period

- **WHEN** the subscription-payment-failed-warning-block template is rendered with English language configuration
- **THEN** it displays:
  - Heading: "Action required: Your plan payment has failed ❌"
  - Subject: "Action required: Your plan payment has failed ❌"
  - Message: "We were unable to process your Oxen subscription payment. Your benefits are now on hold."
  - Defer period notice: "💡 You have {{defer_day}} days to top up your balance to avoid service suspension." (with defer_day variable)
  - Action steps section: "📌 What to do?"
  - Step 1: "✅ Add funds to your Oxen account."
  - Step 2: "✅ We will automatically collect the payment as soon as your balance is sufficient."
  - CTA: "👉 Add Funds" (via `{{cta_url}}`)

#### Scenario: Payment failed warning displays in French with defer period

- **WHEN** the subscription-payment-failed-warning-block template is rendered with French language configuration
- **THEN** it displays:
  - Heading: "Action requise : le paiement de votre abonnement a échoué ❌"
  - Subject: "Action requise : le paiement de votre abonnement a échoué ❌"
  - Message: "Nous n'avons pas pu traiter le paiement de votre abonnement Oxen. Vos avantages sont temporairement suspendus."
  - Defer period notice: "💡 Vous disposez de {{defer_day}} jours pour recharger votre solde afin d'éviter la suspension du service." (with defer_day variable)
  - Action steps section: "📌 Que faire ?"
  - Step 1: "✅ Ajoutez des fonds à votre compte Oxen."
  - Step 2: "✅ Le paiement sera automatiquement prélevé dès que le solde sera suffisant."
  - CTA: "👉 Ajouter des fonds" (via `{{cta_url}}`)

#### Scenario: Template includes defer_day dynamic variable

- **WHEN** the payment failed warning template is used
- **THEN**:
  - Configuration includes `{{defer_day}}` variable for dynamic defer period
  - Variable can be set to any number of days (e.g., 7, 14, 30)
  - Variable is displayed inline within the defer period notice message

### Requirement: Subscription Account Suspend Email Template

The system SHALL provide an email template for notifying users that their account has been suspended due to overdue subscription payment, with information about lost benefits.

#### Scenario: Account suspension displays in English with benefits list

- **WHEN** the subscription-account-suspend template is rendered with English language configuration
- **THEN** it displays:
  - Heading: "Plan suspended: Update your balance now 🚫"
  - Subject: "Plan suspended: Update your balance now 🚫"
  - Message: "Your Oxen subscription has been overdue, and your account has now been suspended."
  - Warning section: "🔴 Without payment, you will permanently lose access to:"
  - Benefits list: "• Tree planting 🌱" (via `{{benefits_list}}` variable for extensibility)
  - Action notice: "💡 To restore access, update your balance now!"
  - CTA: "👉 Update My Balance" (via `{{cta_url}}`)

#### Scenario: Account suspension displays in French with benefits list

- **WHEN** the subscription-account-suspend template is rendered with French language configuration
- **THEN** it displays:
  - Heading: "Abonnement suspendu : mettez à jour votre solde 🚫"
  - Subject: "Abonnement suspendu : mettez à jour votre solde 🚫"
  - Message: "Votre abonnement Oxen est en retard de paiement et votre compte a été suspendu."
  - Warning section: "🔴 Sans paiement, vous perdrez définitivement l'accès à :"
  - Benefits list: "• Plantation d'arbres 🌱" (via `{{benefits_list}}` variable for extensibility)
  - Action notice: "💡 Pour rétablir l'accès, mettez à jour votre solde dès maintenant !"
  - CTA: "👉 Mettre à jour mon solde" (via `{{cta_url}}`)

### Requirement: Automatic Account Closure Warning Email Templates (15-day, Final)

The system SHALL provide two account closure warning email templates for 15 days before closure and final notice (1 day before closure).

#### Scenario: 15-day closure warning displays in English

- **WHEN** the automatic-account-closure-15-day-left template is rendered with English language configuration
- **THEN** it displays:
  - Heading: "Halfway to account deactivation: Update your balance now"
  - Subject: "Halfway to account deactivation: Update your balance now"
  - Greeting: "Hi {{first_name}},"
  - Message: "Your Oxen account is currently halfway to automatic deactivation due to an unpaid subscription."
  - Time remaining: "You still have 15 days to update your balance and keep your account active."
  - CTA: "👉 Access your account" (via `{{cta_url}}`)
  - Signature: "The Oxen Team 🌱"

#### Scenario: 15-day closure warning displays in French

- **WHEN** the automatic-account-closure-15-day-left template is rendered with French language configuration
- **THEN** it displays:
  - Heading: "À mi-parcours avant la désactivation du compte : mettez à jour votre solde"
  - Subject: "À mi-parcours avant la désactivation du compte : mettez à jour votre solde"
  - Greeting: "Bonjour {{first_name}},"
  - Message: "Votre compte Oxen est à mi-chemin de la désactivation automatique en raison d'un abonnement impayé."
  - Time remaining: "Il vous reste 15 jours pour mettre à jour votre solde et conserver votre compte actif."
  - CTA: "👉 Accédez à votre compte" (via `{{cta_url}}`)
  - Signature: "L'équipe Oxen 🌱"

#### Scenario: Final closure warning displays in English

- **WHEN** the automatic-account-closure-final-remind template is rendered with English language configuration
- **THEN** it displays:
  - Heading: "Last chance to prevent account deactivation"
  - Subject: "Last chance to prevent account deactivation"
  - Greeting: "Hi {{first_name}},"
  - Urgent message: "This is your final notice."
  - Deadline: "If payment is not completed by tomorrow, your Oxen account will be automatically closed."
  - CTA: "👉 Access your account" (via `{{cta_url}}`)
  - Signature: "The Oxen Team 🌱"

#### Scenario: Final closure warning displays in French

- **WHEN** the automatic-account-closure-final-remind template is rendered with French language configuration
- **THEN** it displays:
  - Heading: "Dernière chance pour éviter la désactivation du compte"
  - Subject: "Dernière chance pour éviter la désactivation du compte"
  - Greeting: "Bonjour {{first_name}},"
  - Urgent message: "Ceci est votre dernier avertissement."
  - Deadline: "Si le paiement n'est pas effectué d'ici demain, votre compte Oxen sera automatiquement fermé."
  - CTA: "👉 Accédez à votre compte" (via `{{cta_url}}`)
  - Signature: "L'équipe Oxen 🌱"

### Requirement: Account Closed Confirmation Email Template (B2B)

The system SHALL provide an email template confirming that a B2B account has been closed after 60 days of non-payment.

#### Scenario: B2B account closure confirmation displays in English

- **WHEN** the gn-b2b-account-closed-confirmation template is rendered with English language configuration
- **THEN** it displays:
  - Heading: "Account Closed: Payment not received after 60 days"
  - Subject: "Account Closed: Payment not received after 60 days"
  - Greeting: "Hi {{first_name}},"
  - Confirmation message: "We confirm that your Oxen account has been successfully closed."
  - Sign-off: "Thank you for your trust,"
  - Signature: "The Oxen Team 🌱"

#### Scenario: B2B account closure confirmation displays in French

- **WHEN** the gn-b2b-account-closed-confirmation template is rendered with French language configuration
- **THEN** it displays:
  - Heading: "Compte fermé : paiement non reçu après 60 jours"
  - Subject: "Compte fermé : paiement non reçu après 60 jours"
  - Greeting: "Bonjour {{first_name}},"
  - Confirmation message: "Nous confirmons que votre compte Oxen a été fermé avec succès."
  - Sign-off: "Merci pour votre confiance,"
  - Signature: "L'équipe Oxen 🌱"

### Requirement: Compliance Request Approved Email Template

The system SHALL provide an email template for notifying users that their compliance request has been approved.

#### Scenario: Compliance approval displays in English

- **WHEN** the compliance-request-approved template is rendered with English language configuration
- **THEN** it displays:
  - Heading: "Your Request Has Been Approved"
  - Subject: "Your Request Has Been Approved"
  - Greeting: "Dear {{first_name}}," (using first_name variable, not company_name_Value)
  - Approval message: "Your request has been approved. Thank you for providing the necessary information."
  - Sign-off: "Best regards,"
  - Signature: "The Compliance Team"

#### Scenario: Compliance approval displays in French

- **WHEN** the compliance-request-approved template is rendered with French language configuration
- **THEN** it displays:
  - Heading: "Votre demande a été approuvée"
  - Subject: "Votre demande a été approuvée"
  - Greeting: "Bonjour {{first_name}}," (using first_name variable, not company_name_Value)
  - Approval message: "Votre demande a été approuvée. Merci d'avoir fourni les informations nécessaires."
  - Sign-off: "Cordialement,"
  - Signature: "L'équipe Conformité"

### Requirement: Compliance Request Rejected Email Template

The system SHALL provide an email template for notifying users that their compliance request has been rejected, with a dynamic rejection reason.

#### Scenario: Compliance rejection displays in English with reason

- **WHEN** the compliance-request-rejected template is rendered with English language configuration
- **THEN** it displays:
  - Heading: "Your Request Has Been Rejected"
  - Subject: "Your Request Has Been Rejected"
  - Greeting: "Dear {{first_name}}," (using first_name variable, not company_name_Value)
  - Rejection message: "Unfortunately, we could not approve your request. This decision was based on: {{reason}}" (with reason variable)
  - Support message: "If you have any questions or need further assistance, please contact our support team."
  - Sign-off: "Best regards,"
  - Signature: "The Compliance Team"

#### Scenario: Compliance rejection displays in French with reason

- **WHEN** the compliance-request-rejected template is rendered with French language configuration
- **THEN** it displays:
  - Heading: "Votre demande a été rejetée"
  - Subject: "Votre demande a été rejetée"
  - Greeting: "Bonjour {{first_name}}," (using first_name variable, not company_name_Value)
  - Rejection message: "Malheureusement, nous n'avons pas pu approuver votre demande. Cette décision est basée sur: {{reason}}" (with reason variable)
  - Support message: "Si vous avez des questions ou avez besoin d'une assistance supplémentaire, veuillez contacter notre service client"
  - Sign-off: "Cordialement,"
  - Signature: "L'équipe Conformité"

#### Scenario: Template includes dynamic reason variable

- **WHEN** the compliance rejection template is used
- **THEN**:
  - Configuration includes `{{reason}}` variable for dynamic rejection reason
  - Variable can contain specific rejection reasons (e.g., "incomplete documents", "invalid information")
  - Variable is displayed inline within the rejection message

### Requirement: Compliance Request Additional Information Email Template

The system SHALL provide an email template for requesting additional information from users for compliance verification.

#### Scenario: Additional information request displays in English

- **WHEN** the compliance-request-need-additional-information template is rendered with English language configuration
- **THEN** it displays:
  - Heading: "Additional Information Required for Your Request"
  - Subject: "Additional Information Required for Your Request"
  - Greeting: "Hello {{first_name}}," (using first_name variable, not company_name_Value)
  - Request message: "we need more information to process your request."
  - Instructions: "Please upload the required documents through your app to continue with the verification process."
  - Support message: "If you have any questions or need help, feel free to reach out to our support team."
  - Sign-off: "Best regards,"
  - Signature: "The Compliance Team"

#### Scenario: Additional information request displays in French

- **WHEN** the compliance-request-need-additional-information template is rendered with French language configuration
- **THEN** it displays:
  - Heading: "Informations supplémentaires requises pour votre demande"
  - Subject: "Informations supplémentaires requises pour votre demande"
  - Greeting: "Bonjour {{first_name}}," (using first_name variable, not company_name_Value)
  - Request message: "nous avons besoin de plus d'informations pour traiter votre demande."
  - Instructions: "Veuillez télécharger les documents requis via votre application pour continuer le processus de vérification."
  - Support message: "Si vous avez des questions ou avez besoin d'aide, n'hésitez pas à contacter notre équipe d'assistance."
  - Sign-off: "Cordialement,"
  - Signature: "L'équipe Conformité"

### Requirement: Template Configuration Standardization

The system SHALL ensure all new templates follow the established configuration file structure and naming conventions.

#### Scenario: Configuration files follow standard structure

- **WHEN** configuration files are created for new templates
- **THEN**:
  - Each template has a dedicated config directory: `templates/config/[template-name]/`
  - Each config directory contains `en.json` and `fr.json` files
  - Configuration files include layout variables at top (lang_code, header_gradient, primary_color, title, preheader, heading, subject)
  - Blank line separates layout variables from content variables
  - Content variables are listed at bottom (greeting, message content, CTA text, signature, etc.)
  - All configuration files follow valid JSON syntax

#### Scenario: Templates use Oxen branding consistently

- **WHEN** any new template is rendered
- **THEN**:
  - All references use "Oxen" brand name (not "Green Nation")
  - Templates use `{{first_name}}` variable for personalization
  - No hardcoded "companyName_Value" or "company_name_Value" references exist
  - Brand consistency is maintained across English and French versions

#### Scenario: Templates include required template variables

- **WHEN** a new template configuration is created
- **THEN** it includes:
  - `lang_code` - Language code (en, fr)
  - `header_gradient` - Header gradient CSS value
  - `primary_color` - Primary brand color
  - `title` - Email page title (for browser tab)
  - `preheader` - Preview text for email clients
  - `heading` - Main email heading
  - `subject` - Email subject line (matching heading)
  - `first_name` - User's first name for personalization
  - `signature` - Email signature text
  - Template-specific variables (defer_day, reason, benefits_list, cta_url, etc.)

