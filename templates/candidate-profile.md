# Candidate profile

Knowledge base about the candidate, filled by agent during `/job-offer-helper:interview` and `/job-offer-helper:rate-offer`.
Candidate can edit this file manually at any time.

## Job target

What candidate is looking for. Asked at first run. It only tells which offers fit, it never changes
calibration questions or the level estimated by agent (a senior may look for an easier job on purpose).

- Target field(s): <!-- backend / frontend / devops, more allowed -->
- Role complexity: <!-- from Role competence complexity table in templates/constants.md -->
- Core stack: <!-- main language and framework, for example Java + Spring Boot -->
- Target level: <!-- junior / medior / senior / lead from Seniority table -->

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
- Education:

Target level is in *Job target*.

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
| Preferred role complexity | prefilled from *Job target*, candidate can add more options from *Role competence complexity table* | | |
| Wanted responsibilities | choose option(s) from *Responsibilities merge table* | | |
| Unwanted responsibilities | choose option(s) from *Responsibilities merge table* | | |
| Preferred domains | | | |
| Avoided domains | | | |
| Other | | | |

## Letter material

Filled by `/job-offer-helper:letter-interview`, used by `/job-offer-helper:cover-letter`. What the CV can not show.
Only what candidate said or confirmed.

### Way of working

| Topic | Answer | Proof | Offer phrases it answers |
| ----- | ------ | ----- | ------------------------ |

### Own words

Answers word for word, only typos fixed. Letters are built from these sentences.

### Direction

- Career path:
- In two years:
- Gives energy:
- Drains (never in letters):

## Strengths and stories

Filled by `/job-offer-helper:letter-interview`, used by `/job-offer-helper:cover-letter` for *why hire me* answers and
soft *must haves*. Only facts candidate gave or confirmed.

### Strengths

| Strength | Proved by stories | Offer phrases it answers |
| -------- | ----------------- | ------------------------ |

### Stories

| Id | Story (plain words) | Starting state | What candidate did | Result | Strengths | Used in letters |
| -- | ------------------- | -------------- | ------------------ | ------ | --------- | --------------- |

### Other

- Proudest result:
- Praised by colleagues / manager for:
- Different from other candidates on same level:
- Motivation (why looking now):
- Never mention in letters:

## Writing style

Filled by `/job-offer-helper:cover-letter` from candidate own letters. Samples are stored in `~/JobOfferHelper/writing-samples/`,
generated letters in offer folders `~/JobOfferHelper/offer-results/<offer>/cover-letter-*.md`.
*Used in letters* column in *Stories* lists offer folder names.

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
