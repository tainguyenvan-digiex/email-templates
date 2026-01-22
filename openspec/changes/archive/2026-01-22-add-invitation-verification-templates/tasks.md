# Tasks

## Template: invite-director-access

- [x]Create `templates/config/invite-director-access/en.json` with English configuration including title, preheader, heading, subject, greeting, invitation message, CTA text, and all dynamic variables (`first_name`, `inviter_name`, `company_name`, `cta_url`)
- [x]Create `templates/config/invite-director-access/fr.json` with French configuration with all translations matching English structure
- [x]Create `content/invite-director-access-content.html` with template structure using common-layout pattern, including header with invitation message, main content area, and CTA button
- [x]Verify template renders correctly in English with test data
- [x]Verify template renders correctly in French with test data
- [x]Add invite-director-access to TEMPLATES_TABLE_CONFLUENCE.html documentation with CSV mapping `invite-director-access-en/fr` and dynamic fields list

## Template: invite-admin

- [x]Create `templates/config/invite-admin/en.json` with English configuration including title, preheader, heading, subject, greeting, admin invitation message, expiration notice (30 days hardcoded), CTA text, and all dynamic variables (`first_name`, `cta_url`)
- [x]Create `templates/config/invite-admin/fr.json` with French configuration with all translations matching English structure
- [x]Create `content/invite-admin-content.html` with template structure using common-layout pattern, including header with admin role specification, expiration notice, and CTA button
- [x]Verify template renders correctly in English with test data
- [x]Verify template renders correctly in French with test data
- [x]Add invite-admin to TEMPLATES_TABLE_CONFLUENCE.html documentation with CSV mapping `invite-admin-en/fr` and dynamic fields list

## Template: approve-kyb

- [x]Create `templates/config/approve-kyb/en.json` with English configuration including title, preheader, heading, subject, greeting, KYB approval request message, admin console instruction, CTA text, and all dynamic variables (`first_name`, `company_name`, `cta_url`)
- [x]Create `templates/config/approve-kyb/fr.json` with French configuration with all translations matching English structure
- [x]Create `content/approve-kyb-content.html` with template structure using common-layout pattern, including header with KYB request details, company name display, and admin console CTA button
- [x]Verify template renders correctly in English with test data
- [x]Verify template renders correctly in French with test data
- [x]Add approve-kyb to TEMPLATES_TABLE_CONFLUENCE.html documentation with CSV mapping `approve-kyb-en/fr` and dynamic fields list

## Template: invite-kyc

- [x]Create `templates/config/invite-kyc/en.json` with English configuration including title, preheader, heading, subject, KYC invitation message, verification purpose explanation, CTA text, and all dynamic variables (`first_name`, `cta_url`)
- [x]Create `templates/config/invite-kyc/fr.json` with French configuration with all translations matching English structure
- [x]Create `content/invite-kyc-content.html` with template structure using common-layout pattern, including header with KYC invitation, purpose explanation, and CTA button
- [x]Verify template renders correctly in English with test data
- [x]Verify template renders correctly in French with test data
- [x]Add invite-kyc to TEMPLATES_TABLE_CONFLUENCE.html documentation with CSV mapping `invite-kyc-en/fr` and dynamic fields list

## Template: verify-email

- [x]Create `templates/config/verify-email/en.json` with English configuration including title, preheader, heading, subject, verification instruction, OTP code label, validity notice (1 minute hardcoded), and all dynamic variables (`first_name`, `otp_code`)
- [x]Create `templates/config/verify-email/fr.json` with French configuration with all translations matching English structure
- [x]Create `content/verify-email-content.html` with template structure using common-layout pattern, including header, prominent OTP code display area (large, monospace font, high contrast), validity notice, and NO CTA button
- [x]Verify template renders correctly in English with test OTP code
- [x]Verify template renders correctly in French with test OTP code
- [x]Verify OTP code is displayed prominently with good readability (font size, spacing, contrast)
- [x]Add verify-email to TEMPLATES_TABLE_CONFLUENCE.html documentation with CSV mapping `verify-email-en/fr` and dynamic fields list

## Documentation Updates

- [x]Update TEMPLATES_TABLE_CONFLUENCE.html "CTA URLs" section to include new templates: invite-director-access, invite-admin, approve-kyb, invite-kyc (exclude verify-email as it uses OTP display, not CTA)
- [x]Verify all 5 new templates are properly documented with correct aliases, CSV mappings, and dynamic fields
- [x]Update Common Dynamic Fields section if new field types are introduced (e.g., `inviter_name`, `otp_code`)

## Validation

- [x]Test all 5 templates render correctly in both English and French
- [x]Verify all dynamic variables are properly replaced
- [x]Verify common layout integration works for all templates
- [x]Verify email client compatibility (Gmail, Outlook, Apple Mail)
- [x]Verify responsive design on mobile devices
- [x]Verify accessibility (alt text, color contrast, semantic HTML)
- [x]Run visual regression tests if available
