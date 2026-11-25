# OP-1170 — F08 fee change notice: variables the backend must send

Alias `fee-change-notice` (new), layout `oxen-layout`, English only. Sender: be-b2b, after
`POST /legacy/pri/admin/fee-change-notices`, through the notification service, one e-mail per affected company to
Owner, Admin and Accountant. Copy = spec F08, with the approved change: the fee changes are listed in the e-mail
instead of "The new rate card is attached to this email." No button. The layout adds the contact line and
"Kind regards, / The Oxen Team".

Subject and title (en.json): `Changes to your Oxen fees from {{effective_date}}`. be-b2b fills `{{effective_date}}`
in the config strings from the values it sends, so `effective_date` must always be sent.

| Variable | Meaning | Example | Default in en.json |
|---|---|---|---|
| `first_name` | Recipient's first name; `""` when unknown | `Claire` | `""` (greeting reads "Hello,") |
| `company_name` | Company whose fees change | `Green Bakery SAS` | `""` (hides "of …") |
| `effective_date` | The new version's `effective_from`, UTC date | `December 25, 2026` | `""` |
| `fee_changes` | List of `{fee_name, old_fee, new_fee}`, one panel row each ("fee_name: old_fee → new_fee") | `[{"fee_name": "SEPA outgoing payment", "old_fee": "€0.50", "new_fee": "€0.80"}, {"fee_name": "Currency conversion", "old_fee": "0.20%", "new_fee": "0.25%"}]` | `[]` (the panel hides) |
| `recipient_email` | Added by be-b2b on every send; not rendered | | `""` |

- `fee_name`: `fee_processes.name`.
- `old_fee` / `new_fee`: formatted fee, same format on both sides: a fixed amount with its currency (`€0.50`) or a
  percentage (`0.20%`). Fold min/max into the string if they changed (the template shows the string as is).
- `fee_changes` must be a JSON array (default `[]`, not `""`), and must not be empty when sending: an empty list hides
  the panel and the e-mail no longer says what changes.

Body as rendered:

> Hello {first_name},
>
> We are updating the fees that apply to the account of {company_name}.
>
> The new fees apply from {effective_date}.
>
> [panel: {fee_name} — {old_fee} → {new_fee}, one row per change]
>
> Your current fees stay in place until that date.
>
> If you have any question about this change, contact us.
