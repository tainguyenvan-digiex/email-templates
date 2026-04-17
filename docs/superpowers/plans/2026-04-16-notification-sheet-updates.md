# Notification Sheet Updates Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Apply all client-requested changes from the new notification sheet to email template configs and HTML content files.

**Architecture:** Changes fall into four categories — (1) contact redirection from "support" to "account manager", (2) security/compliance team name branding, (3) content additions (Faster Payments), and (4) sign-off consistency ("Best regards / Thank you, The Oxen Team"). Config changes go in `templates/config/<template>/{en,fr}.json`; HTML changes go in `templates/content/<template>-content.html`.

**Tech Stack:** JSON config files + Handlebars-style `{{variable}}` HTML templates. No build step — changes are direct file edits.

---

## File Map

**Modified configs (EN + FR):**

- `templates/config/card-blocked/{en,fr}.json`
- `templates/config/card-temporarily-disabled/{en,fr}.json`
- `templates/config/card-unblocked/{en,fr}.json`
- `templates/config/new-device-login/{en,fr}.json`
- `templates/config/password-updated/{en,fr}.json`
- `templates/config/kyb-process-started/{en,fr}.json`
- `templates/config/invite-kyc/{en,fr}.json`
- `templates/config/welcome-email/{en,fr}.json`
- `templates/config/monthly-statement-ready/{en,fr}.json`
- `templates/config/automatic-account-closure-final-remind/{en,fr}.json`
- `templates/config/expense-report/{en,fr}.json`
- `templates/config/subscription-account-suspend/{en,fr}.json`
- `templates/config/subscription-collection-remind-24-hours/{en,fr}.json`
- `templates/config/subscription-collection-remind-3-days/{en,fr}.json`
- `templates/config/subscription-invoice/{en,fr}.json`

**Modified HTML content files:**

- `templates/content/kyb-process-started-content.html`
- `templates/content/invite-kyc-content.html`
- `templates/content/monthly-statement-ready-content.html`
- `templates/content/automatic-account-closure-final-remind-content.html`
- `templates/content/subscription-account-suspend-content.html`
- `templates/content/subscription-collection-remind-24-hours-content.html`
- `templates/content/subscription-collection-remind-3-days-content.html`
- `templates/content/subscription-invoice-content.html`

---

## Task 1: Security Contact Redirection — Card Templates

Update `security_warning` / `security_message` to say "account manager" instead of "support", and rename "The Security Team" to "The Oxen Security Team" across card-blocked, card-temporarily-disabled, card-unblocked.

**Files:**

- Modify: `templates/config/card-blocked/en.json`
- Modify: `templates/config/card-blocked/fr.json`
- Modify: `templates/config/card-temporarily-disabled/en.json`
- Modify: `templates/config/card-temporarily-disabled/fr.json`
- Modify: `templates/config/card-unblocked/en.json`
- Modify: `templates/config/card-unblocked/fr.json`

- [x] **Step 1: Update `card-blocked/en.json`**

Replace the file with:

```json
{
  "layout": "oxen-layout",
  "title": "Your card has been blocked - Oxen",
  "subject": "🔒 Card blocked",
  "card_info_prefix": "The card ending in",
  "card_info_suffix": "has been blocked via the Oxen app.",
  "security_signature": "The Oxen Security Team.",
  "security_warning": "👉 If you didn't initiate this action, please contact your account manager immediately.",
  "card_last_four": "1234",
  "first_name": "",
  "recipient_email": ""
}
```

- [x] **Step 2: Update `card-blocked/fr.json`**

Replace the file with:

```json
{
  "layout": "oxen-layout",
  "title": "Votre carte a été bloquée - Oxen",
  "subject": "🔒 Carte bloquée",
  "card_info_prefix": "La carte terminant par",
  "card_info_suffix": "a été bloquée depuis l'application Oxen.",
  "security_signature": "L'équipe Sécurité Oxen.",
  "security_warning": "👉 Si vous n'êtes pas à l'origine de cette action, contactez votre chargé de compte immédiatement.",
  "card_last_four": "1234",
  "first_name": "",
  "recipient_email": ""
}
```

