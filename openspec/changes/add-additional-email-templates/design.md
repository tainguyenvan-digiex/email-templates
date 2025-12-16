# Design: Additional Email Templates

## Architecture Decision

All new email templates will follow the established pattern:

- **Layout**: Use `shared-layout.html` (already supports header gradient, greeting, social media, footer, unsubscribe)
- **Content**: Create content-only files in `content/` directory
- **Configuration**: Create JSON config files in `templates/config/<template-name>/` with en.json and fr.json
- **Structure**: Follow the same variable organization (layout variables at top, dynamic content at bottom with blank line separator)

## Template Categories

### 1. Team Management Templates

- **team-invitation**: Simple invitation with CTA button
- **team-member-removed**: Informational notification with optional user details

### 2. Subscription Management Templates

- **subscription-updated**: Shows previous/new plan comparison with effective date

### 3. Security Alert Templates

- **unusual-login**: Shows IP address, location, time with security warning
- **new-device-login**: Shows device name, location, time
- **failed-login-attempts**: Shows number of attempts and email address

### 4. Receipt Management Templates

- **receipt-reminder**: Single expense reminder with amount and merchant
- **receipt-final-reminder**: Final reminder with CTA button
- **missing-receipts-summary**: List of multiple expenses without receipts

### 5. System Notification Templates

- **maintenance-extended**: Shows new ETA for maintenance completion
- **technical-incident**: Generic incident notification

### 6. Compliance & Legal Templates

- **terms-updated**: Terms update notification with CTA button
- **update-personal-info**: Request to update identity/address documents
- **kyb-process-started**: KYB verification process started notification

### 7. Account Summary Templates

- **monthly-summary**: Monthly account summary with statistics and CTA
- **monthly-statement-ready**: Monthly statement available for download

### 8. Compliance & Verification Templates (Additional)

- **company-verified**: Company verification completed successfully
- **document-resubmit-required**: Document validation failed, resubmission required
- **id-update-required**: ID document expired or missing

### 9. Card Management Templates (Additional)

- **card-temporarily-disabled**: Card disabled for security reasons
- **card-shipping**: Card shipping notification with tracking

### 10. Payment & Transfer Templates (Additional)

- **payment-confirmed**: Payment transaction confirmed
- **transfer-sent**: Transfer sent confirmation
- **payment-approval-pending**: Payment awaiting approval (simple)
- **payment-approval-required**: Payment approval required with details

### 11. Account Lifecycle Templates

- **account-opened**: Account opened notification
- **account-closed**: Account closed confirmation
- **account-opening-incomplete**: Reminder to complete account opening

### 12. Account Manager Appointment Templates

- **call-confirmed**: Appointment confirmed with details
- **call-rescheduled**: Appointment rescheduled with new details
- **call-cancelled**: Appointment cancelled notification
- **call-reminder**: Appointment reminder (1 hour before)

### 13. User Preference Templates

- **password-updated**: Password/PIN updated confirmation
- **preferences-updated**: Notification/preference settings updated
- **unsubscribed**: Unsubscribed confirmation

## Content Structure Patterns

### Simple Notification Pattern

Used by: team-invitation, team-member-removed, failed-login-attempts, receipt-reminder, company-verified, account-closed, password-updated, preferences-updated, unsubscribed, payment-confirmed, transfer-sent, card-shipping

- Intro message
- Key information (highlighted)
- Action message with CTA (optional)
- Signature

### Detail List Pattern

Used by: subscription-updated, unusual-login, new-device-login

- Intro message
- Multiple detail lines (label: value format, values bolded)
- Action message
- Signature

### Summary List Pattern

Used by: missing-receipts-summary, monthly-summary

- Intro message
- Bulleted or formatted list of items
- CTA button/link
- Signature

### CTA-Heavy Pattern

Used by: receipt-final-reminder, terms-updated, kyb-process-started, document-resubmit-required, id-update-required, monthly-statement-ready, account-opening-incomplete, payment-approval-pending, payment-approval-required

- Intro message
- Key information
- Prominent CTA button
- Additional instructions
- Signature

### Detail List with CTA Pattern

Used by: payment-approval-required, call-confirmed, call-rescheduled

- Intro message
- Multiple detail lines (label: value format, values bolded)
- Prominent CTA button
- Additional instructions
- Signature

### Appointment Details Pattern

Used by: call-confirmed, call-rescheduled, call-reminder

- Intro message
- Appointment details (date, time, location/link) with emoji icons
- Instructions or CTA
- Signature

## Variable Naming Conventions

- Use descriptive, template-specific variable names
- Follow existing patterns (e.g., `card_info_prefix`, `card_info_suffix`)
- For lists: use `item_1`, `item_2` or `expense_1_name`, `expense_1_amount`
- For CTAs: use `cta_text` and `cta_url`
- For dates: use descriptive names like `effective_date`, `expense_date`

## Configuration File Structure

All config files follow this structure:

```json
{
  // Layout variables (top section)
  "lang_code": "...",
  "header_gradient": "...",
  "primary_color": "...",
  "title": "...",
  "preheader": "...",
  "heading": "...",
  "subject": "...", // Same as heading
  "greeting": "...",
  // ... footer variables ...

  // Blank line separator

  // Dynamic content variables (bottom section)
  "template_specific_var_1": "...",
  "template_specific_var_2": "..."
}
```

## Email Client Compatibility

All templates must:

- Use table-based layouts for complex structures
- Include inline styles
- Support Outlook (Word rendering engine)
- Be responsive (mobile-friendly)
- Include proper alt text for images
- Use web-safe fonts (Poppins with fallbacks)

## Accessibility Considerations

- Proper heading hierarchy
- Alt text for all images
- Sufficient color contrast
- Clear call-to-action buttons
- Readable font sizes (minimum 14px for body text)
