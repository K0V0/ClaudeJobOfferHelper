I am doing app that should help the candidates to filter out job offers, but you will need to know what candidate     
know

My exceptation is that the human who first runt this app on his claude will start interview with You - for exaple You will ask what technology is he     
using

- user will answer for example "Spring boot"

Are you able to give him 5 to 10 questions, not long to each tecnology the user will name and memorize the answer - write it into user visible MD file   
in this project ?

Then use that knowledge to process actual offer ?

Is it doable this way or are there some optimalizations ? - for example for consistency I have an idea of generating 
some lists of most common technologies and skills in IT and questions to each that everyone gets ? 

---

## Claude answer

Yes, this works well with Claude Code. A few changes are recommended before building it - the main risk is the user
getting tired of questions, not anything technical.

### What works as described

- At the start, Claude asks "what technologies do you use?", then asks follow-ups for each one and writes the answers
  to a markdown file in the project, for example `profile/candidate-knowledge.md`.
- Later, when the user pastes an offer, Claude reads that file and rates the match (must have, nice to have, total).
- Put this in a skill or slash command (`/interview` and `/rate-offer`), with a line in `CLAUDE.md` pointing to the
  profile file, so it runs the same way every time.

### Recommended changes

**1. Ask about experience, not exam questions.**
To match offers you need to know how deep and how recent the experience is, not whether the candidate can answer
trivia. Use the same short template for every technology:
- Years of use, and when last used
- Context: production, side project, or just studied
- Depth level on a fixed scale: `0 none · 1 tutorial · 2 used with help · 3 independent in prod · 4 designs/mentors others`
- 1-2 questions specific to that technology to place them on the scale
- Whether they want to keep working with it (covers "rate candidate preference")

**2. The common list idea is good - make it a catalog that grows.**
- Static `templates/technologies.md` with common technologies, each with categories, aliases
  (`Postgres` = `PostgreSQL`, `k8s` = `Kubernetes`), related technologies (MySQL counts partly toward PostgreSQL)
  and calibration questions.
- When the user names something not in the catalog, Claude writes questions on the spot and adds them to the catalog,
  so the next user gets the same questions.
- Aliases and related technologies matter more than the questions - without them matching against offers is not reliable.

**3. Fill most of the profile from a CV first.**
Claude extracts technologies and years from a pasted CV / LinkedIn text, and the interview only covers what is missing.

**4. Ask more when an offer needs it.**
15 technologies x 10 questions = 150 questions, people will give up. Do a short first pass, then ask about missing
must-haves when an offer needs them and save the answer.

**5. Store the profile as a table.**

| Technology | Category | Level (0-4) | Years | Last used | Context | Wants to use | Notes |
|---|---|---|---|---|---|---|---|
| Spring Boot | Backend | 3 | 5 | 2026 | prod | yes | REST, JPA, Security; no WebFlux |

Easy to read and edit, uses little context, a must-have can be compared against a level directly.
Soft skills and preferences go into a separate section.

---

## Follow-up question

Yes, I have an idea about exactly that type of questions - like "did You implement your own spring boot starter
module ?" and similar questions.

- One more idea - write instruction that if you see something that might not be clear from the offer based on
  obtained knowledge - ask user that question and save his skill, might be used in next offer.

## Claude answer

Implemented:

- `templates/technologies.md` - catalog of ~25 common technologies with aliases, related technologies and 4-6 yes/no
  questions tagged L1-L4, for example `[L4] Did You implement Your own Spring Boot starter / auto-configuration module ?`
  - Level = highest level answered "yes", with at least one "yes" on every lower level.
  - Unknown technologies get generated questions in the same style, appended under *Added by agent*.
- `templates/candidate-profile.md` - profile template: technologies table, answers per question,
  *Learned from offers* log, preferences using role and responsibilities tables from `templates/constants.md`.
- `.claude/skills/interview/SKILL.md` - optional CV bootstrap, one numbered message per technology
  (short answers like `1: 5y 2: prod 3: y 4: n`), saves after each technology, `done` / `skip` to stop.
- `.claude/skills/rate-offer/SKILL.md` - **Clarification** section: when the offer asks for something the profile
  does not cover (new technology, narrower sub-skill like WebFlux or Kafka Streams, higher level than recorded,
  domain requirement), Claude asks up to 7 yes/no questions in one message before rating. Answers are saved to the
  profile and *Learned from offers* log so they are not asked again; generally useful questions are added to the catalog.
- `CLAUDE.md` - points Claude to these files; a pasted offer is handled as `/rate-offer`.
- `.gitignore` - ignores `profile/` (personal data) and `.idea/`.