- [x] **Step 3: Update `card-temporarily-disabled/en.json`**

Replace the file with:

```json
{
  "layout": "oxen-layout",
  "title": "🔒 We temporarily disabled your card for security reasons",
  "subject": "🔒 We temporarily disabled your card for security reasons",
  "card_disabled_message": "Due to suspicious activity, your card has been disabled.",
  "security_message": "👉 Contact your account manager to reactivate it.",
  "signature": "The Oxen Team.",
  "first_name": "",
  "recipient_email": ""
}
```

- [x] **Step 4: Update `card-temporarily-disabled/fr.json`**

Replace the file with:

```json
{
  "layout": "oxen-layout",
  "title": "🔒 Nous avons temporairement désactivé votre carte pour des raisons de sécurité",
  "subject": "🔒 Nous avons temporairement désactivé votre carte pour des raisons de sécurité",
  "card_disabled_message": "Suite à une activité suspecte, votre carte a été désactivée.",
  "security_message": "👉 Contactez votre chargé de compte pour la réactiver.",
  "signature": "L'équipe Oxen.",
  "first_name": "",
  "recipient_email": ""
}
```

- [x] **Step 5: Update `card-unblocked/en.json`**

Replace the file with:

```json
{
  "layout": "oxen-layout",
  "title": "Card unblocked - Oxen",
  "subject": "🔒 Card unblocked",
  "card_info_prefix": "The card ending in",
  "card_info_suffix": "has been unblocked via the Oxen app.",
  "security_signature": "The Oxen Security Team.",
  "security_warning": "👉 If you didn't initiate this action, please contact your account manager immediately.",
  "card_last_four": "4827",
  "first_name": "",
  "recipient_email": ""
}
```

- [x] **Step 6: Update `card-unblocked/fr.json`**

Replace the file with:

```json
{
  "layout": "oxen-layout",
  "title": "Carte débloquée - Oxen",
  "subject": "🔒 Carte débloquée",
  "card_info_prefix": "La carte terminant par",
  "card_info_suffix": "a été débloquée depuis l'application Oxen.",
  "security_signature": "L'équipe Sécurité Oxen.",
  "security_warning": "👉 Si vous n'êtes pas à l'origine de cette action, contactez votre chargé de compte immédiatement.",
  "card_last_four": "4827",
  "first_name": "",
  "recipient_email": ""
}
```

---

## Task 2: Security Contact Redirection — Login & Password Templates

Update `security_warning` / `security_message` to "account manager" and rename "The Security Team" → "The Oxen Security Team".

**Files:**

- Modify: `templates/config/new-device-login/en.json`
- Modify: `templates/config/new-device-login/fr.json`
- Modify: `templates/config/password-updated/en.json`
- Modify: `templates/config/password-updated/fr.json`

- [x] **Step 1: Update `new-device-login/en.json`**

Replace the file with:

```json
{
  "layout": "oxen-layout",
  "title": "New device login detected - Oxen",
  "subject": "📱 New device login detected",
  "device_label": "Device:",
  "device_name": "MacBook Air",
  "location_label": "Location:",
  "new_device_intro": "Your account was accessed from a new device:",
  "security_warning": "If this wasn't you please contact your account manager immediately.",
  "signature": "The Oxen Team.",
  "time_label": "Time:",
  "first_name": "",
  "location": "Lyon, France",
  "time": "10:21 (UTC+2)",
  "recipient_email": ""
}
```

- [x] **Step 2: Update `new-device-login/fr.json`**

Replace the file with:

```json
{
  "layout": "oxen-layout",
  "title": "Nouvelle connexion depuis un appareil inconnu - Oxen",
  "subject": "📱 Nouvelle connexion depuis un appareil inconnu",
  "device_label": "Appareil :",
  "device_name": "MacBook Air",
  "location_label": "Lieu :",
  "new_device_intro": "Votre compte a été utilisé sur un nouvel appareil :",
  "security_warning": "Si ce n'était pas vous, contactez votre chargé de compte immédiatement.",
  "signature": "L'équipe Oxen.",
  "time_label": "Heure :",
  "first_name": "",
  "location": "Lyon, France",
  "time": "10:21 (UTC+2)",
  "recipient_email": ""
}
```

