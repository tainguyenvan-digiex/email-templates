# Change: Add Subscription and Compliance Email Templates

## Why

The email template system needs 12 new templates to support subscription lifecycle management and compliance workflows. These templates cover critical user communications including:
- Subscription renewal reminders (7 days, 3 days, 24 hours before renewal)
- Payment failure and account suspension warnings
- Account closure notifications
- Compliance request status updates (approved, rejected, additional information needed)

These templates are essential for maintaining user engagement, ensuring payment collection, and managing compliance processes effectively.

## What Changes

- **Add 9 subscription-related email templates** covering the full subscription lifecycle from renewal reminders to account closure
- **Add 3 compliance-related email templates** for request approval/rejection workflows
- All templates support English and French languages via configuration files
- Templates follow the existing shared layout pattern (header, content, footer)
- Configuration files follow the established structure with layout variables at top and dynamic content variables at bottom
- All templates use the brand name "Oxen" (replacing "Green Nation" references)
- All templates use `{{first_name}}` variable (replacing companyName_Value)

### New Templates:

**Subscription Management (9 templates):**
1. `subscription-collection-remind-7-days` - 7-day renewal reminder
2. `subscription-collection-remind-3-days` - 3-day renewal reminder
3. `subscription-collection-remind-24-hours` - 24-hour renewal reminder
4. `subscription-payment-failed-warning-block` - Payment failure warning with defer period
5. `subscription-account-suspend` - Account suspension notification
6. `automatic-account-closure-15-day-left` - 15-day closure warning
7. `automatic-account-closure-final-remind` - Final closure warning
8. `gn-b2b-account-closed-confirmation` - Account closure confirmation
9. (Note: Template #9 is missing from the list, only 8 subscription templates provided)

**Compliance Management (3 templates):**
10. `compliance-request-approved` - Compliance request approval
11. `compliance-request-rejected` - Compliance request rejection with reason
12. `compliance-request-need-additional-information` - Request for additional documents

## Impact

- Affected specs: `specs/email-templates/spec.md`
- Affected code:
  - New config files: `templates/config/[template-name]/en.json` and `fr.json` for each template (24 files total)
  - New HTML template files: `templates/[template-name].html` for each template (12 files total, if following existing pattern)
  - Alternatively, templates may use shared layout with content-only files in `content/` directory
- No breaking changes to existing templates
- Extends existing email template system without modifications to current templates
