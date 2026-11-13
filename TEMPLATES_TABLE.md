# Email Templates Reference Table

This document lists all email templates with their aliases, mappings to the database, and dynamic fields that need to be provided from the server.

## Template List

| # | Template Name | Alias | CSV Mapping | Dynamic Fields (Server-Provided) |
|---|--------------|-------|-------------|-----------------------------------|
| 1 | Account Closed | `account-closed` | `gn-b2b-account-closed-confirmation-en/fr` | `first_name` |
| 2 | Account Opened | `account-opened` | `gn-b2b-account-opened-confirmation-en/fr` | `first_name`, `iban`, `bic`, `account_number`, `sort_code`, `bank_name`, `bank_address`, `currency`, `addressable_in` — sent with the Account Confirmation Letter PDF attached |
| 3 | Account Opening Incomplete | `account-opening-incomplete` | `gn-b2b-onboarding-incomplete-en/fr` | `first_name` |
| 4 | Call Cancelled | `call-cancelled` | `gn-b2b-call-cancelled-en/fr` | `first_name` |
| 5 | Call Confirmed | `call-confirmed` | `gn-b2b-call-booked-en/fr` | `first_name`, `appointment_date`, `appointment_time`, `location` |
| 6 | Call Reminder | `call-reminder` | `gn-b2b-call-reminder-1h-en/fr` | `first_name`, `date`, `time`, `meeting_link` |
| 7 | Call Rescheduled | `call-rescheduled` | `gn-b2b-call-rescheduled-en/fr` | `first_name`, `date`, `time`, `meeting_link` |
| 8 | Card Blocked | `card-blocked` | `gn-b2b-card-blocked-en/fr` | `first_name`, `card_last_four` |
| 9 | Card Deleted | `card-deleted` | `gn-b2b-card-deleted-en/fr` | `first_name`, `card_last_four` |
| 10 | Card Shipping | `card-shipping` | ❌ Not in DB | `first_name` |
| 11 | Card Temporarily Disabled | `card-temporarily-disabled` | ❌ Not in DB | `first_name` |
| 12 | Card Unblocked | `card-unblocked` | ❌ Not in DB | `first_name`, `card_last_four` |
| 13 | Company Verified | `company-verified` | `gn-b2b-onboarding-kyb-validated-en/fr` | `first_name`, `company_name`, `cta_url` |
| 14 | Document Resubmit Required | `document-resubmit-required` | `gn-b2b-onboarding-document-rejected-en/fr` | `first_name`, `reason`, `cta_url` |
| 15 | Failed Login Attempts | `failed-login-attempts` | `gn-b2b-auth-multiple-failed-login-attempts-en/fr` | `first_name` |
| 16 | High Spending | `high-spending` | `gn-b2b-card-high-spending-en/fr` | `first_name`, `amount`, `card_last_four`, `location` |
| 17 | ID Update Required | `id-update-required` | `gn-b2b-onboarding-expired-or-missing-document-en/fr` | `first_name`, `cta_url` |
| 18 | KYB Process Started | `kyb-process-started` | `gn-b2b-onboarding-started-kyb-process-en/fr` | `first_name` |
| 19 | Maintenance Extended | `maintenance-extended` | ❌ Not in DB | `first_name`, `eta` |
| 20 | Missing Receipts Summary | `missing-receipts-summary` | `gn-b2b-receipt-weekly-summary-report-en/fr` | `first_name`, `start_date`, `end_date`, `expenses` (array) |
| 21 | Monthly Statement Ready | `monthly-statement-ready` | `gn-b2b-account-monthly-statement-en/fr` | `first_name`, `month_year`, `cta_url` |
| 22 | Monthly Summary | `monthly-summary` | `gn-b2b-account-monthly-activity-summary-en/fr` | `first_name`, `month_year`, `cta_url` |
| 23 | New Device Login | `new-device-login` | `gn-b2b-auth-first-login-en/fr` | `first_name`, `location`, `time` |
| 24 | Password Updated | `password-updated` | `gn-b2b-account-password-pin-changed-en/fr` | `first_name` |
| 25 | Payment Approval Pending | `payment-approval-pending` | `gn-b2b-transfer-pending-approval-en/fr` | `first_name`, `amount`, `cta_url` |
| 26 | Payment Approval Required | `payment-approval-required` | ❌ Not in DB | `first_name`, `amount`, `initiated_by`, `beneficiary`, `iban`, `heading`, `subject` |
| 27 | Payment Confirmed | `payment-confirmed` | ❌ Not in DB | `first_name`, `amount`, `merchant`, `heading`, `subject` |
| 28 | Preferences Updated | `preferences-updated` | `gn-b2b-account-preferences-updated-en/fr` | `first_name` |
| 29 | Receipt Final Reminder | `receipt-final-reminder` | `gn-b2b-receipt-missing-72h-en/fr` | `first_name`, `cta_url` |
| 30 | Receipt Reminder | `receipt-reminder` | `gn-b2b-receipt-missing-24h-en/fr` | `first_name`, `amount`, `merchant` |
| 31 | Subscription Updated | `subscription-updated` | `gn-b2b-account-subscription-plan-changed-en/fr` | `first_name`, `effective_date`, `previous_plan`, `new_plan` |
| 32 | Team Invitation | `team-invitation` | `gn-b2b-account-invitation-sent-en/fr` | `first_name`, `cta_url` |
| 33 | Team Member Removed | `team-member-removed` | ❌ Not in DB | `first_name`, `removed_user_info`, `company_name` |
| 34 | Technical Incident | `technical-incident` | ❌ Not in DB | `first_name` |
| 35 | Terms Updated | `terms-updated` | ❌ Not in DB | `first_name`, `update_date`, `cta_url` |
| 36 | Transfer Alert | `transfer-alert` | ❌ Not in DB | `first_name`, `account_name`, `amount` |
| 37 | Transfer Failed | `transfer-failed` | `gn-b2b-transfer-failed-en/fr` | `first_name`, `amount`, `failure_reason`, `transaction_type` |
| 38 | Transfer Sent | `transfer-sent` | ❌ Not in DB | `first_name`, `amount`, `recipient_name`, `heading`, `subject` |
| 39 | Unsubscribed | `unsubscribed` | `gn-b2b-account-newsletter-unsubscription-en/fr` | `first_name` |
| 40 | Unusual Login | `unusual-login` | `gn-b2b-auth-suspicious-login-attempt-en/fr` | `first_name`, `ip_address`, `location`, `time` |
| 41 | Update Personal Info | `update-personal-info` | `gn-b2b-onboarding-legal-compliance-requirement-en/fr` | `first_name`, `cta_url` |
| 42 | Welcome (B2B) | `welcome` (b2b.json) | ❌ Not in DB | `first_name`, `book_call_url`, `faq_url` |
| 43 | Welcome (B2C) | `welcome` (b2c.json) | ❌ Not in DB | `first_name`, `book_call_url`, `faq_url` |
| 44 | Expense Report | `expense-report` | `gn-b2b-expense-report-ready-en/fr` | `first_name`, `date_from`, `date_to`, `cta_url` |
| 45 | Revenue Export (KPI, fiat/crypto) | `revenue-export` | ❌ Not in DB | `revenue_label` (`fiat` or `crypto`), `date_from`, `date_to`, `download_url`, `expiration_minutes` |
| 46 | Visa Cards Live (announcement) | `visa-cards-live` | ❌ Not in DB | `first_name`, `cta_url` (portal Cards page, e.g. `https://portal-stg.oxen.finance/cards`; used by both CTA buttons) |
| 47 | Access Created (M02) | `access-created` | ❌ Not in DB | `first_name`, `company_name`, `role_name`, `cta_url` (portal login URL) |
| 48 | Access Removed (M03) | `access-removed` | ❌ Not in DB | `first_name`, `company_name`, `date` (UTC) |
| 49 | Card Activated (K01) | `card-activated` | ❌ Not in DB (card-service, OP-1312) | `first_name`, `last4`, `cardholder_name` |
| 50 | Virtual Card Created (K02) | `card-virtual-created` | ❌ Not in DB (card-service, OP-1312) | `first_name`, `last4`, `cardholder_name` |
| 51 | Card Ordered (K03) | `card-ordered` | ❌ Not in DB (card-service, OP-1312) | `first_name`, `cardholder_name`, `delivery_line` (full sentence, empty hides it) |
| 52 | Card Blocked Permanently (K04) | `card-blocked-permanently` | ❌ Not in DB (card-service, OP-1312) | `first_name`, `last4`, `blocked_by` (person's name or `Oxen`) |
| 53 | Card Frozen (K07) | `card-frozen` | ❌ Not in DB (card-service, OP-1312) | `first_name`, `last4` |
| 54 | Card Unfrozen (K07) | `card-unfrozen` | ❌ Not in DB (card-service, OP-1312) | `first_name`, `last4` |
| 55 | Card Payment Above Threshold (K08) | `card-payment-above-threshold` | ❌ Not in DB (card-service, OP-1312) | `first_name`, `last4`, `amount`, `merchant`, `location` |
| 56 | Card Payment Declined (K10) | `card-payment-declined` | ❌ Not in DB (card-service, OP-1312) | `first_name`, `amount`, `merchant`, `last4`, `decline_reason` (sentence from `mapDeclineReason`), `cta_url` |
| 57 | Card Payment Refunded (K11) | `card-payment-refunded` | ❌ Not in DB (card-service, OP-1312) | `first_name`, `amount`, `merchant`, `card_balance` |
| 58 | Card Top-up Returned (K14) | `card-topup-returned` | ❌ Not in DB (card-service, OP-1312) | `first_name`, `amount` |
| 59 | Card Top-up Refund Failed (K15) | `card-topup-refund-failed` | ❌ Not in DB (card-service, OP-1312) | `first_name`, `amount`, `topup_reference`, `cta_url` (empty → `mailto:support@oxen.finance`) |
| 60 | Card Withdrawal Completed (K17) | `card-withdrawal-completed` | ❌ Not in DB (card-service, OP-1312) | `first_name`, `amount`, `card_balance` |
| 61 | Card Balance Low (K18) | `card-balance-low` | ❌ Not in DB (card-service, OP-1312) | `first_name`, `card_balance`, `threshold` |
| 62 | Card Balance Used Up (K19) | `card-balance-used-up` | ❌ Not in DB (card-service, OP-1312) | `first_name`, `cta_url` |
| 63 | Card Limit Updated (K20) | `card-limit-updated` | ❌ Not in DB (card-service, OP-1312) | `first_name`, `last4`, `limit_amount`, `frequency_text` (`per day`/`per week`/`per month`/`per year`/`in total`/`per transaction`, from `limitFrequencyText`) |
| 64 | Card PIN Changed (K21) | `card-pin-changed` | ❌ Not in DB (card-service, OP-1312) | `first_name`, `last4` |
| 65 | Card Balance Ready (K22) | `card-balance-ready` | ❌ Not in DB (card-service, OP-1312) | `first_name`, `company_name` |
| 66 | Card Statement Ready (K23) | `card-statement-ready` | ❌ Not in DB (card-service, OP-1312) | `first_name`, `period`, `download_url`, `expiration_text` (words, e.g. `1 hour`) |
| 67 | Card Statement Failed (K24) | `card-statement-failed` | ❌ Not in DB (card-service, OP-1312) | `first_name`, `period_from`, `period_to` (both empty = single-transaction receipt failure) |
| 68 | Card Receipt Ready (K25) | `card-receipt-ready` | ❌ Not in DB (card-service, OP-1312) | `first_name`, `transaction_amount`, `transaction_date`, `download_url`, `expiration_text` (words, e.g. `1 hour`) |
| 69 | Card Payment Code, 3DS (K27) | `card-payment-code` | ❌ Not in DB (card-service, OP-1312) | `first_name`, `last4`, `merchant`, `amount`, `otp_code`, `otp_minutes` |
| 70 | [internal] Rain webhook, no hash match | `card-dev-rain-no-hash` | ❌ Not in DB (card-service, OP-1312) | `transaction_hash`, `company_id`, `card_account_id`, `amount`, `reason`, `hide_contact_block: true` |
| 71 | [internal] Rain compliance alert | `card-rain-compliance-alert` | ❌ Not in DB (card-service, OP-1312) | `company_id`, `event_code`, `rain_status`, `reason_codes`, `step`, `reason_text`, `owner`, `hold_source`, `cleared_by_admin`, `admin_url`; run: `companies` (list of `{company_id, reason_codes, admin_url}`), `company_count`; `hide_contact_block: true` |
| 72 | [internal] PIN lockouts over the limit | `auth-pin-disabled-alert` | ❌ Not in DB (gn-auth-service, OP-1368) | `subject` (built by the sender, e.g. `[STG] 7 PIN lockouts in 60 minutes`), `env`, `count`, `threshold`, `window_minutes`, `window_start` (`dd MMM yyyy, HH:mm UTC`), `user_ids` (array of up to 20 user ids), `more_users` (`""` when none: the "and N more" line hides), `recipient_email`; `hide_contact_block: true` |
| 73 | [internal] Phone trust expiries over the limit | `auth-trust-expired-alert` | ❌ Not in DB (gn-auth-service, OP-1368) | `subject` (built by the sender, e.g. `[STG] 7 PIN lockouts in 60 minutes`), `env`, `count`, `threshold`, `window_minutes`, `window_start` (`dd MMM yyyy, HH:mm UTC`), `user_ids` (array of up to 20 user ids), `more_users` (`""` when none: the "and N more" line hides), `recipient_email`; `hide_contact_block: true` |
| 74 | [internal] Phones removed from the web over the limit | `auth-device-removed-alert` | ❌ Not in DB (gn-auth-service, OP-1368) | `subject` (built by the sender, e.g. `[STG] 7 PIN lockouts in 60 minutes`), `env`, `count`, `threshold`, `window_minutes`, `window_start` (`dd MMM yyyy, HH:mm UTC`), `user_ids` (array of up to 20 user ids), `more_users` (`""` when none: the "and N more" line hides), `recipient_email`; `hide_contact_block: true` |
| 75 | [internal] Phones replaced over the limit | `auth-device-replaced-alert` | ❌ Not in DB (gn-auth-service, OP-1368) | `subject` (built by the sender, e.g. `[STG] 7 PIN lockouts in 60 minutes`), `env`, `count`, `threshold`, `window_minutes`, `window_start` (`dd MMM yyyy, HH:mm UTC`), `user_ids` (array of up to 20 user ids), `more_users` (`""` when none: the "and N more" line hides), `recipient_email`; `hide_contact_block: true` |
| 76 | [internal] Trust ended on all devices | `auth-trust-epoch-bumped-alert` | ❌ Not in DB (gn-auth-service, OP-1368) | `subject` (built by the sender), `env`, `epoch_before`, `epoch_after`, `requested_by`, `approved_by` (admin user ids), `approved_at` (`dd MMM yyyy, HH:mm UTC`), `recipient_email`; `hide_contact_block: true` |
| 77 | [internal] Face ID approvals by one user over the limit | `auth-face-id-approval-burst-alert` | ❌ Not in DB (gn-auth-service, OP-1368) | `subject` and `title` (same value, built by the sender, e.g. `[STG] 11 Face ID approvals by one user in 60 minutes`), `env`, `user_id`, `count`, `threshold`, `window_minutes`, `window_start` (`dd MMM yyyy, HH:mm UTC`), `action_types` (array of distinct actionType values), `approval_ids` (array of up to 20, newest last), `more_approvals` (`""` when none: the "and N more" line hides), `recipient_email`; `hide_contact_block: true` |
| 78 | [internal] Large Face ID payment to a new payee from a new phone | `auth-face-id-large-new-payee-alert` | ❌ Not in DB (gn-auth-service, OP-1368) | `subject` and `title` (same value, built by the sender), `env`, `user_id`, `company_id`, `approval_id`, `action_type`, `amount_eur` (e.g. `12500.00`), `threshold_eur`, `payee_added_at`, `device_trusted_at`, `approved_at` (times `dd MMM yyyy, HH:mm UTC`), `recipient_email`; `hide_contact_block: true` |
| 79 | Crypto Withdrawal to a New Address (X05) | `crypto-withdrawal-new-address` | crypto `withdrawal_new_address` → be-b2b `crypto.withdrawal_new_address` | `first_name`, `initiator_name`, `amount`, `symbol`, `network`, `address`, `date` (UTC; the template adds "UTC"), `cta_url` ("View the withdrawal"), `devices_url` (OP-1367, `{CLIENT_PORTAL_URL}/settings`; the "Not you? Review my devices" line hides while empty) |
| 80 | Payee Added (A1) | `beneficiary-added-alert` | ❌ Not in DB (be-b2b `beneficiary.added_alert`, OP-1367) | `first_name`, `payee_name`, `account_masked` (last 4 only, `•••• 1234`; empty for a green contact, another Oxen client with no IBAN: the Account row hides), `initiator_name`, `approval_status` (optional: be-b2b sends the translated "Pending approval" while the change awaits approval; the Status row hides when empty), `date` (`dd MMM yyyy, HH:mm`, UTC; the template adds "UTC"), `cta_url` (`{CLIENT_PORTAL_URL}/settings`, button "Review my devices"); subject/title use `payee_name` |
| 81 | Payee Details Changed (A2) | `beneficiary-edited-alert` | ❌ Not in DB (be-b2b `beneficiary.edited_alert`, OP-1367) | `first_name`, `payee_name`, `account_masked` (last 4 only, `•••• 1234`; empty for a green contact, another Oxen client with no IBAN: the Account row hides), `initiator_name`, `approval_status` (optional: be-b2b sends the translated "Pending approval" while the change awaits approval; the Status row hides when empty), `date` (`dd MMM yyyy, HH:mm`, UTC; the template adds "UTC"), `cta_url` (`{CLIENT_PORTAL_URL}/settings`, button "Review my devices"); subject/title use `payee_name` |
| 82 | First Payment to a Payee (A3) | `beneficiary-first-payment-alert` | ❌ Not in DB (be-b2b `beneficiary.first_payment_alert`, OP-1367) | `first_name`, `payee_name`, `account_masked` (last 4 only, `•••• 1234`; empty for a green contact, another Oxen client with no IBAN: the Account row hides), `amount` (decimal string), `symbol` (ISO currency), `initiator_name`, `date` (`dd MMM yyyy, HH:mm`, UTC; the template adds "UTC"), `cta_url` (`{CLIENT_PORTAL_URL}/settings`, button "Review my devices"); subject/title use `payee_name` |
| 83 | Crypto Address Added (A4) | `crypto-address-added-alert` | ❌ Not in DB (crypto `address_added_alert` → be-b2b `crypto.address_added_alert`, OP-1367) | `first_name`, `address_label`, `address_short` (first 6 + last 4), `network`, `symbol` (optional, row hides when empty), `initiator_name`, `approval_status` (optional: be-b2b sends the translated "Pending approval" while the change awaits approval; the Status row hides when empty), `date` (`dd MMM yyyy, HH:mm`, UTC; the template adds "UTC"), `cta_url` (`{CLIENT_PORTAL_URL}/settings`, button "Review my devices"); subject/title use `address_label` |
| 84 | Crypto Address Changed (A5) | `crypto-address-edited-alert` | ❌ Not in DB (crypto `address_edited_alert` → be-b2b `crypto.address_edited_alert`, OP-1367) | `first_name`, `address_label`, `address_short` (first 6 + last 4), `network`, `symbol` (optional, row hides when empty), `initiator_name`, `approval_status` (optional: be-b2b sends the translated "Pending approval" while the change awaits approval; the Status row hides when empty), `date` (`dd MMM yyyy, HH:mm`, UTC; the template adds "UTC"), `cta_url` (`{CLIENT_PORTAL_URL}/settings`, button "Review my devices"); subject/title use `address_label` |

## Common Dynamic Fields

Most templates require these common fields:
- `first_name` - User's first name

**Note:** Unsubscribe links are handled automatically by Postmark using `{{{ pm:unsubscribe }}}` variable.

## Field Notes

### Dynamic Headings/Subjects
Some templates have dynamic `heading` and `subject` fields that are provided by the server:
- **Payment Confirmed**: `heading` and `subject` contain `{{amount}}` and `{{merchant}}`
- **Transfer Sent**: `heading` and `subject` contain `{{amount}}` and `{{recipient_name}}`
- **Payment Approval Required**: `heading` and `subject` contain `{{amount}}`

### CTA URLs
Templates with CTA buttons require `cta_url`:
- Document Resubmit Required
- ID Update Required
- Payment Approval Pending
- Receipt Reminder
- Receipt Final Reminder
- Team Invitation
- Terms Updated
- Update Personal Info
- Welcome (B2B/B2C)
- Expense Report

### Date/Time Fields
Call-related templates use different date/time field names:
- **Call Confirmed**: `appointment_date`, `appointment_time`, `location`
- **Call Reminder**: `date`, `time`, `meeting_link`
- **Call Rescheduled**: `date`, `time`, `meeting_link`

## CSV Mapping Notes

- Templates marked with ❌ Not in DB are not yet registered in the database
- Templates with CSV mappings use the format: `gn-b2b-{alias}-en` and `gn-b2b-{alias}-fr`
- Some CSV aliases differ slightly from template aliases (e.g., `account-opened` vs `account-opened-confirmation`)
