# email-templates Specification Deltas

## ADDED Requirements

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
