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
| 8 | Card Shipping | `card-shipping` | ❌ Not in DB | `first_name` |
| 9 | Card Temporarily Disabled | `card-temporarily-disabled` | ❌ Not in DB | `first_name` |
| 10 | Company Verified | `company-verified` | `gn-b2b-onboarding-kyb-validated-en/fr` | `first_name`, `company_name`, `cta_url` |
| 11 | Document Resubmit Required | `document-resubmit-required` | `gn-b2b-onboarding-document-rejected-en/fr` | `first_name`, `reason`, `cta_url` |
| 12 | Failed Login Attempts | `failed-login-attempts` | `gn-b2b-auth-multiple-failed-login-attempts-en/fr` | `first_name` |
| 13 | High Spending | `high-spending` | `gn-b2b-card-high-spending-en/fr` | `first_name`, `amount`, `card_last_four`, `location` |
| 14 | ID Update Required | `id-update-required` | `gn-b2b-onboarding-expired-or-missing-document-en/fr` | `first_name`, `cta_url` |
| 15 | KYB Process Started | `kyb-process-started` | `gn-b2b-onboarding-started-kyb-process-en/fr` | `first_name` |
| 16 | Maintenance Extended | `maintenance-extended` | ❌ Not in DB | `first_name`, `eta` |
| 17 | Missing Receipts Summary | `missing-receipts-summary` | `gn-b2b-receipt-weekly-summary-report-en/fr` | `first_name`, `start_date`, `end_date`, `expenses` (array) |
| 18 | Monthly Statement Ready | `monthly-statement-ready` | `gn-b2b-account-monthly-statement-en/fr` | `first_name`, `month_year`, `cta_url` |
| 19 | Monthly Summary | `monthly-summary` | `gn-b2b-account-monthly-activity-summary-en/fr` | `first_name`, `month_year`, `cta_url` |
| 20 | New Device Login | `new-device-login` | `gn-b2b-auth-first-login-en/fr` | `first_name`, `location`, `time` |
| 21 | Password Updated | `password-updated` | `gn-b2b-account-password-pin-changed-en/fr` | `first_name` |
| 22 | Payment Approval Pending | `payment-approval-pending` | `gn-b2b-transfer-pending-approval-en/fr` | `first_name`, `amount`, `cta_url` |
| 23 | Payment Approval Required | `payment-approval-required` | ❌ Not in DB | `first_name`, `amount`, `initiated_by`, `beneficiary`, `iban`, `heading`, `subject` |
| 24 | Payment Confirmed | `payment-confirmed` | ❌ Not in DB | `first_name`, `amount`, `merchant`, `heading`, `subject` |
| 25 | Preferences Updated | `preferences-updated` | `gn-b2b-account-preferences-updated-en/fr` | `first_name` |
| 26 | Receipt Final Reminder | `receipt-final-reminder` | `gn-b2b-receipt-missing-72h-en/fr` | `first_name`, `cta_url` |
| 27 | Receipt Reminder | `receipt-reminder` | `gn-b2b-receipt-missing-24h-en/fr` | `first_name`, `amount`, `merchant` |
| 28 | Subscription Updated | `subscription-updated` | `gn-b2b-account-subscription-plan-changed-en/fr` | `first_name`, `effective_date`, `previous_plan`, `new_plan` |
| 29 | Team Invitation | `team-invitation` | `gn-b2b-account-invitation-sent-en/fr` | `first_name`, `cta_url` |
| 30 | Team Member Removed | `team-member-removed` | ❌ Not in DB | `first_name`, `removed_user_info`, `company_name` |
| 31 | Technical Incident | `technical-incident` | ❌ Not in DB | `first_name` |
| 32 | Terms Updated | `terms-updated` | ❌ Not in DB | `first_name`, `update_date`, `cta_url` |
| 33 | Transfer Alert | `transfer-alert` | ❌ Not in DB | `first_name`, `account_name`, `amount` |
| 34 | Transfer Failed | `transfer-failed` | `gn-b2b-transfer-failed-en/fr` | `first_name`, `amount`, `failure_reason`, `transaction_type` |
| 35 | Transfer Sent | `transfer-sent` | ❌ Not in DB | `first_name`, `amount`, `recipient_name`, `heading`, `subject` |
| 36 | Unsubscribed | `unsubscribed` | `gn-b2b-account-newsletter-unsubscription-en/fr` | `first_name` |
| 37 | Unusual Login | `unusual-login` | `gn-b2b-auth-suspicious-login-attempt-en/fr` | `first_name`, `ip_address`, `location`, `time` |
| 38 | Update Personal Info | `update-personal-info` | `gn-b2b-onboarding-legal-compliance-requirement-en/fr` | `first_name`, `cta_url` |
| 39 | Welcome (B2B) | `welcome` (b2b.json) | ❌ Not in DB | `first_name`, `book_call_url`, `faq_url` |
| 40 | Welcome (B2C) | `welcome` (b2c.json) | ❌ Not in DB | `first_name`, `book_call_url`, `faq_url` |
| 41 | Expense Report | `expense-report` | `gn-b2b-expense-report-ready-en/fr` | `first_name`, `date_from`, `date_to`, `cta_url` |
| 42 | Revenue Export (KPI, fiat/crypto) | `revenue-export` | ❌ Not in DB | `revenue_label` (`fiat` or `crypto`), `date_from`, `date_to`, `download_url`, `expiration_minutes` |
| 43 | Visa Cards Live (announcement) | `visa-cards-live` | ❌ Not in DB | `first_name`, `cta_url` (portal Cards page, e.g. `https://portal-stg.oxen.finance/cards`; used by both CTA buttons) |

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