- [x] **Step 3: Update `password-updated/en.json`**

Replace the file with:

```json
{
  "layout": "oxen-layout",
  "title": "Password / PIN successfully updated",
  "subject": "Password / PIN successfully updated",
  "password_updated_message": "Your password/PIN has been successfully updated.",
  "security_message": "👉 If you didn't make this change, please contact your account manager immediately.",
  "signature": "The Oxen Security Team.",
  "first_name": "",
  "recipient_email": ""
}
```

- [x] **Step 4: Update `password-updated/fr.json`**

Replace the file with:

```json
{
  "layout": "oxen-layout",
  "title": "Mot de passe / Code PIN mis à jour avec succès",
  "subject": "Mot de passe / Code PIN mis à jour avec succès",
  "password_updated_message": "Votre mot de passe/PIN a été mis à jour avec succès.",
  "security_message": "👉 Si vous n'avez pas effectué cette modification, veuillez contacter votre chargé de compte immédiatement.",
  "signature": "L'équipe Sécurité Oxen.",
  "first_name": "",
  "recipient_email": ""
}
```

---

## Task 3: Compliance Team — KYB Tracking & KYC Invitation

Update signature to "The Oxen Compliance Team" and add "Thank you" sign-off with signature block in HTML for KYB Tracking and KYC Invitation.

**Files:**

- Modify: `templates/config/kyb-process-started/en.json`
- Modify: `templates/config/kyb-process-started/fr.json`
- Modify: `templates/content/kyb-process-started-content.html`
- Modify: `templates/config/invite-kyc/en.json`
- Modify: `templates/config/invite-kyc/fr.json`
- Modify: `templates/content/invite-kyc-content.html`

- [x] **Step 1: Update `kyb-process-started/en.json`**

Replace the file with:

```json
{
  "layout": "oxen-layout",
  "title": "🎬 Start of the company verification process - Oxen",
  "subject": "🎬 Start of the company verification process",
  "cta_text": "Access KYB tracking",
  "kyb_started_message": "The verification process (KYB) for your company has just started. Please update the required documents from your Oxen Business interface.",
  "signature": "The Oxen Compliance Team.",
  "tracking_message": "You can track progress at any time in your company space.",
  "cta_url": "",
  "first_name": "",
  "recipient_email": ""
}
```

- [x] **Step 2: Update `kyb-process-started/fr.json`**

Replace the file with:

```json
{
  "layout": "oxen-layout",
  "title": "Démarrage du processus de vérification de votre entreprise - Oxen",
  "subject": "🎬 Démarrage du processus de vérification de votre entreprise",
  "cta_text": "Accéder au suivi KYB",
  "kyb_started_message": "Le processus de vérification (KYB) de votre entreprise vient de démarrer. Merci de mettre à jour les documents requis depuis votre interface Oxen Business.",
  "signature": "L'équipe Conformité Oxen.",
  "tracking_message": "Vous pouvez suivre l'avancement à tout moment dans votre espace entreprise.",
  "cta_url": "",
  "first_name": "",
  "recipient_email": ""
}
```

- [x] **Step 3: Add signature block to `kyb-process-started-content.html`**

Append after the closing CTA `</tr>` block (after line 108):

```html
<!-- Signature -->
<tr>
  <td style="padding: 20px 40px 20px 40px" class="mobile-padding">
    <table
      role="presentation"
      cellspacing="0"
      cellpadding="0"
      border="0"
      width="100%"
    >
      <tr>
        <td align="center">
          <p
            style="
              margin: 0;
              font-family: 'DM Sans', Arial, sans-serif;
              font-size: 18px;
              font-weight: 500;
              line-height: 24px;
              color: #F5F0EB;
              text-align: center;
            "
            class="body-text"
          >
            Thank you,<br />
            {{signature}}
          </p>
        </td>
      </tr>
    </table>
  </td>
</tr>
```

