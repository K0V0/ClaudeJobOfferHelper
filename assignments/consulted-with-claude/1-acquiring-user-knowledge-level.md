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
