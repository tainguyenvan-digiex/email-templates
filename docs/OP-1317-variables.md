# OP-1317 — variables the backend must send (F01–F07, M08, M10, `-v2` aliases)

Contract between these templates and the senders (be-b2b, and gn-b2b-crypto for F03). Copy follows spec rows
F01–F07, M08 and M10 (sheets "6. Documents & fees" and "7. Team, receipts & calls"), English only.

## New aliases, the live ones stay

Postmark is one server for stg and prod, so the new copy lives in **new** aliases and the nine live aliases are not
changed. The backend switches each sender to the `-v2` alias when it sends the new values below; until then prod
keeps sending the old alias with the old copy.

| Spec | Live alias (unchanged) | New alias |
|---|---|---|
| F01 | `statement-transactions-by-period` | `statement-transactions-by-period-v2` |
| F02 | `statement-single-transaction` | `statement-single-transaction-v2` |
| F03 | `crypto-transaction-statement` | `crypto-transaction-statement-v2` |
| F04 | `rib-document` | `rib-document-v2` |
| F05 | `balance-statement` | `balance-statement-v2` |
| F06 | `monthly-statement-ready` | `monthly-statement-ready-v2` |
| F07 | `monthly-summary` | `monthly-summary-v2` |
| M08 | `receipt-final-reminder` | `receipt-final-reminder-v2` |
| M10 | `missing-receipts-summary` | `missing-receipts-summary-v2` |

- Templates: `templates/content/<alias>-v2-content.html`; configs: `templates/config/<alias>-v2/{en,fr}.json`.
  be-b2b loads params from the folder named like the alias (`getTemplateName()`), so it needs the same
  `config/email-template-params/oxen/<alias>-v2/{en,fr}.json`, and the `email_mapping` rows must point at the
  `-v2` aliases.
- **New/existing** below compares with what the backend sends to the live alias today.

## How the values reach Postmark

- The body copy is in `templates/content/<alias>-content.html`. The config `templates/config/<alias>/en.json` holds
  only `layout`, `subject`, `title` and an empty default for every variable (`""`, or `[]` for a list).
- be-b2b loads `en.json`, fills each `{{x}}` in `subject`/`title` from the values it sends, then
  `array_replace_recursive(static, dynamic)`. A variable named in the subject must therefore be sent, or the
  subject shows a gap.
- Lists (`metrics`, `expenses`) default to `[]`. The old configs had example items, and `array_replace_recursive`
  merges lists by index, so a send with fewer items than the examples showed the leftover example lines.
- The layout adds the contact line ("For any question, write to support@oxen.finance or message us on Telegram.")
  and the sign-off ("Kind regards, / The Oxen Team"). Do not send them.
- Checked in be-b2b `stg`, 2026-11-25. **Default** is the value in `en.json`; an optional value that is `""` hides its words or row.
- `first_name` is always the **recipient's** first name, never the company name. With `""` the greeting reads "Hello,".

## F01 — `statement-transactions-by-period-v2`

Subject: `Your account statement for {{period_short}} is ready` · Button: "Download the statement" → `download_url`

| Variable | Meaning | Example | New/existing | Default |
|---|---|---|---|---|
| `first_name` | Requester's first name | `Claire` | existing (empty for a business holder today) | `""` |
| `period` | Statement period, in the body | `November 01, 2026 to November 30, 2026` | existing | `""` (hides "for …") |
| `period_short` | Short period, subject only | `01 Nov to 30 Nov` | existing | `""` |
| `download_url` | Signed download link | `https://…` | existing | `""` |
| `expiration_time` | Link expiry, **in UTC**, without the zone (the template adds " UTC") | `November 25, 2026 at 3:04 PM` | existing (today in server time) | `""` (hides "(link valid until …)") |

Keys of the live alias that `-v2` does not use: `customer_name`, `expiration_hours`, all old copy keys (`message_prefix`, `message_suffix`,
`cta_text`, `expiration_message_*`, `expiration_note`, `support_*`, `footer_note`, `greeting`).

## F02 — `statement-single-transaction-v2`

Subject: `Your statement for the payment of {{transaction_amount}} is ready` · Button: "Download the statement" → `download_url`

| Variable | Meaning | Example | New/existing | Default |
|---|---|---|---|---|
| `first_name` | Requester's first name | `Claire` | existing | `""` |
| `transaction_amount` | Amount **with** its currency, shared format (D28) | `€250.00` | existing | `""` |
| `transaction_date` | Payment date | `November 20, 2026` | existing | `""` (hides "on …") |
| `counterparty` | Other party; optional panel row | `ACME SARL` | existing | `""` (row hides) |
| `reference` | Payment reference; optional panel row | `INV-2026-114` | existing | `""` (row hides) |
| `download_url` | Signed download link | `https://…` | existing | `""` |
| `expiration_time` | Link expiry in UTC, no zone | `November 25, 2026 at 3:04 PM` | existing | `""` |

Keys of the live alias that `-v2` does not use: `transaction_currency` (the currency is part of `transaction_amount`), `customer_name`,
`expiration_hours`, old copy keys.

## F03 — `crypto-transaction-statement-v2`

Subject: `Your statement for {{transaction_amount}} {{transaction_currency}} is ready` · Button: "Download the statement" → `download_url`

