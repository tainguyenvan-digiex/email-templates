# Change: Add Card Blocked Email Template

## Why
We need a transactional email template to notify users when their card has been blocked from the Green Nation application. This is a critical security notification that requires clear, professional presentation and proper email client compatibility.

## What Changes
- Add new HTML email template for card blocked notifications
- Template includes header with logo, main content area, social media section, and footer
- Supports personalization (first name, last 4 digits of card)
- Includes unsubscribe link and legal disclaimers
- Responsive design for mobile and desktop email clients

## Impact
- Affected specs: `email-templates` capability (new)
- Affected code: New template file `templates/card-blocked.html`
- Design source: Figma design at node-id 1-2189