- [x] **Step 4: Update `invite-kyc/en.json`**

Replace the file with:

```json
{
  "layout": "oxen-layout",
  "title": "KYC Invitation - Oxen",
  "subject": "KYC Invitation",
  "greeting": "Hello",
  "kyc_invitation_message": "You have been invited to complete the KYC process. This verification ensures secure access to our services.",
  "cta_text": "👉 Start KYC Verification",
  "signature": "The Oxen Compliance Team.",
  "cta_url": "",
  "first_name": "",
  "recipient_email": ""
}
```

- [x] **Step 5: Update `invite-kyc/fr.json`**

Replace the file with:

```json
{
  "layout": "oxen-layout",
  "title": "Invitation KYC - Oxen",
  "subject": "Invitation KYC",
  "greeting": "Bonjour",
  "kyc_invitation_message": "Vous êtes invité(e) à compléter la procédure KYC. Cette vérification garantit un accès sécurisé à nos services.",
  "cta_text": "👉 Commencer la vérification KYC",
  "signature": "L'équipe Conformité Oxen.",
  "cta_url": "",
  "first_name": "",
  "recipient_email": ""
}
```

- [x] **Step 6: Add thank you + signature block to `invite-kyc-content.html`**

Append after the closing CTA `</tr>` block (after line 83):

```html
<!-- Thank you and Signature -->
<tr>
  <td style="padding: 20px 40px 20px 40px" class="mobile-padding">
    <table
      role="presentation"
      cellspacing="0"
      cellpadding="0"
      border="0"
      width="100%"
    >
      <tr>
        <td align="center">
          <p
            style="
              margin: 0;
              font-family: 'DM Sans', Arial, sans-serif;
              font-size: 18px;
              font-weight: 500;
              line-height: 24px;
              color: #F5F0EB;
              text-align: center;
            "
            class="body-text"
          >
            Thank you,<br />
            {{signature}}
          </p>
        </td>
      </tr>
    </table>
  </td>
</tr>
```

---

## Task 4: Welcome Email — Add Faster Payments to Getting Started

**Files:**

- Modify: `templates/config/welcome-email/en.json`
- Modify: `templates/config/welcome-email/fr.json`

- [x] **Step 1: Update `list_item_1` in `welcome-email/en.json`**

Change:

```
"list_item_1": "Send and receive payments via SEPA Instant and SWIFT",
```

To:

```
"list_item_1": "Send and receive payments via SEPA Instant, Faster Payments and SWIFT",
```

- [x] **Step 2: Update `list_item_1` in `welcome-email/fr.json`**

Change:

```
"list_item_1": "Envoyez et recevez des paiements via SEPA Instant et SWIFT",
```

To:

```
"list_item_1": "Envoyez et recevez des paiements via SEPA Instant, Faster Payments et SWIFT",
```

---

## Task 5: Sign-off Consistency — Config-only Updates

Update signature fields in templates whose HTML content files already render `{{signature}}` (with or without "Best regards" prefix).

**Files:**

- Modify: `templates/config/monthly-statement-ready/en.json`
- Modify: `templates/config/monthly-statement-ready/fr.json`
- Modify: `templates/config/automatic-account-closure-final-remind/en.json`
- Modify: `templates/config/automatic-account-closure-final-remind/fr.json`
- Modify: `templates/config/expense-report/en.json`
- Modify: `templates/config/expense-report/fr.json`
- Modify: `templates/content/monthly-statement-ready-content.html`
- Modify: `templates/content/automatic-account-closure-final-remind-content.html`

**Context on the HTML files:**

- `monthly-statement-ready-content.html` renders `{{signature}}` alone → update HTML to prefix "Best regards,"
- `automatic-account-closure-final-remind-content.html` renders `{{signature}}` alone → update HTML to prefix "Thank you,"
- `expense-report-content.html` already hardcodes "Best regards,<br>{{signature}}" → only config change needed

