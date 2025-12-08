## 1. Analysis and Planning

- [x] 1.1 Compare all 6 Figma designs to identify differences between variants
- [x] 1.2 Document all variant-specific values (colors, gradients, addresses, legal text)
- [x] 1.3 Identify which parts are truly common vs variant-specific
- [x] 1.4 Define naming convention for config files and variables

## 2. Template Refactoring

- [x] 2.1 Extract all hardcoded values to template variables in `card-blocked.html`
- [x] 2.2 Replace gradient definitions with `{{header_gradient}}` variable
- [x] 2.3 Replace color values with variables (`{{primary_color}}`, `{{footer_bg_color}}`, `{{separator_color}}`)
- [x] 2.4 Replace address with `{{company_address}}` variable
- [x] 2.5 Replace legal text with `{{legal_text}}` and `{{company_registration}}` variables
- [x] 2.6 Replace logo URLs with `{{logo_url}}` and `{{logo_footer_url}}` variables
- [x] 2.7 Add comments marking configurable sections

## 3. Configuration System

- [x] 3.1 Create `templates/config/card-blocked/` directory structure
- [x] 3.2 Create config file: `b2b-france.json`
- [x] 3.3 Create config file: `b2c-france.json`
- [x] 3.4 Create config file: `b2b-european.json`
- [x] 3.5 Create config file: `b2c-european.json`
- [x] 3.6 Create config file: `b2b-international.json`
- [x] 3.7 Create config file: `b2c-international.json`
- [x] 3.8 Define configuration schema with all required fields

## 4. Documentation

- [x] 4.1 Document all template variables and their purposes
- [x] 4.2 Create example configuration file with comments
- [x] 4.3 Document how to add new variants (new regions, new segments)
- [x] 4.4 Update `openspec/project.md` with template system conventions

## 5. Testing

- [ ] 5.1 Test B2B France variant renders correctly
- [ ] 5.2 Test B2C France variant renders correctly
- [ ] 5.3 Test B2B European variant renders correctly
- [ ] 5.4 Test B2C European variant renders correctly
- [ ] 5.5 Test B2B International variant renders correctly
- [ ] 5.6 Test B2C International variant renders correctly
- [ ] 5.7 Verify email client compatibility for all variants
- [ ] 5.8 Test variable replacement doesn't break HTML structure