| Variable | Meaning | Example | New/existing | Default |
|---|---|---|---|---|
| `first_name` | Requester's first name | `Claire` | existing | `""` |
| `transaction_amount` | Amount as a formatted string (not a Decimal) | `1,250.50` | existing (today raw `toFixed()`, e.g. `0.00125`) | `""` |
| `transaction_currency` | Asset symbol | `USDC` | existing | `""` |
| `transaction_date` | Transaction date | `November 20, 2026` | existing (today ISO `2026-11-20`) | `""` (hides "on …") |
| `counterparty` | Beneficiary; optional panel row | `Jane Smith` | existing | `""` (row hides) |
| `tx_hash` | Transaction hash; optional panel row | `0x9f2c…e8f` | existing | `""` (row hides) |
| `download_url` | Signed download link | `https://…` | existing | `""` |
| `expiration_time` | Link expiry in UTC, no zone | `November 25, 2026 at 3:04 PM` | **new** (computed by be-b2b but not sent) | `""` |

Keys of the live alias that `-v2` does not use: `customer_name` (held the counterparty, bug P1), `method`, old copy keys.

## F04 — `rib-document-v2` (account details letter)

Subject: `Your account details letter is ready` · Button: "Download the letter" → `download_url`

| Variable | Meaning | Example | New/existing | Default |
|---|---|---|---|---|
| `first_name` | Requester's first name | `Claire` | existing (**today the holder's full name, i.e. the company**) | `""` |
| `account_name` | Account name | `Main EUR account` | existing | `""` |
| `account_number` | Account identifier (IBAN or correspondent's) | `FR76 1234 5678 9012 3456 7890 123` | existing | `""` (hides "(…)") |
| `download_url` | Signed download link | `https://…` | existing | `""` |
| `expiration_time` | Link expiry in UTC, no zone | `November 25, 2026 at 3:04 PM` | existing | `""` |

Keys of the live alias that `-v2` does not use: `customer_name`, `expiration_hours`, old copy keys.

## F05 — `balance-statement-v2`

Subject: `Your statement of balances is ready` · Button: "Download the statement" → `download_url`

Same variables, meanings and defaults as F04 (`first_name` must become the requester's first name;
it is the company name today).

## F06 — `monthly-statement-ready-v2`

Subject: `Your {{month_year}} statement is ready` · Button: "View the statement" → `statement_url`

| Variable | Meaning | Example | New/existing | Default |
|---|---|---|---|---|
| `first_name` | Recipient's first name | `Claire` | existing | `""` |
| `company_name` | Company name | `Green Bakery SAS` | existing (added by GenericNotificationHandler) | `""` (hides "of …") |
| `month_year` | Statement month | `October 2026` | existing | `""` |
| `statement_url` | Portal statement download page with the month preselected; built by the backend | `https://portal.oxen.finance/…` (the statements page with that month selected) | **new** (replaces `cta_url`/`statementLink`, which point to the dashboard) | `""` |

Keys of the live alias that `-v2` does not use: `cta_url`, `cta_text`, `statement_ready_*`, `sign_off`, `signature`.

## F07 — `monthly-summary-v2`

Subject: `Your Oxen activity in {{month_year}}` · Button: "Go to my dashboard" → `cta_url`

| Variable | Meaning | Example | New/existing | Default |
|---|---|---|---|---|
| `first_name` | Recipient's first name | `Claire` | existing | `""` |
| `company_name` | Company name | `Green Bakery SAS` | existing | `""` (hides "of …") |
| `month_year` | Month summarised | `October 2026` | existing | `""` |
| `metrics` | List of `{"this": "<line>"}`, one bullet each | `[{"this":"46 transactions"},{"this":"5 active users"},{"this":"€8,350.00 total spending"}]` | existing (the lines must be filled: today the `{{…}}` in translations/report.en.yaml are likely not substituted) | `[]` |
| `receipts_line` | `"{n} card payments are still missing a receipt."`, `""` when n = 0 | `2 card payments are still missing a receipt.` | **new** | `""` (line hides) |
| `cta_url` | Dashboard URL | `https://…/dashboard` | existing (falls back to the universal link root) | `""` |

Keys of the live alias that `-v2` does not use: `heading_*`, `summary_intro_prefix`, `cta_text`, `signature`.

## M08 — `receipt-final-reminder-v2`

Subject: `Reminder: receipt missing for {{amount}} at {{merchant}}` · Button: "Add the receipt" → `cta_url`

| Variable | Meaning | Example | New/existing | Default |
|---|---|---|---|---|
| `first_name` | Cardholder's first name | `Claire` | existing | `""` |
| `amount` | Amount with currency | `€72.00` | existing | `""` |
| `merchant` | Merchant name | `Uber` | existing | `""` (hides "at …" in the body; the subject keeps "at") |
| `date` | Payment date | `22/11/2026` | existing | `""` (hides "on …") |
| `cta_url` | Expense receipts page | `https://…` | existing key, **new value** (today unset, so the universal link root; the transaction link is in `cta_link`) | `""` |

Keys of the live alias that `-v2` does not use: `final_reminder_message`, `action_message`, `cta_text`, `signature`.

## M10 — `missing-receipts-summary-v2`

Subject: `{{transactions_count}} card payments without a receipt this week` · Button: "Open expenses" → `cta_url`

| Variable | Meaning | Example | New/existing | Default |
|---|---|---|---|---|
| `first_name` | Recipient's first name | `Claire` | existing | `""` |
| `start_date` | First day of the week, full | `November 18` | existing (**today the day only, `18`**) | `""` |
| `end_date` | Last day of the week | `November 25` | existing | `""` |
| `transactions_count` | Number of card payments without a receipt | `2` | existing (today the count of the list, capped at 100) | `""` |
| `expenses` | List of `{"this": "<line>"}`, one per payment | `[{"this":"Thomas D. – €58.90 – Biocoop – 24/11"}]` | existing | `[]` |
| `cta_url` | Expense receipts page | `https://…` | existing key, **new value** (today the universal link root) | `""` |

Keys of the live alias that `-v2` does not use: `summary_intro`, `action_message`, `signature`.
