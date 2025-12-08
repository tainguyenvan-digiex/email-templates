# email-templates Specification

## Purpose
TBD - created by archiving change add-card-blocked-email-template. Update Purpose after archive.
## Requirements
### Requirement: Card Blocked Email Template
The system SHALL provide a generic, reusable HTML email template for notifying users when their card has been blocked, supporting multiple variants through configuration and multiple languages.

#### Scenario: Template renders in French language
- **WHEN** the template is used with French language configuration
- **THEN** it displays:
  - French title: "Votre carte a été bloquée - Green Nation"
  - French heading: "VOTRE CARTE A ÉTÉ BLOQUÉE, VÉRIFIEZ VOTRE COMPTE 🔔"
  - French greeting: "Bonjour {{first_name}},"
  - French card information text
  - French security message
  - French social media section text
  - French footer text
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
  - English footer text
  - All text content in English

#### Scenario: Language can be selected at email send time
- **WHEN** an email is sent with a specific language parameter
- **THEN**:
  - The template uses the specified language file (fr.json or en.json)
  - All text content is replaced with translations from the selected language
  - The HTML `lang` attribute matches the selected language
  - User-specific variables ({{first_name}}, {{card_last_four}}) are still replaced correctly

#### Scenario: Template variables are replaced correctly with language content
- **WHEN** template variables are replaced with language file values
- **THEN**:
  - All `{{lang.*}}` placeholders are replaced with translated text
  - HTML structure remains valid
  - Email client compatibility is maintained
  - No hardcoded language-specific text remains

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

