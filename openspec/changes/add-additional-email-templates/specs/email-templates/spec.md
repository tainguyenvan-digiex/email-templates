# email-templates Specification Delta

## ADDED Requirements

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
