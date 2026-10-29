# Candidate profile

Knowledge base about the candidate, filled by agent during `/interview` and `/rate-offer`.
Candidate can edit this file manually at any time.

## Technologies

Levels are defined in `templates/technologies.md`.

| Technology | Category | Level (0-4) | Years | Last used | Context | Wants to use | Notes |
| ---------- | -------- | ----------- | ----- | --------- | ------- | ------------ | ----- |

## Skill details

Answers to calibration questions, per technology. `[x]` = yes, `[ ]` = no.

<!-- Example:
### Spring Boot
- [x] L1 Created Spring Boot application with REST endpoints
- [x] L3 Configured Spring Security
- [ ] L4 Implemented own Spring Boot starter
-->

## Learned from offers

Skills clarified when rating offers. Reused for next offers.

| Date | Offer | Question | Answer | Saved to |
| ---- | ----- | -------- | ------ | -------- |

## Seniority

Levels and signals are defined in *Seniority table* in `templates/constants.md`.

- Self-assessed level:
- Level estimated by agent from sources and interview:
- Target level (what candidate applies for):

## Preferences

Weight of every preference, used for preference match rating:

| weight | meaning |
| ------ | ------- |
| deal-breaker | offer violating it is marked as not suitable, regardless of other ratings |
| important | 1 point when met, reported as important when missed |
| nice | 1 point when met, reported as nice when missed |
| don't care | ignored |

| Preference | How to ask | Value | Weight |
| ---------- | ---------- | ----- | ------ |
| Work mode | how much days per week at home | | |
| Location | city, max commute | | |
| Contract type | HPP / IČO / both | | |
| Salary - survival minimum | what candidate needs to survive, below it offer is always deal-breaker | | deal-breaker |
| Salary - expected | what candidate expects and wants | | |
| Preferred role complexity | choose option(s) from *Role competence complexity table* | | |
| Wanted responsibilities | choose option(s) from *Responsibilities merge table* | | |
| Unwanted responsibilities | choose option(s) from *Responsibilities merge table* | | |
| Preferred domains | | | |
| Avoided domains | | | |
| Other | | | |

## Writing style

Filled by `/cover-letter` from candidate own letters. Samples are stored in `profile/writing-samples/`,
generated letters in `profile/cover-letters/`.

- Name for signature:
- Contact in signature (e-mail, phone, LinkedIn, GitHub):
- Letter languages:

### Samples

Only letters written or at least finalized by candidate, not raw AI output.

| File | Offer / company | Employer type | Prompt type | Language | Written by |
| ---- | --------------- | ------------- | ----------- | -------- | ---------- |

### Style notes

Learned from samples, used instead of *Tone by employer type* in `templates/cover-letter.md` where filled.

| Property | Value |
| -------- | ----- |
| Typical length | |
| Sentence length and structure | |
| Formality, Ty / Vy, I / we | |
| Greeting and closing | |
| Typical vocabulary and phrases | |
| Phrases candidate never uses | |
| Punctuation habits | |
| How candidate presents results | |

| Employer type | Differences from the style above |
| ------------- | -------------------------------- |
