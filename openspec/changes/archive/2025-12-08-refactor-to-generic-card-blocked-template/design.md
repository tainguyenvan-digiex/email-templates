# Design: Generic Card Blocked Email Template System

## Context

We have 6 variants of the card blocked email template:

| Variant           | Segment  | Region        | Background      | Address               |
| ----------------- | -------- | ------------- | --------------- | --------------------- |
| B2B France        | Business | France        | Blue (#3651F3)  | Paris, France         |
| B2C France        | Consumer | France        | Green (#2CCA97) | Paris, France         |
| B2B European      | Business | Europe        | Blue (#3651F3)  | European address      |
| B2C European      | Consumer | Europe        | Green (#2CCA97) | European address      |
| B2B International | Business | International | Blue (#3651F3)  | International address |
| B2C International | Consumer | International | Green (#2CCA97) | International address |

All variants share:

- Same structure (header, content, social media, footer)
- Same content sections (greeting, card info, security message)
- Same footer components (legal text, unsubscribe, social icons)
- Only differ in: colors/gradients, addresses, legal text, region-specific wording

## Goals / Non-Goals

### Goals

- Create a single generic template that supports all 6 variants
- Minimize code duplication (1 template instead of 6)
- Make it easy to add new variants through configuration
- Maintain email client compatibility
- Keep template variables simple and clear

### Non-Goals

- Full templating engine implementation (keep it simple)
- Dynamic template generation at runtime (static HTML output)
- Complex inheritance or composition patterns

## Decisions

### Decision 1: Configuration-Based Approach

**What**: Use JSON configuration files to define variant-specific values
**Why**: Simple, readable, easy to maintain. No need for complex templating engine.
**Alternatives considered**:

- CSS classes with variant modifiers: More complex, harder to maintain
- Separate template files: Duplicates code 6x
- Full templating engine (Handlebars/Mustache): Overkill for this use case

### Decision 2: Template Variable System

**What**: Use simple placeholder replacement (`{{variable}}`) in HTML template
**Why**: Email clients support this, no build step required, easy to understand
**Variables include**:

- Content: `{{first_name}}`, `{{card_last_four}}`, `{{email}}`, `{{unsubscribe_url}}`
- Styling: `{{header_gradient}}`, `{{primary_color}}`, `{{footer_bg_color}}`, `{{separator_color}}`
- Branding: `{{company_address}}`, `{{logo_url}}`, `{{logo_footer_url}}`
- Region/Segment: `{{legal_text}}`, `{{region_specific_text}}`, `{{company_registration}}`

### Decision 3: Inline CSS with Variables

**What**: Keep inline CSS but make color values configurable
**Why**: Email clients require inline CSS. Variables can be replaced before sending.
**Implementation**: Replace `{{header_gradient}}` with actual gradient CSS from config

### Decision 4: Component Structure

**What**: Keep single HTML file but organize with clear sections
**Why**: Email templates work best as single files. Components are logical sections, not separate files.
**Sections**:

- Header (logo, gradient background)
- Main content (greeting, card info, security message)
- Social media promotion
- Footer (wave, chatbox, logo, socials, legal text)

### Decision 5: Configuration File Structure

**What**: One JSON config file per variant in `templates/config/card-blocked/`
**Why**: Easy to maintain, clear separation of concerns

```
templates/
├── card-blocked.html          # Generic template
└── config/
    └── card-blocked/
        ├── b2b-france.json
        ├── b2c-france.json
        ├── b2b-european.json
        ├── b2c-european.json
        ├── b2b-international.json
        └── b2c-international.json
```

## Configuration Schema

```json
{
  "variant": "b2c-france",
  "segment": "B2C",
  "region": "France",
  "styling": {
    "headerGradient": "linear-gradient(181deg, #2CCA97 -4.19%, rgba(255, 255, 255, 0) 65.81%)",
    "primaryColor": "#2CCA97",
    "footerBgColor": "#0e174c",
    "separatorColor": "#43e8b3"
  },
  "branding": {
    "logoUrl": "https://cdn.greennation.green/assets/logo.png",
    "logoFooterUrl": "https://cdn.greennation.green/assets/logo-footer.png"
  },
  "content": {
    "companyAddress": "48 Rue de la Bienfaisance, 75008 Paris, France",
    "companyRegistration": "Green Nation, société immatriculée au R.C.S de Paris sous le numéro 953371085...",
    "legalText": "Cette carte Visa est émise par UAB StanHope..."
  }
}
```

## Risks / Trade-offs

### Risk: Template Complexity

**Risk**: Generic template becomes harder to read/maintain
**Mitigation**: Keep structure clear, document variables well, use comments

### Risk: Email Client Compatibility

**Risk**: Variable replacement might break in some clients
**Mitigation**: Variables are replaced server-side before sending, clients see final HTML

### Trade-off: Flexibility vs Simplicity

**Trade-off**: More configurable = more complex
**Decision**: Keep it simple - only make truly variant-specific things configurable

## Migration Plan

1. **Phase 1**: Create generic template with variables
2. **Phase 2**: Create config files for all 6 variants
3. **Phase 3**: Test all variants render correctly
4. **Phase 4**: Update any systems using the template to use new variable system

## Open Questions

- Do we need a build step to generate final HTML, or replace variables at send time?
- Should we create a simple Node.js script to render templates with configs?
- Are there any other differences between B2B and B2C beyond colors? (tone, legal text)
