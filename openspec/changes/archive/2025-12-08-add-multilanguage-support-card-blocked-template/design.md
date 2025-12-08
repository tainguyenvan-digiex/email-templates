# Design: Multi-Language Support for Card Blocked Email Template

## Context

The card blocked email template currently has all French text hardcoded. We need to support:
- **French (fr)**: Current language, all text already exists
- **English (en)**: New language, needs translation

All text content must be dynamic to support multiple languages while maintaining the same template structure.

## Goals / Non-Goals

### Goals

- Support French and English languages
- Make all user-facing text configurable per language
- Maintain single template file (no language-specific HTML files)
- Keep language files separate from variant configs (B2B/B2C, regions)
- Easy to add new languages in the future
- Language selection at email send time

### Non-Goals

- Automatic language detection (handled by email service)
- More than 2 languages initially (but structure should support expansion)
- Language-specific layouts or designs (same structure, different text)

## Decisions

### Decision 1: Separate Language Files

**What**: Create separate JSON files for each language (`fr.json`, `en.json`)
**Why**: 
- Clean separation of concerns
- Easy to add new languages
- Can be maintained by translators independently
- Reusable across all variants (B2B/B2C, regions)

**Structure**:
```
templates/config/card-blocked/
├── languages/
│   ├── fr.json
│   └── en.json
├── b2b-france.json (references language)
├── b2c-france.json
└── ...
```

### Decision 2: Language Content Schema

**What**: Each language file contains all translatable strings
**Why**: Single source of truth per language, easy to maintain

**Schema**:
```json
{
  "lang": "fr",
  "content": {
    "title": "Votre carte a été bloquée - Green Nation",
    "preheader": "⚠️ Votre carte Green Nation a été bloquée...",
    "heading": {
      "part1": "VOTRE",
      "part2": "CARTE A ÉTÉ BLOQUÉE,",
      "part3": "VÉRIFIEZ VOTRE COMPTE",
      "emoji": "🔔"
    },
    "greeting": "Bonjour",
    "card_info": {
      "prefix": "La carte terminant par",
      "suffix": "a été bloquée depuis l'application Green Nation."
    },
    "security": {
      "warning": "👉 Si vous n'êtes pas à l'origine de cette action, contactez notre support immédiatement.",
      "signature": "L'équipe Sécurité."
    },
    "social": {
      "title": "Ne passez pas à côté de notre actu !",
      "hashtags": "#CLEANTECH #ARGENT #PLANETE... ET SURTOUT... DES INFOS EXCLUSIVES!"
    },
    "footer": {
      "copyright": "© Green Nation 2025",
      "unsubscribe": {
        "sent_to": "Sent to:",
        "link_text": "Pour vous désinscrire, cliquez ici."
      }
    }
  }
}
```

### Decision 3: Template Variable Naming

**What**: Use `{{lang.key}}` pattern for language variables
**Why**: Clear namespace, easy to identify language content

**Examples**:
- `{{lang.title}}` - Page title
- `{{lang.greeting}}` - Greeting word
- `{{lang.card_info.prefix}}` - Card info prefix
- `{{lang.security.warning}}` - Security warning

### Decision 4: Language Selection in Config

**What**: Variant config files reference language file
**Why**: Each variant can specify its default language, but can be overridden at send time

**Example**:
```json
{
  "variant": "b2b-france",
  "language": "fr",
  "styling": {...},
  "content": {
    "company_address": "...",
    "company_registration": "...",
    "legal_text": "..."
  }
}
```

### Decision 5: Nested Content Structure

**What**: Use nested objects for related content (e.g., `card_info.prefix`, `card_info.suffix`)
**Why**: 
- Groups related translations
- Easier to maintain context
- Supports complex text structures

## Text Content to Translate

### Header Section
- Page title (`<title>` tag)
- Preheader text (hidden preview)
- Main heading (3 parts + emoji)

### Main Content
- Greeting word ("Bonjour" / "Hello")
- Card information prefix ("La carte terminant par" / "The card ending in")
- Card information suffix ("a été bloquée depuis..." / "has been blocked from...")
- Security warning message
- Security team signature

### Social Media Section
- Section title
- Hashtags text

### Footer Section
- Copyright text
- "Sent to:" label
- Unsubscribe link text
- Company name (if needed)

### Legal Text
- Company registration (already configurable, but needs language versions)
- Legal disclaimer (already configurable, but needs language versions)

## Language File Structure

Each language file (`fr.json`, `en.json`) contains:
- Language code (`lang`)
- All translatable strings organized by section
- Support for HTML in strings (for line breaks, emphasis)
- Support for placeholders (e.g., `{{first_name}}` in greeting)

## Integration with Existing System

- Language files work alongside existing variant configs
- Variant configs can specify default language
- Email service can override language at send time
- Template variables: `{{lang.*}}` for language content, `{{content.*}}` for variant-specific content (addresses, legal text)

## Risks / Trade-offs

### Risk: Template Complexity
**Risk**: Too many variables make template hard to read
**Mitigation**: Use clear naming (`lang.*` prefix), group related content

### Risk: Missing Translations
**Risk**: New content added but not translated
**Mitigation**: Validation script to check all language files have same keys

### Trade-off: Flat vs Nested Structure
**Trade-off**: Flat (`lang.title`) vs Nested (`lang.heading.part1`)
**Decision**: Nested for related content, flat for simple strings

## Migration Plan

1. **Phase 1**: Extract all French text to `fr.json`
2. **Phase 2**: Create `en.json` with English translations
3. **Phase 3**: Update template to use `{{lang.*}}` variables
4. **Phase 4**: Update all variant configs to reference language
5. **Phase 5**: Test both languages render correctly

## Open Questions

- Should legal text be in language files or variant configs? (Probably variant configs since they're region-specific)
- Do we need language-specific image alt text? (Yes, should be in language files)
- How to handle pluralization? (Keep simple for now, use full phrases)

