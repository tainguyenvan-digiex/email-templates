# Oxen Postmark Layout Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create `layouts/oxen-layout.html` — the Postmark layout for all Oxen dark-theme transactional emails — following the same `{{{ @content }}}` injection pattern used in `layouts/common-layout.html`.

**Architecture:** Single layout file owns the HTML boilerplate (head, dark-mode CSS, MSO conditionals), the silk-wave header with Outlook VML fallback, and the shared footer. Each Oxen email template injects its body rows into `{{{ @content }}}`. All i18n strings are flat top-level Postmark variables — no nested objects, no conditionals.

**Tech Stack:** HTML email (table-based), Postmark Handlebars templating (`{{variable}}`, `{{{@content}}}`), VML for Outlook background image fallback, Google Fonts (DM Sans + Bellfair), GitHub raw CDN for images.

---

## Reference files

| File                                       | Role                                                           |
| ------------------------------------------ | -------------------------------------------------------------- |
| `layouts/common-layout.html`               | Pattern to follow (structure, `{{{ @content }}}` slot, footer) |
| `oxen-emails/oxen-email-payment-sent.html` | Source of Oxen dark-theme boilerplate and VML header           |
| `assets/silk-wave-header.png`              | Header background (already on GitHub CDN)                      |
| `assets/logo.png`                          | Oxen logo (already on GitHub CDN)                              |

---

## Files

| Path                       | Action     | Responsibility                                        |
| -------------------------- | ---------- | ----------------------------------------------------- |
| `layouts/oxen-layout.html` | **Create** | Shared Postmark layout for all Oxen dark-theme emails |

---

## Figma design tokens (node 68:2)

| Element                  | Value                    |
| ------------------------ | ------------------------ |
| Top / footer dividers    | `rgba(192,139,136,0.08)` |
| Body / sign-off dividers | `rgba(192,139,136,0.05)` |
| Footer / label text      | `rgba(245,240,235,0.35)` |
| Footer links             | `rgba(245,240,235,0.6)`  |
| Ref text                 | `rgba(245,240,235,0.2)`  |

---

## Variable inventory (flat — no nested objects)

| Variable               | Example value                                                                                                                         |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `{{title}}`            | `Payment sent`                                                                                                                        |
| `{{lang_code}}`        | `en`                                                                                                                                  |
| `{{ref}}`              | `TXN-2026-12044`                                                                                                                      |
| `{{footer_automated}}` | `This is an automated message from Oxen. Please do not reply.`                                                                        |
| `{{footer_legal}}`     | `Oxen is a platform operated by Escrowfy GmbH, Bahnhofstrasse 7, 6300 Zug, Switzerland (CHE-281.608.494). VQF/SRO Member Nr. 101009.` |
| `{{footer_help}}`      | `Help Centre`                                                                                                                         |
| `{{footer_privacy}}`   | `Privacy Policy`                                                                                                                      |
| `{{footer_terms}}`     | `Terms of Service`                                                                                                                    |
| `{{footer_copyright}}` | `© 2026 Oxen Finance`                                                                                                                 |

---

## Task 1: Create `layouts/oxen-layout.html`

**Files:**

- Create: `layouts/oxen-layout.html`

- [x] **Step 1: Write the layout file**

