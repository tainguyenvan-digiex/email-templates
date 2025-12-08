## 1. Analysis and Planning

- [x] 1.1 Identify all hardcoded text content in template (title, headings, body text, footer)
- [x] 1.2 Document text content structure (which text appears where, context)
- [x] 1.3 Define language file schema and variable naming convention
- [x] 1.4 List all text that needs translation (French → English)

## 2. Language Files Creation

- [x] 2.1 Create `templates/config/card-blocked/languages/` directory
- [x] 2.2 Create `fr.json` with all French text content
- [x] 2.3 Create `en.json` with all English translations
- [x] 2.4 Ensure both language files have identical structure/keys
- [x] 2.5 Add language-specific alt text for images

## 3. Template Refactoring

- [x] 3.1 Replace page title with `{{lang.title}}`
- [x] 3.2 Replace preheader text with `{{lang.preheader}}`
- [x] 3.3 Replace main heading parts with `{{lang.heading.*}}` variables
- [x] 3.4 Replace greeting with `{{lang.greeting}}`
- [x] 3.5 Replace card info text with `{{lang.card_info.*}}` variables
- [x] 3.6 Replace security message with `{{lang.security.*}}` variables
- [x] 3.7 Replace social media section text with `{{lang.social.*}}` variables
- [x] 3.8 Replace footer text with `{{lang.footer.*}}` variables
- [x] 3.9 Replace image alt text with language variables
- [x] 3.10 Update HTML `lang` attribute to use `{{lang_code}}` variable

## 4. Configuration Updates

- [x] 4.1 Update variant config schema to include `language` field
- [x] 4.2 Update all 6 variant configs to specify default language
- [x] 4.3 Document how to override language at send time
- [x] 4.4 Update configuration README with language support

## 5. Documentation

- [x] 5.1 Document language file structure and schema
- [x] 5.2 Document how to add new languages
- [x] 5.3 Create translation guide for translators
- [x] 5.4 Update VARIABLES.md with language variables
- [x] 5.5 Update project.md with multi-language conventions

## 6. Testing

- [ ] 6.1 Test French language renders correctly
- [ ] 6.2 Test English language renders correctly
- [ ] 6.3 Verify all text is replaced (no hardcoded French)
- [ ] 6.4 Test language switching at send time
- [ ] 6.5 Verify email client compatibility for both languages