- [x] **Step 1: Update `monthly-statement-ready/en.json`**

Change `signature` value:

```json
"signature": "The Oxen Team."
```

(No change needed — HTML will be updated in Step 3 to add the "Best regards," prefix.)

- [x] **Step 2: Update `monthly-statement-ready/fr.json`**

Read the file to confirm `signature` value, then leave `signature` as is (HTML handles prefix).

Check: `templates/config/monthly-statement-ready/fr.json` — if `signature` field is missing, add:

```json
"signature": "L'équipe Oxen."
```

- [x] **Step 3: Update `monthly-statement-ready-content.html` — add "Best regards," prefix**

In the Signature section (around line 96–126), replace:

```html
<p
  style="
              margin: 0;
              font-family: 'DM Sans', Arial, sans-serif;
              font-size: 18px;
              font-weight: 500;
              line-height: 24px;
              color: #F5F0EB;
              text-align: center;
            "
  class="body-text"
>
  {{signature}}
</p>
```

With:

```html
<p
  style="
              margin: 0;
              font-family: 'DM Sans', Arial, sans-serif;
              font-size: 18px;
              font-weight: 500;
              line-height: 24px;
              color: #F5F0EB;
              text-align: center;
            "
  class="body-text"
>
  Best regards,<br />
  {{signature}}
</p>
```

- [x] **Step 4: Update `automatic-account-closure-final-remind/en.json`**

Change `signature` value to include "Thank you,":

```json
"signature": "The Oxen Team."
```

(The "Thank you," prefix is added in the HTML — see Step 6.)

- [x] **Step 5: Update `automatic-account-closure-final-remind/fr.json`**

`signature` stays as `"L'équipe Oxen."` — HTML will add the "Merci," prefix.

- [x] **Step 6: Update `automatic-account-closure-final-remind-content.html` — add "Thank you," prefix**

In the Signature section (around line 99–129), replace:

```html
<p
  style="
              margin: 0;
              font-family: 'DM Sans', Arial, sans-serif;
              font-size: 18px;
              font-weight: 500;
              line-height: 22px;
              color: #F5F0EB;
              text-align: center;
            "
  class="body-text"
>
  {{signature}}
</p>
```

With:

```html
<p
  style="
              margin: 0;
              font-family: 'DM Sans', Arial, sans-serif;
              font-size: 18px;
              font-weight: 500;
              line-height: 22px;
              color: #F5F0EB;
              text-align: center;
            "
  class="body-text"
>
  Thank you,<br />
  {{signature}}
</p>
```

- [x] **Step 7: Update `expense-report/en.json`** — remove emoji from signature

Change:

```json
"signature": "The Oxen Team 🌱"
```

To:

```json
"signature": "The Oxen Team."
```

- [x] **Step 8: Update `expense-report/fr.json`** — remove emoji from signature

Change:

```json
"signature": "L'équipe Oxen 🌱"
```

To:

```json
"signature": "L'équipe Oxen."
```

---

## Task 6: Sign-off Consistency — Templates Needing New Signature HTML Block

These templates have no `{{signature}}` in their content HTML. Add a signature block to each HTML file and add `signature` to the config.

**Files:**

- Modify: `templates/config/subscription-account-suspend/en.json`
- Modify: `templates/config/subscription-account-suspend/fr.json`
- Modify: `templates/content/subscription-account-suspend-content.html`
- Modify: `templates/config/subscription-collection-remind-24-hours/en.json`
- Modify: `templates/config/subscription-collection-remind-24-hours/fr.json`
- Modify: `templates/content/subscription-collection-remind-24-hours-content.html`
- Modify: `templates/config/subscription-collection-remind-3-days/en.json`
- Modify: `templates/config/subscription-collection-remind-3-days/fr.json`
- Modify: `templates/content/subscription-collection-remind-3-days-content.html`
- Modify: `templates/config/subscription-invoice/en.json`
- Modify: `templates/config/subscription-invoice/fr.json`
- Modify: `templates/content/subscription-invoice-content.html`