```html
<!doctype html>
<html
  lang="{{lang_code}}"
  xmlns="http://www.w3.org/1999/xhtml"
  xmlns:v="urn:schemas-microsoft-com:vml"
  xmlns:o="urn:schemas-microsoft-com:office:office"
>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="x-apple-disable-message-reformatting" />
    <meta
      name="format-detection"
      content="telephone=no,address=no,email=no,date=no,url=no"
    />
    <meta name="color-scheme" content="only dark" />
    <meta name="supported-color-schemes" content="only dark" />
    <title>{{title}}</title>

    <link
      href="https://fonts.googleapis.com/css2?family=Bellfair&family=DM+Sans:wght@400;500;600&display=swap"
      rel="stylesheet"
    />

    <!--[if mso]>
      <noscript>
        <xml>
          <o:OfficeDocumentSettings>
            <o:AllowPNG />
            <o:PixelsPerInch>96</o:PixelsPerInch>
          </o:OfficeDocumentSettings>
        </xml>
      </noscript>
      <style type="text/css">
        table,
        td {
          font-family: "DM Sans", Arial, sans-serif !important;
        }
      </style>
    <![endif]-->

    <style type="text/css">
      :root {
        color-scheme: dark only;
      }
      body,
      .body {
        background-color: #0c0d14 !important;
      }
      [data-ogsc] body,
      [data-ogsc] .body {
        background-color: #0c0d14 !important;
      }
      u + .body {
        background-color: #0c0d14 !important;
      }
      img {
        border: 0;
        height: auto;
        line-height: 100%;
        outline: none;
        text-decoration: none;
        -ms-interpolation-mode: bicubic;
      }
      table,
      td {
        mso-table-lspace: 0pt;
        mso-table-rspace: 0pt;
      }
    </style>
  </head>
  <body
    class="body"
    style="
      margin: 0;
      padding: 0;
      background-color: #0c0d14;
      color-scheme: dark only;
      -webkit-text-size-adjust: none;
      -ms-text-size-adjust: 100%;
    "
  >
    <!-- Outer wrapper -->
    <table
      role="presentation"
      width="100%"
      cellpadding="0"
      cellspacing="0"
      border="0"
      style="background-color: #0c0d14"
    >
      <tr>
        <td align="center" style="padding: 0">
          <!-- 600px email container -->
          <table
            role="presentation"
            width="600"
            cellpadding="0"
            cellspacing="0"
            border="0"
            style="max-width: 600px; width: 100%; background-color: #0c0d14"
          >
            <!-- ========== HEADER: Silk wave + Logo ========== -->
            <tr>
              <td
                align="center"
                style="
                  padding: 0;
                  background-color: #0c0d14;
                  background-image: url('https://raw.githubusercontent.com/tainguyenvan-digiex/email-templates/main/assets/silk-wave-header.png');
                  background-size: 600px 240px;
                  background-position: center top;
                  background-repeat: no-repeat;
                "
              >
                <!--[if gte mso 9]><v:rect xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false" style="width:600px;height:240px;"><v:fill type="frame" src="https://raw.githubusercontent.com/tainguyenvan-digiex/email-templates/main/assets/silk-wave-header.png" color="#0C0D14"/><v:textbox inset="0,0,0,0"><div style="text-align:center;"><![endif]-->
                <table
                  role="presentation"
                  cellpadding="0"
                  cellspacing="0"
                  border="0"
                >
                  <tr>
                    <td style="height: 40px; font-size: 0; line-height: 0">
                      &nbsp;
                    </td>
                  </tr>
                  <tr>
                    <td align="center">
                      <a href="https://oxen.finance" target="_blank">
                        <img
                          src="https://raw.githubusercontent.com/tainguyenvan-digiex/email-templates/main/assets/logo.png"
                          alt="Oxen"
                          width="140"
                          style="display: block; width: 140px; height: auto"
                        />
                      </a>
                    </td>
                  </tr>
                  <tr>
                    <td style="height: 40px; font-size: 0; line-height: 0">
                      &nbsp;
                    </td>
                  </tr>
                </table>
                <!--[if gte mso 9]></div></v:textbox></v:rect><![endif]-->
              </td>
            </tr>

            <!-- Header divider -->
            <tr>
              <td style="padding: 0 32px">
                <table
                  role="presentation"
                  width="100%"
                  cellpadding="0"
                  cellspacing="0"
                  border="0"
                >
                  <tr>
                    <td
                      style="border-top: 1px solid rgba(192,139,136,0.08); font-size: 0; line-height: 0; height: 1px"
                    >
                      &nbsp;
                    </td>
                  </tr>
                </table>
              </td>
            </tr>

            <!-- ========== BODY CONTENT (injected by each template) ========== -->
            {{{ @content }}}

            <!-- ========== FOOTER ========== -->

            <!-- Footer divider -->
            <tr>
              <td style="padding: 0 32px">
                <table
                  role="presentation"
                  width="100%"
                  cellpadding="0"
                  cellspacing="0"
                  border="0"
                >
                  <tr>
                    <td
                      style="border-top: 1px solid rgba(192,139,136,0.08); font-size: 0; line-height: 0; height: 1px"
                    >
                      &nbsp;
                    </td>
                  </tr>
                </table>
              </td>
            </tr>

            <!-- Automated message -->
            <tr>
              <td
                style="
                  padding: 24px 32px 0 32px;
                  font-family: 'DM Sans', Arial, sans-serif;
                  font-size: 11px;
                  color: rgba(245,240,235,0.35);
                  line-height: 18px;
                "
              >
                {{footer_automated}}
              </td>
            </tr>

            <!-- Legal text -->
            <tr>
              <td
                style="
                  padding: 12px 32px 0 32px;
                  font-family: 'DM Sans', Arial, sans-serif;
                  font-size: 10px;
                  color: rgba(245,240,235,0.35);
                  line-height: 16px;
                "
              >
                {{footer_legal}}
              </td>
            </tr>

            <!-- Help · Privacy · Terms -->
            <tr>
              <td
                align="center"
                style="
                  padding: 12px 32px 0 32px;
                  font-family: 'DM Sans', Arial, sans-serif;
                  font-size: 11px;
                  line-height: 18px;
                "
              >
                <a
                  href="https://oxen.finance/help"
                  style="color: rgba(245,240,235,0.6); text-decoration: none"
                  >{{footer_help}}</a
                >
                <span style="color: rgba(245,240,235,0.35)"> &middot; </span>
                <a
                  href="https://oxen.finance/privacy"
                  style="color: rgba(245,240,235,0.6); text-decoration: none"
                  >{{footer_privacy}}</a
                >
                <span style="color: rgba(245,240,235,0.35)"> &middot; </span>
                <a
                  href="https://oxen.finance/terms"
                  style="color: rgba(245,240,235,0.6); text-decoration: none"
                  >{{footer_terms}}</a
                >
              </td>
            </tr>

            <!-- Copyright -->
            <tr>
              <td
                align="center"
                style="
                  padding: 8px 32px 0 32px;
                  font-family: 'DM Sans', Arial, sans-serif;
                  font-size: 10px;
                  color: rgba(245,240,235,0.35);
                  line-height: 16px;
                "
              >
                {{footer_copyright}}
              </td>
            </tr>

            <!-- Ref -->
            <tr>
              <td
                align="right"
                style="
                  padding: 16px 32px 32px 32px;
                  font-family: 'DM Sans', Arial, sans-serif;
                  font-size: 9px;
                  color: rgba(245,240,235,0.2);
                  line-height: 14px;
                "
              >
                {{ref}}
              </td>
            </tr>
          </table>
          <!-- End 600px container -->
        </td>
      </tr>
    </table>
    <!-- End outer wrapper -->
  </body>
</html>
```

