# Layout Migration: Backend Dynamic Fields

Templates are migrating from `shared-layout` to `oxen-layout`. Update your send logic to reference `oxen-layout` as the layout for any migrated template.

Only the fields listed below need to be injected by the backend at send time — everything else is static and resolved from the config file.

---

## Layout Config — URLs to Update Before Production

The `oxen-layout` config currently uses staging URLs. These **must be replaced with production values** before going live.

**File:** `templates/config/oxen-layout/{lang}.json`

| Field         | Current (staging)                                       |
| ------------- | ------------------------------------------------------- |
| `website_url` | `https://green-nation-6d62f9.webflow.io/`               |
| `help_url`    | `https://green-nation-6d62f9.webflow.io/`               |
| `privacy_url` | `https://green-nation-6d62f9.webflow.io/privacy-policy` |
| `terms_url`   | `https://green-nation-6d62f9.webflow.io/terms-of-use`   |

---

## welcome-email

**Config:** `templates/config/welcome-email/{lang}.json`

| Field            | Description                      | Example                                        |
| ---------------- | -------------------------------- | ---------------------------------------------- |
| `first_name`     | Recipient's first name           | `Jane`                                         |
| `account_holder` | Company / account name           | `Acme Corp`                                    |
| `account_id`     | Oxen account ID                  | `OXEN-AC-29481`                                |
| `iban_eur`       | IBAN for EUR account             | `DE89 3704 0044 0532 0130 00`                  |
| `iban_usd`       | IBAN for USD account             | `US12 3456 7890 1234 5678 90`                  |
| `currencies`     | Supported currencies             | `EUR · USD · GBP`                              |
| `bic`            | BIC / SWIFT code                 | `COBADEFFXXX`                                  |
| `am_initials`    | Account manager initials         | `C`                                            |
| `am_name`        | Account manager full name        | `Christel`                                     |
| `am_title`       | Account manager job title        | `Account Manager`                              |
| `am_email`       | Account manager email            | `cr@oxen.finance`                              |
| `am_phone`       | Account manager phone            | `+41 79 123 45 67`                             |
| `portal_url`     | Full URL to the client portal    | `https://portal.oxen.finance`                  |
| `portal_domain`  | Display text for the portal link | `portal.oxen.finance`                          |
| `onboarding_url` | Onboarding call booking URL      | `https://portal.oxen.finance/customer-support` |