**Reusable signature HTML block** (append after last content `</tr>` in each HTML file):

```html
<!-- Signature -->
<tr>
  <td style="padding: 20px 40px 20px 40px" class="mobile-padding">
    <table
      role="presentation"
      cellspacing="0"
      cellpadding="0"
      border="0"
      width="100%"
    >
      <tr>
        <td align="center">
          <p
            style="
              margin: 0;
              font-family: 'DM Sans', Arial, sans-serif;
              font-size: 18px;
              font-weight: 500;
              line-height: 24px;
              color: #F5F0EB;
              text-align: center;
            "
            class="body-text"
          >
            Best regards,<br />
            {{signature}}
          </p>
        </td>
      </tr>
    </table>
  </td>
</tr>
```

- [x] **Step 1: Add `signature` to `subscription-account-suspend/en.json`**

Add field after `"cta_url": ""`:

```json
"signature": "The Oxen Team."
```

Full updated file:

```json
{
  "layout": "oxen-layout",
  "title": "Plan suspended: Update your balance now 🚫",
  "subject": "Plan suspended: Update your balance now 🚫",
  "suspension_message": "Your Oxen subscription has been overdue, and your account has now been suspended.",
  "warning_section": "🔴 Without payment, you will permanently lose access to your account.",
  "action_notice": "💡 To restore access, update your balance now!",
  "cta_text": "👉 Update My Balance",
  "cta_url": "",
  "signature": "The Oxen Team.",
  "first_name": "",
  "recipient_email": ""
}
```

- [x] **Step 2: Add `signature` to `subscription-account-suspend/fr.json`**

Full updated file:

```json
{
  "layout": "oxen-layout",
  "title": "Abonnement suspendu : mettez à jour votre solde 🚫",
  "subject": "Abonnement suspendu : mettez à jour votre solde 🚫",
  "suspension_message": "Votre abonnement Oxen est en retard de paiement et votre compte a été suspendu.",
  "warning_section": "🔴 Sans paiement, vous perdrez définitivement l'accès à votre compte.",
  "action_notice": "💡 Pour rétablir l'accès, mettez à jour votre solde dès maintenant !",
  "cta_text": "👉 Mettre à jour mon solde",
  "cta_url": "",
  "signature": "L'équipe Oxen.",
  "first_name": "",
  "recipient_email": ""
}
```

- [x] **Step 3: Append signature block to `subscription-account-suspend-content.html`**

Append the reusable signature HTML block (shown above) after the closing CTA `</tr>` at line 129.

- [x] **Step 4: Add `signature` to `subscription-collection-remind-24-hours/en.json`**

Full updated file:

```json
{
  "layout": "oxen-layout",
  "title": "Your Oxen plan renews tomorrow – Check your balance!",
  "subject": "Your Oxen plan renews tomorrow – Check your balance!",
  "renewal_message": "Your Oxen subscription renews tomorrow! 🚀",
  "instruction": "Ensure your account is funded to keep enjoying all your benefits.",
  "renewal_notice": "📅 Renewal tomorrow",
  "action_item": "💡 Avoid any disruption, check your balance now.",
  "cta_text": "👉 Access your account",
  "cta_url": "",
  "signature": "The Oxen Team.",
  "first_name": "",
  "recipient_email": ""
}
```

- [x] **Step 5: Add `signature` to `subscription-collection-remind-24-hours/fr.json`**

Full updated file:

```json
{
  "layout": "oxen-layout",
  "title": "Votre abonnement Oxen est renouvelé demain – Vérifiez votre solde !",
  "subject": "Votre abonnement Oxen est renouvelé demain – Vérifiez votre solde !",
  "renewal_message": "Votre abonnement Oxen sera renouvelé demain ! 🚀",
  "instruction": "Assurez-vous que votre compte est suffisamment approvisionné pour continuer à profiter de tous vos avantages.",
  "renewal_notice": "📅 Renouvellement demain",
  "action_item": "💡 Évitez toute interruption, vérifiez votre solde maintenant.",
  "cta_text": "👉 Accédez à votre compte",
  "cta_url": "",
  "signature": "L'équipe Oxen.",
  "first_name": "",
  "recipient_email": ""
}
```