- [x] **Step 2: Verify**

```bash
grep '{{{ @content }}}' layouts/oxen-layout.html
# Expected: 1 match

grep 'silk-wave-header' layouts/oxen-layout.html
# Expected: 2 matches (CSS url + VML src)

grep 'preheader\|lang\.\|#if' layouts/oxen-layout.html
# Expected: 0 matches
```

- [x] **Step 3: Commit**

```bash
git add layouts/oxen-layout.html
git commit -m "feat: add Oxen Postmark layout with dark theme and Figma-correct design tokens"
```

---

## Validation checklist (manual, after commit)

- [x] Open in browser — silk-wave background renders, logo visible, footer shows `{{...}}` placeholders
- [ ] Upload to Postmark → Templates → Layouts — no parsing errors, `{{{ @content }}}` accepted as layout slot
- [ ] Send Postmark test with `{ "title": "Test", "lang_code": "en", "ref": "TEST-001", "footer_automated": "...", "footer_legal": "...", "footer_help": "Help Centre", "footer_privacy": "Privacy Policy", "footer_terms": "Terms of Service", "footer_copyright": "© 2026 Oxen Finance" }` — footer renders correctly
- [ ] Check Outlook — VML silk-wave image displays
- [ ] Check Gmail — Google Fonts fall back to Arial gracefully