Notes:
- Catalog leans toward backend / Java - add technologies target users work with.
- Restart Claude Code if `/interview` or `/rate-offer` does not show up, then test with own profile.

---

## Follow-up question

Starting new conversation will not delete context and burn more tokens ? I wanted clear like in Linux terminal,
just scrape text.

## Claude answer

- **Ctrl+L** clears the screen like `clear` in Linux - conversation and context stay, token cost does not change.
- **`/clear`** removes the conversation from context, so following messages use **fewer** tokens (history is not sent
  again). Files stay on disk and a new session reads `CLAUDE.md` automatically.

---

## Follow-up question

At the beginning ask the user for his CV, LinkedIn profile (if you can read it) or other source of data.

- If user has some other tech skills not mentioned here and not prepared in questions table, fill it like later
  during offers reviewing.

## Claude answer

Implemented in `.claude/skills/interview/SKILL.md`, section *Bootstrap from candidate sources* - always the first step:

- CV - file path (PDF, DOCX, MD, TXT) or pasted text
- LinkedIn - usually blocked without login, Claude tries URL and falls back to PDF export
  (profile -> *More* -> *Save to PDF*) or pasted text
- GitHub / GitLab - public repositories, languages, dependency files (`pom.xml`, `package.json`, ...), README files
- portfolio, certificates, older job descriptions, or `skip`

Technologies from sources missing in the catalog get 4-6 generated questions, are appended under *Added by agent*
in `templates/technologies.md` and are marked `new` in the extracted list. `CLAUDE.md` now starts `/interview`
automatically when no profile exists.

---

## Follow-up question

Write short user manual to README.md what is this agent capable of yet, for example:

- user will input CV
- I will have few questions to get his tech level
  - the best ones are those where user only clicks Y/n like in Linux or MS-DOS times
- done, show me the offer
  - if something is unclear -> questions
- then results presenting (will be specified in assignment more)

## Claude answer

Added *User manual* section to `README.md` with these 4 steps (sources, questions, offer, results).

Also fixed references: app description (summary, rating, red flags) is in `assignments/task1.md`, not `README.md`,
so `CLAUDE.md` and the rate-offer skill now point there.

---

## Follow-up question

Yes, switch to clickable Y/n questions.

## Claude answer

Both skills now use Claude Code's built-in `AskUserQuestion` tool:

- calibration questions are `Yes` / `No` buttons, question text ends with `[Y/n]`
- common questions are clickable options too:
  - Years: `<1` / `1-3` / `3-5` / `5+`
  - Last used: `Now` / `1-2 years ago` / `3+ years ago`
  - Context: `Production` / `Side project` / `Course / school`
  - Wants to use: `Yes` / `Neutral` / `No`
- max 4 questions per screen, so one technology takes 2-3 screens; common questions known from sources are skipped
- `skip` / `done` are typed into the *Other* field
- fallback to typed answers (`1: y 2: n`) when the tool is not available
- offer review: max 2 screens of 4 questions (8 per offer, was 7)
- `README.md` steps 2 and 3 describe clicking instead of typing

Note: the interview description earlier in this file (one numbered message per technology, typed answers) is replaced
by the clickable flow above.

---

## Follow-up question

Now let's talk about that tables - do you have any ideas what can be filled there or what might be missing ?

## Claude answer

**Role competence complexity table**
- It mixes two scales: technical breadth (single / with overlap / multirole / full-fullstack) and non-technical load
  (none / domain / product + sales / management). Splitting into two columns makes matching clearer; `Founder` is
  maximum on both.
- `multirole` and `full-fullstack` overlap - multirole = deep in 2 fields, full-fullstack = all fields including ops.
- Missing roles: tech lead, architect, people manager / team lead, consultant / presales.
- Seniority (junior / medior / senior / lead) is missing entirely.

**Responsibilities merge table**
- `design API` fits better in `Extened` than `Bare`.
- Missing: code review / mentoring, planning, operations (daytime, unlike on call), legacy maintenance, hiring,
  people management, onsite / travel, security / compliance.
- Split `bodyshop` into one agency vs. chain of agencies.
- Add column `possible red flag (y/n)`.

**Missing tables**
1. Red flags / phrase decoder (phrases + inconsistency rules)
2. Company type (product, software house, agency, bodyshop, startup, corporate, public sector)
3. Salary normalization (survival / expected / walk-away minimum, IČO MD rate -> HPP monthly equivalent)

**Missing in candidate profile**
- domain experience, languages (CEFR), leadership experience
- preference weights (`deal-breaker` / `important` / `don't care`)
- company size, team size, notice period, legacy tolerance, travel