- [x] **Step 6: Append signature block to `subscription-collection-remind-24-hours-content.html`**

Append the reusable signature HTML block after the closing CTA `</tr>` at line 125.

- [x] **Step 7: Add `signature` to `subscription-collection-remind-3-days/en.json`**

Full updated file:

```json
{
  "layout": "oxen-layout",
  "title": "Only 3 days left before your Oxen plan renewal ⏳",
  "subject": "Only 3 days left before your Oxen plan renewal ⏳",
  "renewal_message": "Your Oxen subscription is renewing soon! 🌍",
  "instruction": "Make sure you have sufficient funds in your account to keep enjoying all your benefits.",
  "renewal_notice": "📅 Renewal in 3 days",
  "action_item": "💡 Check your balance now to avoid any disruption.",
  "cta_text": "👉 Access your account",
  "cta_url": "",
  "signature": "The Oxen Team.",
  "first_name": "",
  "recipient_email": ""
}
```

- [x] **Step 8: Add `signature` to `subscription-collection-remind-3-days/fr.json`**

Read `templates/config/subscription-collection-remind-3-days/fr.json`, then add `"signature": "L'équipe Oxen."` field.

- [x] **Step 9: Append signature block to `subscription-collection-remind-3-days-content.html`**

Read `templates/content/subscription-collection-remind-3-days-content.html` to confirm structure (same pattern as 24-hours version), then append the reusable signature HTML block after the last CTA `</tr>`.

- [x] **Step 10: Add `signature` to `subscription-invoice/en.json`**

Full updated file (note: `support_message` is already updated to mention account manager in this config):

```json
{
  "layout": "oxen-layout",
  "title": "Subscription Invoice - Oxen",
  "subject": "🧾 Your subscription invoice #{{invoice_number}} is ready",
  "greeting": "Hello",
  "message": "Your subscription invoice is ready for download. Here are the details:",
  "label_invoice_number": "Invoice Number:",
  "label_invoice_date": "Invoice Date:",
  "label_due_date": "Due Date:",
  "label_amount": "Amount:",
  "label_status": "Status:",
  "cta_text": "🧾 View Invoice",
  "expiration_message_prefix": "This link will expire on",
  "expiration_message_suffix": "(1 hour from now).",
  "expiration_note": "* All times are in UTC",
  "support_message": "For any request or assistance, you can contact your account manager directly or use:",
  "support_email": "support@oxen.finance",
  "footer_note": "This email was sent because you requested a subscription invoice download that took longer than 5 seconds to process.",
  "signature": "The Oxen Team.",
  "customer_name": "John Doe",
  "invoice_number": "INV-2025-12-001",
  "invoice_date": "December 26, 2025",
  "due_date": "January 26, 2026",
  "invoice_amount": "€99.00",
  "invoice_currency": "EUR",
  "invoice_status": "Paid",
  "download_url": "",
  "expiration_time": "December 26, 2025 14:30 UTC",
  "expiration_hours": "1"
}
```

- [x] **Step 11: Add `signature` to `subscription-invoice/fr.json`**

Read the file and add `"signature": "L'équipe Oxen."` field.

- [x] **Step 12: Append signature block to `subscription-invoice-content.html`**

Append the reusable signature HTML block after the Support Contact section closing `</tr>` (end of file, after line 299).

---

## Final Verification

- [x] **Verify all config files have correct values** by running a search for "our support" and "The Security Team" and "The Compliance Team" to confirm none remain:

```bash
grep -r "our support\|The Security Team\b\|The Compliance Team\b" templates/config/
```

Expected: no output

- [x] **Verify all signature blocks are present** in the updated HTML content files:

```bash
grep -l "{{signature}}" templates/content/
```

Expected: includes kyb-process-started, invite-kyc, subscription-account-suspend, subscription-collection-remind-24-hours, subscription-collection-remind-3-days, subscription-invoice alongside the existing ones.

