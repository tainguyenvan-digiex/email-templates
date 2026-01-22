# Change: Add Invitation and Verification Email Templates

## Why

The email template system needs 5 new templates to support user invitation workflows and email verification processes. These templates cover critical administrative and security communications including:
- Director and admin invitation flows
- KYB (Know Your Business) approval workflow for admins
- KYC (Know Your Customer) invitation for users
- Email verification with OTP codes

These templates are essential for onboarding team members, managing business verification processes, and securing user accounts through email verification.

## What Changes

- **Add 5 invitation and verification email templates** covering admin/director invitations, KYB/KYC workflows, and email verification
- All templates support English and French languages via configuration files
- Templates follow the existing shared layout pattern (common-layout.html)
- Configuration files follow the established structure with layout variables and dynamic content variables
- All templates use the brand name "Oxen"
- Templates use consistent variable naming (`first_name` for recipient names)

### New Templates:

**Invitation & Access Management (2 templates):**
1. `invite-director-access` - Invitation to join company's Business account as director
2. `invite-admin` - Invitation to join Oxen Platform as Admin

**KYB/KYC Workflows (2 templates):**
3. `approve-kyb` - KYB approval request notification for admins
4. `invite-kyc` - KYC process invitation for users

**Email Verification (1 template):**
5. `verify-email` - Email verification with OTP code

### Dynamic Variables by Template:

1. **invite-director-access**: `first_name`, `inviter_name`, `company_name`, `cta_url`
2. **invite-admin**: `first_name`, `cta_url`
3. **approve-kyb**: `first_name`, `company_name`, `cta_url`
4. **invite-kyc**: `first_name`, `cta_url`
5. **verify-email**: `first_name`, `otp_code`

## Impact

- Affected specs: `specs/email-templates/spec.md`
- Affected code:
  - New config files: `templates/config/[template-name]/en.json` and `fr.json` for each template (10 files total)
  - New content files: `content/[template-name]-content.html` for each template (5 files total)
- No breaking changes to existing templates
- Extends existing email template system without modifications to current templates
- All templates use common-layout.html for consistency
