## ADDED Requirements

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