- [x] **Verify Faster Payments addition** in welcome-email configs:

```bash
grep "Faster Payments" templates/config/welcome-email/en.json templates/config/welcome-email/fr.json
```

Expected: both files match

- [x] **Commit all changes**:

```bash
git add templates/config/ templates/content/ TEMPLATES_TABLE_CONFLUENCE.html
git commit -m "feat: apply client notification sheet updates - contact redirection, branding, sign-off consistency"
```

---

## Task 7: Update TEMPLATES_TABLE_CONFLUENCE.html

Add a "Recent Updates" changelog section to the confluence reference document so that developers and integration teams know what content/config changed and why.

**Files:**

- Modify: `TEMPLATES_TABLE_CONFLUENCE.html`

No dynamic fields changed in this update cycle — all changes are static config values. The confluence table rows themselves stay the same. The update appends a changelog section at the end of the file.

- [x] **Step 1: Append changelog section to `TEMPLATES_TABLE_CONFLUENCE.html`**

Append at the very end of the file (after the closing `</ul>` of the "Date/Time Fields" section):

```html
<h2>Update Log</h2>

<h3>2026-04-16 — Notification Sheet Client Feedback Updates</h3>

<p>
  The following changes were applied based on client feedback from the updated
  notification sheet:
</p>

<h4>1. Contact Redirection — "Support" → "Account Manager"</h4>
<p>
  Security warning messages updated to direct users to their
  <strong>account manager</strong> instead of generic support:
</p>
<ul>
  <li><code>card-blocked</code> — <code>security_warning</code></li>
  <li>
    <code>card-temporarily-disabled</code> — <code>security_message</code>
  </li>
  <li><code>card-unblocked</code> — <code>security_warning</code></li>
  <li><code>new-device-login</code> — <code>security_warning</code></li>
  <li><code>password-updated</code> — <code>security_message</code></li>
</ul>

<h4>2. Team Name Branding</h4>
<ul>
  <li>
    <strong>Security Team</strong>: "The Security Team" → "The Oxen Security
    Team" in <code>card-blocked</code>, <code>card-unblocked</code>,
    <code>password-updated</code>
  </li>
  <li>
    <strong>Compliance Team</strong>: Signature updated to "The Oxen Compliance
    Team" in <code>kyb-process-started</code>, <code>invite-kyc</code>
  </li>
</ul>

<h4>3. Content Additions</h4>
<ul>
  <li>
    <code>welcome-email</code> — "Getting Started" list now includes
    <strong>Faster Payments</strong> alongside SEPA Instant and SWIFT
  </li>
  <li>
    <code>kyb-process-started</code> — Added formal "Thank you, The Oxen
    Compliance Team" sign-off (config + HTML)
  </li>
  <li>
    <code>invite-kyc</code> — Added formal "Thank you, The Oxen Compliance Team"
    sign-off (config + HTML)
  </li>
</ul>

<h4>4. Sign-off Consistency</h4>
<p>
  Standardized sign-offs to "Best regards / Thank you, The Oxen Team" across
  subscription and statement templates:
</p>
<ul>
  <li>
    <code>monthly-statement-ready</code> — Added "Best regards," prefix in HTML
  </li>
  <li>
    <code>automatic-account-closure-final-remind</code> — Added "Thank you,"
    prefix in HTML
  </li>
  <li><code>expense-report</code> — Removed 🌱 emoji from signature</li>
  <li>
    <code>subscription-account-suspend</code> — Added signature field + HTML
    sign-off block
  </li>
  <li>
    <code>subscription-collection-remind-24-hours</code> — Added signature field
    + HTML sign-off block
  </li>
  <li>
    <code>subscription-collection-remind-3-days</code> — Added signature field +
    HTML sign-off block
  </li>
  <li>
    <code>subscription-invoice</code> — Added signature field + HTML sign-off
    block
  </li>
</ul>

<p>
  <em
    >Note: All changes above are static config values. No new server-provided
    dynamic fields were introduced.</em
  >
</p>
```
