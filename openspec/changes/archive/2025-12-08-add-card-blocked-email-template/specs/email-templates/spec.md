## ADDED Requirements

### Requirement: Card Blocked Email Template
The system SHALL provide an HTML email template for notifying users when their card has been blocked.

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
  - Proper gradient background in header
  - Correct logo positioning
  - Readable text with proper contrast
  - Functional links and social media icons
  - Responsive layout on mobile devices

#### Scenario: Email includes required legal elements
- **WHEN** the email is sent
- **THEN** it includes:
  - Automatic email disclaimer
  - Unsubscribe link
  - Company address and legal registration information
  - Copyright notice

