# Content Files for Postmark Templates

This directory contains content-only files designed to be used with Postmark layouts.

## Overview

Content files contain only template-specific sections and are designed to be inserted into Postmark layouts via the `{{{ @content }}}` placeholder.

## Files

- **welcome-content.html**: Welcome email content (header, features, impact, support, assistance sections)
- **card-blocked-content.html**: Card blocked email content (header with card info, social media section)

## What's Included

Each content file contains:

- Template-specific HTML sections (header, body content)
- Template variables (e.g., `{{heading}}`, `{{first_name}}`)
- Inline styles for template-specific elements

## What's NOT Included

Content files do NOT include:

- Footer section (provided by layout)
- Unsubscribe section (provided by layout)
- CSS styles in `<head>` (provided by layout)
- HTML document structure (`<!DOCTYPE>`, `<html>`, `<head>`, `<body>` tags)

## Usage with Postmark

1. Upload the layout (`layouts/common-layout.html`) to Postmark as a Layout
2. Create a new template in Postmark
3. Select the layout from the Layout dropdown
4. Copy and paste the content file HTML into the template editor
5. Postmark will automatically combine the content with the layout

## Template Variables

Content files use template variables that are replaced when sending emails. These variables are documented in the configuration files (`templates/config/`).

## Original Templates

The original full templates remain in `templates/` directory:

- `templates/welcome.html` - Full welcome template (unchanged)
- `templates/card-blocked.html` - Full card-blocked template (unchanged)

These are preserved for backward compatibility and reference.
