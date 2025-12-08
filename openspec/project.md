# Project Context

## Purpose

This project manages email templates for transactional and marketing emails. The goal is to create reusable, maintainable, and responsive email templates that work across major email clients.

## Tech Stack

- **Template Language**: HTML/CSS (with consideration for email client compatibility)
- **Templating Engine**: [To be determined - options: Handlebars, Mustache, MJML, or plain HTML]
- **Build Tooling**: [To be determined - options: Node.js/TypeScript for preprocessing, or static HTML]
- **Testing**: Email client testing tools (Litmus, Email on Acid, or manual testing)

## Project Conventions

### Code Style

- Use semantic HTML5 elements where supported by email clients
- Inline CSS for email compatibility (or use CSS-inlining tool)
- Use table-based layouts for complex email structures (for Outlook compatibility)
- Follow email-safe color codes (hex format)
- Use descriptive class names and IDs
- Comment complex layout sections

### Architecture Patterns

- **Template Structure**: Generic templates with configuration files for variants
- **Template Variables**: Use `{{variable_name}}` syntax for configurable values
- **Multi-Language Support**: Language files (`languages/*.json`) contain all translatable text
- **Language Variables**: Use `{{lang.*}}` prefix for language-specific content
- **Configuration System**: JSON config files define variant-specific values (colors, addresses, legal text)
- **Component Reuse**: Single template file supports multiple variants and languages through configuration
- **Responsive Design**: Mobile-first approach with media queries
- **Email Client Compatibility**: Test against major clients (Gmail, Outlook, Apple Mail, etc.)
- **Version Control**: Track template versions and changes

### Testing Strategy

- Visual testing across major email clients
- HTML validation
- Link and image validation
- Accessibility checks (alt text, color contrast)
- Spam score testing
- Manual review checklist before deployment

### Git Workflow

- **Branching**: Feature branches for new templates (`feature/template-name`)
- **Commits**: Conventional commits format (`feat:`, `fix:`, `refactor:`)
- **Review**: Template changes require visual review before merge
- **Tags**: Version tags for template releases

## Domain Context

- Email templates must work in email clients with limited CSS support
- Outlook uses Word rendering engine (requires specific HTML patterns)
- Many email clients strip `<style>` tags, requiring inline styles
- Dark mode support may be needed for modern email clients
- Email width typically 600px max for desktop, responsive for mobile
- Images should be hosted externally (not embedded)
- Plain text alternatives recommended for accessibility

## Important Constraints

- **Email Client Compatibility**: Must render correctly in Outlook (Windows), Gmail, Apple Mail, and major mobile clients
- **File Size**: Keep HTML size reasonable (<100KB recommended)
- **Image Hosting**: Images must be hosted on reliable CDN or server
- **Accessibility**: WCAG 2.1 AA compliance where possible
- **Deliverability**: Templates should not trigger spam filters

## External Dependencies

- Email service provider (SendGrid, Mailgun, AWS SES, etc.) - [To be specified]
- Image hosting/CDN - [To be specified]
- Email testing service (optional) - [To be specified]
