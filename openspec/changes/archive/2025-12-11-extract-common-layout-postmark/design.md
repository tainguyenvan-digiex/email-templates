## Context

Postmark supports a Layout system where reusable components (headers, footers, CSS) can be defined once and shared across multiple templates. Templates reference a layout and provide their unique content through a `{{{ content }}}` placeholder.

Current templates (`welcome.html`, `card-blocked.html`) have significant duplication:
- Identical footer sections (~320 lines each)
- Identical unsubscribe sections (~85 lines each)
- Identical CSS styles in `<head>` (~150 lines each)
- Similar header structure (logo placement, gradient backgrounds)

## Goals / Non-Goals

### Goals
- Extract common footer and unsubscribe sections into a reusable Postmark layout
- Extract common CSS styles into layout
- Create content-only files for welcome and card-blocked templates (no footer/unsubscribe/CSS)
- Maintain email client compatibility (Outlook, Gmail, Apple Mail)
- Preserve all template variables and functionality
- Enable easy upload to Postmark's template system
- Reduce code duplication by ~500+ lines per template
- Keep existing template files unchanged for backward compatibility

### Non-Goals
- Changing template variable names or structure
- Modifying visual design or styling
- Supporting other email service providers (SendGrid, Mailgun, etc.)
- Creating a build system or preprocessing pipeline

## Decisions

### Decision: Use Postmark Layouts (not partials or includes)
- **Rationale**: Postmark's Layout system is the native way to share components. Layouts wrap template content, which matches our use case (footer/unsubscribe wrap all templates). Partials would require different template structure.
- **Alternatives considered**: 
  - Build-time includes/partials: Would require build tooling, not Postmark-native
  - Copy-paste: Current approach, causes maintenance issues

### Decision: Extract footer and unsubscribe into layout (not header)
- **Rationale**: Footer and unsubscribe are truly identical across templates. Header has some variation (different headings, content). Keeping header in templates allows flexibility while standardizing footer.
- **Alternatives considered**:
  - Extract header too: Would reduce flexibility for template-specific headers
  - Keep footer in templates: Doesn't solve duplication problem

### Decision: Keep template-specific CSS in templates
- **Rationale**: Common CSS (reset, responsive, footer styles) goes in layout. Template-specific styles (if any) stay in templates. This balances reusability with flexibility.
- **Alternatives considered**:
  - All CSS in layout: Too rigid, templates might need custom styles
  - All CSS in templates: Doesn't reduce duplication

### Decision: Create separate content files (don't modify existing templates)
- **Rationale**: Preserve existing template files for backward compatibility and reference. Create new content-only files that contain just the template-specific sections (no footer, unsubscribe, or CSS). These content files are designed to be inserted into Postmark layouts.
- **Alternatives considered**:
  - Modify existing templates: Would break backward compatibility and make it harder to compare old vs new structure
  - Create content files: Allows preserving originals while providing Postmark-ready content files

### Decision: Use `{{{ content }}}` placeholder (triple braces)
- **Rationale**: Postmark uses Handlebars syntax. Triple braces prevent HTML escaping, which is required for email HTML content.
- **Alternatives considered**:
  - Double braces `{{ content }}`: Would escape HTML, breaking email structure

## Risks / Trade-offs

### Risk: Template variable scope
- **Mitigation**: Ensure all template variables used in layout are documented and provided by all templates. Layout variables should be clearly separated from template-specific variables.

### Risk: Email client compatibility
- **Mitigation**: Maintain table-based structure, inline styles. Test in major clients (Outlook, Gmail, Apple Mail) after refactoring.

### Risk: Postmark layout limitations
- **Mitigation**: Verify Postmark layout supports all required features (nested tables, complex CSS, variables) before full implementation.

### Trade-off: Less flexibility for template-specific footers
- **Impact**: If a template needs a different footer in the future, we'd need to either create a new layout or override the layout. This is acceptable given current requirements show identical footers.

## Migration Plan

1. **Create layout file**: Extract common components to `layouts/common-layout.html`
2. **Create content files**: Extract template-specific content to `content/welcome-content.html` and `content/card-blocked-content.html`
3. **Preserve originals**: Keep `templates/welcome.html` and `templates/card-blocked.html` unchanged
4. **Test locally**: Combine layout + content files manually to verify rendering
5. **Upload to Postmark**: 
   - Upload layout to Postmark server
   - Upload content files as templates (associate with layout)
   - Associate templates with layout in Postmark UI
6. **Validate**: Test email rendering in Postmark preview and actual email clients
7. **Documentation**: Document the relationship between content files and layout

## Open Questions

- Should we create separate layouts for B2B vs B2C if footer colors differ? (Currently footer uses fixed color #0e174c)
- How should we handle template variables that are only used in layout? (Document in config files?)
- Should we version the layout file for future changes?

