# Change: Add Multi-Language Support to Card Blocked Template

## Why

The card blocked email template currently only supports French language with hardcoded text. We need to support multiple languages (French and English initially) to serve international users. All text content should be dynamic and configurable per language, allowing the same template structure to work across different languages.

## What Changes

- Add language configuration to the existing generic template system
- Extract all hardcoded French text to template variables
- Create language-specific content files (French and English)
- Update configuration schema to include language selection
- Make all user-facing text dynamic (title, headings, body text, buttons, legal text)
- Support language detection/selection per email send
- **BREAKING**: All text content becomes template variables (no hardcoded French)

## Impact

- Affected specs: `email-templates` capability (MODIFIED)
- Affected code:
  - `templates/card-blocked.html` → All text content becomes variables
  - New: `templates/config/card-blocked/languages/` directory:
    - `fr.json` (French translations)
    - `en.json` (English translations)
  - Updated: Configuration files to reference language files
  - New: Language variable system for all text content
- Affected content:
  - Page title, preheader text
  - Main heading ("VOTRE CARTE A ÉTÉ BLOQUÉE...")
  - Greeting ("Bonjour...")
  - Card information text
  - Security message
  - Social media section text
  - Footer text
  - Unsubscribe text
  - All legal disclaimers