Recommended first: preference weights, red flag table, seniority.

---

## Follow-up question

Yes, add those three first.

## Claude answer

- `templates/constants.md` - *Seniority table* (junior / medior / senior / lead with years, autonomy, scope, offer
  signals; autonomy and scope decide, years are orientation) and *Red flags table* (phrases with meaning, severity
  `info` / `warning` / `alert` and interview question; inconsistency rules like title vs. requirements, švarcsystém).
- `templates/candidate-profile.md` - *Seniority* section (self-assessed / agent estimate / target) and *Preferences*
  as table: preference | how to ask | value | weight. Survival minimum salary is always `deal-breaker`.
- Interview asks seniority and every preference with its weight as clickable options.
- Offer review determines offer seniority from requirements, checks red flags, marks violated deal-breaker as
  **NOT SUITABLE**, unknown preferences are not counted as violated.

---

## Follow-up question

I am proud of that red flag table - I guess there is more than that, what else might be there ? What about
"Fruits in office" or "Free coffee" ? "Beer after work", "Playing games together".

Let's find a lot more of them - I found especially juniors that come from bad jobs and "famine holes" on
countryside do not spot that red flags, and that hurts market and morals in the field for all of us.

## Claude answer

Red flag table grew from ~23 to ~80 entries, new sections in `templates/constants.md`:

- **Phrases** (+18): "work hard, play hard", "young dynamic team", "stress resistance" (*odolnost vůči stresu*,
  `alert`), "flexibility", "loyalty", "not a 9-5 job", "go the extra mile", "salary based on performance", ...
- **Perks instead of benefits**: perks are fine themselves, red flag when they replace real benefits (money, time,
  security). Fruit / coffee `info`, beer after work `warning` (pressure to stay, drinking culture), games `info`,
  pizza Fridays / free dinner `warning` (people stay late).
- **Contract and money**: part of salary in cash, minimum wage + bonuses, DPP/DPČ for full time, unpaid trial day
  (illegal in CZ), overtime included in salary, training repayment, non-compete, own laptop.
- **Junior traps**: only developer, "also help with printers", paid academies, multi-day test assignments,
  unpaid internships.
- **Hiring process**: any payment from candidate = scam, ID copy before contract, >4 rounds, 24h pressure.
- **Inconsistency rules** (+7): only perks no salary, "cutting-edge" with Java 8, Extended responsibilities with
  junior title, salary range wider than 2x, offer reposted for months.
- Czech phrases are matched too; more `info` flags together raise severity.
- `/rate-offer` explains every flag in plain words when candidate target level is junior.

Notes: CZ legal points kept general - verify against current *zákoník práce* (changed in 2025). "Reposted for months"
needs a history of rated offers, which does not exist yet.

---

## Follow-up question

OK, I added something about rating in task1, can you place it where needed ?

## Claude answer

New *Scoring* section in `.claude/skills/rate-offer/SKILL.md` following `assignments/task1.md`: skill match
= 1 point, preference met = 1 point, red flag = -1, total = (skills + preferences - red flags) / max points in %.
Output uses the results table from `task1.md`.

Open decisions: partial matches, unmentioned preferences (not counted, not even into maximum), red flag severity,
weights `important` / `nice` no longer change the score, total min 0 %.

## Follow-up question

Partial 0.5, red flags by severity.

## Claude answer

- Partial match (one level below required or related technology) = 0.5 point.
- Red flags: `info` = 0, `warning` = -1, `alert` = -2; info flags are still listed.

---

## Follow-up question

Yes, update it (`task1.md`), I also finished that presentation instructions.

## Claude answer

- `assignments/task1.md` - scoring lines updated (partial 0.5, red flags by severity).
- `/rate-offer` output order:
  1. Summary including offer seniority vs. candidate target level
  2. Requirement table (required level, candidate level, match)
  3. Statistics table with rows from `task1.md`, percentage and points (`75 % (6 / 8)`); *missed* = max - gained
  4. Findings table: finding | category | severity | detail
     - missing skill: `required` / `optional`, required vs. candidate level
     - missing requirement (preference): weight as severity, margin as detail (`salary 10 000 CZK below expected`)
     - red flag: `info` / `warning` / `alert`, interview question as detail
  5. Final verdict: **NOT SUITABLE** with violated deal-breaker, or **SUITABLE** with total % and main thing to verify
- Deal-breaker warning moved from top to the verdict at the end, as in `task1.md`.
- Profile weights `important` / `nice`: 1 point when met, used as severity when missed.
