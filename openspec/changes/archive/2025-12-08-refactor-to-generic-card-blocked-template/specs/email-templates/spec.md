## MODIFIED Requirements

### Requirement: Card Blocked Email Template
The system SHALL provide a generic, reusable HTML email template for notifying users when their card has been blocked, supporting multiple variants through configuration.

#### Scenario: User receives card blocked notification
- **WHEN** a card is blocked from the Green Nation application
- **THEN** the user receives an email with:
  - Personalized greeting using their first name
  - Last 4 digits of the blocked card displayed prominently
  - Security warning message with instructions to contact support if unauthorized
  - Green Nation branding and logo
  - Social media promotion section
  - Footer with legal disclaimers and unsubscribe link

#### Scenario: Email renders correctly across clients
- **WHEN** the email is opened in major email clients (Gmail, Outlook, Apple Mail)
- **THEN** the template displays correctly with:
  - Proper gradient background in header (configurable per variant)
  - Correct logo positioning
  - Readable text with proper contrast
  - Functional links and social media icons
  - Responsive layout on mobile devices

#### Scenario: Email includes required legal elements
- **WHEN** the email is sent
- **THEN** it includes:
  - Automatic email disclaimer
  - Unsubscribe link
  - Company address and legal registration information (configurable per variant)
  - Copyright notice

#### Scenario: Template renders with B2B France configuration
- **WHEN** the template is used with B2B France configuration
- **THEN** it displays:
  - Blue gradient header background (#3651F3)
  - Paris address
  - B2B-specific legal text and registration info

#### Scenario: Template renders with B2C France configuration
- **WHEN** the template is used with B2C France configuration
- **THEN** it displays:
  - Green gradient header background (#2CCA97)
  - Paris address
  - B2C-specific legal text and registration info

#### Scenario: Template renders with B2B European configuration
- **WHEN** the template is used with B2B European configuration
- **THEN** it displays:
  - Blue gradient header background (#3651F3)
  - European address
  - B2B-specific legal text

#### Scenario: Template renders with B2C European configuration
- **WHEN** the template is used with B2C European configuration
- **THEN** it displays:
  - Green gradient header background (#2CCA97)
  - European address
  - B2C-specific legal text

#### Scenario: Template renders with B2B International configuration
- **WHEN** the template is used with B2B International configuration
- **THEN** it displays:
  - Blue gradient header background (#3651F3)
  - International address
  - B2B-specific legal text

#### Scenario: Template renders with B2C International configuration
- **WHEN** the template is used with B2C International configuration
- **THEN** it displays:
  - Green gradient header background (#2CCA97)
  - International address
  - B2C-specific legal text

#### Scenario: Template variables are replaced correctly
- **WHEN** template variables are replaced with configuration values
- **THEN**:
  - All `{{variable}}` placeholders are replaced with actual values
  - HTML structure remains valid
  - Email client compatibility is maintained
  - No broken references or missing content

#### Scenario: New variant can be created through configuration
- **WHEN** a new variant configuration file is created
- **THEN**:
  - The same template HTML can be used
  - Only configuration values need to be changed
  - No HTML code duplication is required
  - Variant renders correctly with new styling/content

## ADDED Requirements

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

