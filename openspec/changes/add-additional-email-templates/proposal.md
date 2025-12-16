# Proposal: Add Additional Email Templates

## Why

The current email template system supports a limited set of transactional emails (welcome, card-blocked, transfer-failed, transfer-alert, card-deleted, card-unblocked, high-spending). To support the full Green Nation Business platform functionality, we need to add 35 additional email templates covering:

1. Team management (invitations, member removal)
2. Subscription management (plan updates)
3. Security alerts (unusual login, failed login attempts, new device, password updates)
4. Receipt management (reminders, missing receipts)
5. System notifications (maintenance, technical incidents)
6. Compliance and legal (terms updates, personal information updates, KYB process, document resubmission, ID updates)
7. Account summaries (monthly summaries, missing receipts summary, monthly statements)
8. Account lifecycle (account opening incomplete, account closed, welcome B2C)
9. Card management (card shipping, card temporarily disabled)
10. Payment management (payment confirmed, transfer sent, payment approval pending/required)
11. Account Manager appointments (call confirmed, rescheduled, cancelled, reminder)
12. User preferences (preferences updated, unsubscribed)

These templates will follow the same architecture pattern as existing templates, using the shared-layout.html layout and JSON configuration files for multi-language support.

## What Changes

### New Content Files (35 templates)

- `content/team-invitation-content.html` - Team invitation email
- `content/subscription-updated-content.html` - Subscription plan update notification
- `content/unusual-login-content.html` - Security alert for unusual login attempts
- `content/team-member-removed-content.html` - Team member removal notification
- `content/new-device-login-content.html` - New device login detection
- `content/failed-login-attempts-content.html` - Multiple failed login attempts alert
- `content/receipt-reminder-content.html` - Receipt upload reminder
- `content/receipt-final-reminder-content.html` - Final reminder for missing receipt
- `content/missing-receipts-summary-content.html` - Weekly summary of missing receipts
- `content/maintenance-extended-content.html` - Extended maintenance notification
- `content/technical-incident-content.html` - Ongoing technical incident notification
- `content/terms-updated-content.html` - Terms of Service update notification
- `content/monthly-summary-content.html` - Monthly account summary
- `content/update-personal-info-content.html` - Personal information update request
- `content/kyb-process-started-content.html` - KYB verification process started
- `content/company-verified-content.html` - Company verification completed
- `content/document-resubmit-required-content.html` - Action required: resubmit document
- `content/id-update-required-content.html` - Time to update your ID
- `content/monthly-statement-ready-content.html` - Monthly statement ready
- `content/card-temporarily-disabled-content.html` - Card temporarily disabled for security
- `content/payment-approval-pending-content.html` - Payment awaits approval
- `content/welcome-b2c-content.html` - Welcome to Green Nation (B2C)
- `content/account-closed-content.html` - Account closed confirmation
- `content/password-updated-content.html` - Password/PIN updated confirmation
- `content/preferences-updated-content.html` - Preferences updated confirmation
- `content/unsubscribed-content.html` - Unsubscribed confirmation
- `content/payment-confirmed-content.html` - Payment confirmed notification
- `content/transfer-sent-content.html` - Transfer sent confirmation
- `content/card-shipping-content.html` - Card shipping notification
- `content/payment-approval-required-content.html` - Approval required: payment details
- `content/account-opening-incomplete-content.html` - Complete account opening reminder
- `content/call-confirmed-content.html` - Account Manager call confirmed
- `content/call-rescheduled-content.html` - Account Manager call rescheduled
- `content/call-cancelled-content.html` - Account Manager call cancelled
- `content/call-reminder-content.html` - Account Manager call reminder

### New Configuration Files (70 files - en.json and fr.json for each)

- `templates/config/team-invitation/` - en.json, fr.json
- `templates/config/subscription-updated/` - en.json, fr.json
- `templates/config/unusual-login/` - en.json, fr.json
- `templates/config/team-member-removed/` - en.json, fr.json
- `templates/config/new-device-login/` - en.json, fr.json
- `templates/config/failed-login-attempts/` - en.json, fr.json
- `templates/config/receipt-reminder/` - en.json, fr.json
- `templates/config/receipt-final-reminder/` - en.json, fr.json
- `templates/config/missing-receipts-summary/` - en.json, fr.json
- `templates/config/maintenance-extended/` - en.json, fr.json
- `templates/config/technical-incident/` - en.json, fr.json
- `templates/config/terms-updated/` - en.json, fr.json
- `templates/config/monthly-summary/` - en.json, fr.json
- `templates/config/update-personal-info/` - en.json, fr.json
- `templates/config/kyb-process-started/` - en.json, fr.json
- `templates/config/company-verified/` - en.json, fr.json
- `templates/config/document-resubmit-required/` - en.json, fr.json
- `templates/config/id-update-required/` - en.json, fr.json
- `templates/config/monthly-statement-ready/` - en.json, fr.json
- `templates/config/card-temporarily-disabled/` - en.json, fr.json
- `templates/config/payment-approval-pending/` - en.json, fr.json
- `templates/config/welcome-b2c/` - en.json, fr.json
- `templates/config/account-closed/` - en.json, fr.json
- `templates/config/password-updated/` - en.json, fr.json
- `templates/config/preferences-updated/` - en.json, fr.json
- `templates/config/unsubscribed/` - en.json, fr.json
- `templates/config/payment-confirmed/` - en.json, fr.json
- `templates/config/transfer-sent/` - en.json, fr.json
- `templates/config/card-shipping/` - en.json, fr.json
- `templates/config/payment-approval-required/` - en.json, fr.json
- `templates/config/account-opening-incomplete/` - en.json, fr.json
- `templates/config/call-confirmed/` - en.json, fr.json
- `templates/config/call-rescheduled/` - en.json, fr.json
- `templates/config/call-cancelled/` - en.json, fr.json
- `templates/config/call-reminder/` - en.json, fr.json

### No Changes To

- Existing templates remain unchanged
- `layouts/shared-layout.html` remains unchanged (all new templates will use it)
- Existing content files remain unchanged
- Existing configuration files remain unchanged

## Impact

- **Affected specs**: `email-templates`
- **New capabilities**: 35 new email template types
- **New files**: 35 content files + 70 configuration files = 105 new files
- **Backward compatibility**: All existing templates continue to work unchanged
- **Layout reuse**: All new templates use existing `shared-layout.html` layout

## Success Criteria

- All 35 templates render correctly in English and French
- All templates use the shared-layout.html layout
- All templates follow the same configuration pattern (layout variables at top, dynamic content at bottom)
- All templates include subject field matching heading
- All templates are responsive and email-client compatible
- All JSON configuration files are valid and follow the established structure
