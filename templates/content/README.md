# Content Files for Postmark Templates

This directory contains content-only files designed to be used with Postmark layouts.

## Overview

Content files contain only template-specific sections and are inserted into Postmark layouts via the `{{{ @content }}}` placeholder. They do not include the document shell, shared styles, footer, or unsubscribe section — all of which are provided by the layout.

## Usage with Postmark

1. Upload the layout (`layouts/common-layout.html`) to Postmark as a Layout
2. Create a new template in Postmark
3. Select the layout from the Layout dropdown
4. Copy and paste the content file HTML into the template editor
5. Postmark will automatically combine the content with the layout

## Files

| File                                                          | Description                                     |
| ------------------------------------------------------------- | ----------------------------------------------- |
| `account-closed-content.html`                                 | Account closure confirmation                    |
| `account-opened-content.html`                                 | Account successfully opened                     |
| `account-opening-incomplete-content.html`                     | Incomplete account opening reminder             |
| `approve-kyb-content.html`                                    | KYB approval notification                       |
| `automatic-account-closure-15-day-left-content.html`          | 15-day warning before automatic account closure |
| `automatic-account-closure-final-remind-content.html`         | Final reminder before automatic account closure |
| `balance-statement-content.html`                              | Balance statement                               |
| `call-cancelled-content.html`                                 | Scheduled call cancellation                     |
| `call-confirmed-content.html`                                 | Scheduled call confirmation                     |
| `call-reminder-content.html`                                  | Upcoming call reminder                          |
| `call-rescheduled-content.html`                               | Call rescheduled notification                   |
| `card-blocked-content.html`                                   | Card blocked notification                       |
| `card-deleted-content.html`                                   | Card deleted confirmation                       |
| `card-shipping-content.html`                                  | Card shipping notification                      |
| `card-temporarily-disabled-content.html`                      | Card temporarily disabled notification          |
| `card-unblocked-content.html`                                 | Card unblocked notification                     |
| `company-verified-content.html`                               | Company verification approved                   |
| `compliance-request-approved-content.html`                    | Compliance request approved                     |
| `compliance-request-need-additional-information-content.html` | Compliance request needs additional information |
| `compliance-request-rejected-content.html`                    | Compliance request rejected                     |
| `crypto-transaction-statement-content.html`                   | Crypto transaction statement                    |
| `document-resubmit-required-content.html`                     | Document resubmission required                  |
| `expense-report-content.html`                                 | Expense report notification                     |
| `failed-login-attempts-content.html`                          | Failed login attempts alert                     |
| `gn-b2b-account-closed-confirmation-content.html`             | B2B account closure confirmation                |
| `high-spending-content.html`                                  | High spending alert                             |
| `id-update-required-content.html`                             | ID update required notification                 |
| `invite-admin-content.html`                                   | Admin invitation                                |
| `invite-director-access-content.html`                         | Director access invitation                      |
| `invite-kyc-content.html`                                     | KYC invitation                                  |
| `invite-member-access-content.html`                           | Member access invitation                        |
| `kyb-process-started-content.html`                            | KYB process started notification                |
| `maintenance-extended-content.html`                           | Maintenance extended notification               |
| `missing-receipts-summary-content.html`                       | Missing receipts summary                        |
| `monthly-statement-ready-content.html`                        | Monthly statement ready                         |
| `monthly-summary-content.html`                                | Monthly summary                                 |
| `new-device-login-content.html`                               | New device login alert                          |
| `password-updated-content.html`                               | Password updated confirmation                   |
| `payment-approval-pending-content.html`                       | Payment approval pending notification           |
| `payment-approval-required-content.html`                      | Payment approval required notification          |
| `payment-confirmed-content.html`                              | Payment confirmed notification                  |
| `payment-sent-content.html`                                   | Payment sent confirmation                       |
| `preferences-updated-content.html`                            | Preferences updated confirmation                |
| `receipt-final-reminder-content.html`                         | Final receipt upload reminder                   |
| `receipt-reminder-content.html`                               | Receipt upload reminder                         |
| `rib-document-content.html`                                   | RIB document notification                       |
| `statement-single-transaction-content.html`                   | Single transaction statement                    |
| `statement-transactions-by-period-content.html`               | Transactions by period statement                |
| `subscription-account-suspend-content.html`                   | Subscription account suspension                 |
| `subscription-collection-remind-24-hours-content.html`        | Subscription collection reminder (24 hours)     |
| `subscription-collection-remind-3-days-content.html`          | Subscription collection reminder (3 days)       |
| `subscription-collection-remind-7-days-content.html`          | Subscription collection reminder (7 days)       |
| `subscription-invoice-content.html`                           | Subscription invoice                            |
| `subscription-payment-failed-warning-block-content.html`      | Subscription payment failed warning             |
| `subscription-payment-success-content.html`                   | Subscription payment success                    |
| `subscription-updated-content.html`                           | Subscription updated confirmation               |
| `team-invitation-content.html`                                | Team member invitation                          |
| `team-member-removed-content.html`                            | Team member removed notification                |
| `technical-incident-content.html`                             | Technical incident notification                 |
| `terms-updated-content.html`                                  | Terms and conditions updated                    |
| `transaction-reconciliation-alert-content.html`               | Transaction reconciliation alert                |
| `transfer-alert-content.html`                                 | Transfer alert                                  |
| `transfer-failed-content.html`                                | Transfer failed notification                    |
| `transfer-sent-content.html`                                  | Transfer sent confirmation                      |
| `unsubscribed-content.html`                                   | Unsubscribe confirmation                        |
| `unusual-login-content.html`                                  | Unusual login alert                             |
| `update-personal-info-content.html`                           | Personal info update confirmation               |
| `verify-email-content.html`                                   | Email verification                              |
| `welcome-content.html`                                        | Welcome email                                   |
| `welcome-content.lapkipay.html`                               | Welcome email (Lapkipay variant)                |
| `welcome-email-content.html`                                  | Welcome email (Postmark variant)                |
