## Context

Currently, the email template system has a single common layout (`layouts/common-layout.html`) that contains only footer and unsubscribe sections. Content files contain everything else (header, body, social media).

For card-blocked type emails (security notifications like card blocked, suspicious login, etc.), there are shared patterns:

- Same logo placement (top-right)
- Same gradient header background
- Same heading structure (multipart with emoji)
- Same greeting pattern
- Same social media promotion section

These shared components are currently duplicated in content files. Creating a specialized layout for card-blocked type emails will centralize these components.

## Goals / Non-Goals

**Goals:**

- Create a specialized Postmark layout for card-blocked type emails
- Centralize logo row, heading, greeting, and social media promotion in the layout
- Reduce duplication across similar notification emails
- New files only - no modification to existing files

**Non-Goals:**

- Modifying existing layout or content files
- Creating layouts for other email types (welcome, etc.)
- Changing the template variable system

## Decisions

### Decision 1: Separate Layout for Card-Blocked Emails

**What**: Create `layouts/card-blocked-layout.html` as a separate file from `common-layout.html`

**Why**:

- Welcome emails have significantly different structure (features grid, impact section, etc.)
- Card-blocked type emails share more common components (logo, heading pattern, greeting, social media)
- Keeping separate layouts allows each to evolve independently

**Alternatives considered**:

- Single layout with conditional sections: Rejected - Postmark layouts don't support conditionals
- Parameterized layout: Rejected - Would make template variables complex

### Decision 2: New Content File Version

**What**: Create `content/card-blocked-content-v2.html` instead of modifying existing

**Why**:

- Existing content file (`card-blocked-content.html`) works with current layout
- New content file will only contain card-specific body content (card info, security message)
- Allows gradual migration without breaking existing setup

### Decision 3: Layout Structure

**What**: The card-blocked layout will contain (in order):

1. HTML document structure with CSS
2. Logo row
3. Header with gradient background
4. Heading section (with `{{heading_part1}}`, `{{heading_part2}}`, `{{heading_part3}}`)
5. Greeting section (`{{greeting}} {{first_name}},`)
6. `{{{ @content }}}` placeholder
7. Social Media Promotion section
8. Footer section
9. Unsubscribe section

**Why**: This matches the current card-blocked email structure while maximizing shared components

## Risks / Trade-offs

| Risk                      | Mitigation                                                      |
| ------------------------- | --------------------------------------------------------------- |
| Two layouts to maintain   | Clear documentation on which layout to use for which email type |
| Template variable overlap | Consistent variable naming across both layouts                  |
| Migration complexity      | New files only, existing system continues to work               |

## Migration Plan

1. Create new layout file (`card-blocked-layout.html`)
2. Create new content file (`card-blocked-content-v2.html`)
3. Test with Postmark
4. Document which emails should use which layout
5. Future similar emails can use the new layout

No rollback needed since existing files are unchanged.

## Open Questions

- Should other notification emails (suspicious login, account closure) use this layout in the future?
  - Answer: Yes, this layout is designed for that purpose. Implementation will be in separate changes.
