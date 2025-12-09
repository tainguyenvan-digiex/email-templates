## ADDED Requirements

### Requirement: Welcome Email Template

The system SHALL provide a generic, reusable HTML email template for welcoming new users when their account is activated, supporting multiple variants through configuration and multiple languages via template variables.

#### Scenario: Template uses variables for all text content

- **WHEN** the welcome email template is created
- **THEN** all text content SHALL be template variables using `{{variable_name}}` syntax:
  - Page metadata: `{{title}}`, `{{preheader}}`, `{{lang_code}}`
  - Welcome section: `{{heading}}`, `{{greeting}}`, `{{first_name}}`, `{{account_active_message}}`
  - Features section: `{{features_title}}`, `{{feature_1_title}}`, `{{feature_1_description}}`, `{{feature_2_title}}`, `{{feature_2_description}}`, `{{feature_3_title}}`, `{{feature_3_description}}`, `{{feature_4_title}}`, `{{feature_4_description}}`
  - Impact section: `{{impact_title}}`, `{{impact_description}}`, `{{partnership_text}}`
  - Support section: `{{support_title}}`, `{{support_description}}`, `{{chat_button_text}}`
  - Assistance section: `{{assistance_title}}`, `{{book_call_text}}`, `{{book_call_url}}`, `{{faq_text}}`, `{{faq_url}}`, `{{signoff}}`
  - Footer section: `{{chatbox_image_url}}`, `{{company_registration_part1}}`, `{{company_registration_part2}}`, `{{company_registration_part3}}`, `{{legal_text}}`
  - Unsubscribe section: `{{footer_unsubscribe_link_text}}`, `{{unsubscribe_url}}`, `{{company_address}}`, `{{company_address_url}}`

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
  - English footer text

#### Scenario: Template supports future multilanguage addition

- **WHEN** a new language needs to be added in the future (e.g., French)
- **THEN**:
  - New configuration files can be created with translated text values
  - All `{{variable}}` placeholders are replaced with translated content
  - No template HTML changes are required for language addition
  - The HTML `lang` attribute uses `{{lang_code}}` variable

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

#### Scenario: Template reuses footer structure from card-blocked

- **WHEN** the welcome email is rendered
- **THEN** it displays:
  - Same wave decoration image
  - Same dark blue footer background (#0E174C)
  - Same footer logo placement
  - Same chatbox/automated email notice image (via `{{chatbox_image_url}}`)
  - Same horizontal separator line
  - Same social media icons (Instagram, TikTok, LinkedIn)
  - Same copyright text
  - Same company registration information (via variables)
  - Same legal text (via `{{legal_text}}`)

#### Scenario: Template reuses unsubscribe section from card-blocked

- **WHEN** the welcome email is rendered
- **THEN** it displays:
  - Sent to email address
  - Unsubscribe link (via `{{footer_unsubscribe_link_text}}`, `{{unsubscribe_url}}`)
  - Company address with map link (via `{{company_address}}`, `{{company_address_url}}`)

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
  - Unsubscribe: `footer_unsubscribe_link_text`, `unsubscribe_url`, `company_address`, `company_address_url`
