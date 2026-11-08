---
name: rate-offer
description: Summarize and rate a job offer against candidate profile, ask candidate about unclear skills and save answers for next offers. Use when candidate pastes a job offer or a link to one.
argument-hint: "[offer text, URL, or company / offer folder to reevaluate]"
allowed-tools: Read(~/.claude/plugins/**) Read(~/JobOfferHelper/**) Edit(~/JobOfferHelper/**) Bash(save-offer *)
---

# Rate job offer

## Data folder

Everything about the candidate lives in `~/JobOfferHelper/` in the home directory of candidate (on Windows
`C:\Users\<name>\JobOfferHelper`). Use the full path with file tools and create the folder when it is missing.
Never write into `${CLAUDE_PLUGIN_ROOT}`, the plugin folder is replaced on every update.

## Inputs

- Offer text or URL. URL is saved by script and rated from the saved `offer.md`, see *Saving the offer*.
  If nothing given, ask candidate to paste the offer.
- Existing offer folder in `~/JobOfferHelper/offer-results/` (see *Offer folder*) - if this offer was rated before,
  this is a *Reevaluation*.
- `~/JobOfferHelper/candidate-profile.md` - if missing, tell candidate to run `/job-offer-helper:interview` first, but offer
  to continue with only questions needed for this offer.
- `${CLAUDE_PLUGIN_ROOT}/templates/technologies.md` and, when it exists, `~/JobOfferHelper/technologies-added.md` (together the *catalog*) -
  aliases, related technologies, levels.
- `${CLAUDE_PLUGIN_ROOT}/templates/constants.md` - role complexity and responsibilities tables.
- `${CLAUDE_PLUGIN_ROOT}/assignments/task1.md` - required parts of summary and rating.

## Steps

1. Extract requirements from offer and split them to *must have* and *nice to have*.
   Estimate required level 0-4 for each from wording (years, "senior", "expert", "basic knowledge", ...).
2. Normalize names using catalog aliases.
3. Match every requirement against profile:
   - exact technology in profile - use its level
   - only related technology in profile - one level lower, max level 2, mark as `related`
   - nothing in profile - **unclear**
4. Determine offer seniority using *Seniority table* in `${CLAUDE_PLUGIN_ROOT}/templates/constants.md` - from responsibilities
   and requirements, not only from title. Compare with candidate target level from *Job target*.
   Also determine offer field(s) (backend / frontend / devops) and core stack from its *core* requirements
   (Tier in catalog) and compare with *Job target* fields and core stack. This is informative only,
   scoring of role fit stays in *Preferred role complexity* preference.
5. Check offer against all sections of *Red flags table*. Posting date only from what the page states
   (text or structured data), never decoded from offer IDs or URLs - those are guesses. If candidate target level is *junior*, explain
   every red flag in plain words: what it means in practice and why accepting it hurts candidate and market.
6. Check preferences: any violated `deal-breaker` marks offer as **not suitable**.
   If offer does not say anything about a preference, count it as unknown, not as violated.
7. Run *Clarification* below before computing final rating.
8. Compute points as described in *Scoring* below.
9. Produce summary and rating as described in `${CLAUDE_PLUGIN_ROOT}/assignments/task1.md`.

## Offer folder

Every rated offer has its own folder, shared with `/job-offer-helper:cover-letter`:

```
~/JobOfferHelper/offer-results/<yyyy-mm-dd>-<company>-<position>/
  offer.md                       offer link and original text, word for word
  offer-page.pdf                 printed offer page
  rating-<yyyy-mm-dd>.md         one file per rating, the first one and every reevaluation
  cover-letter-<yyyy-mm-dd>.md   one file per generated letter (written by /job-offer-helper:cover-letter)
```

- Folder name: date of the first rating, company and position as lowercase slug, for example
  `2026-11-03-teamit-java-developer`. Recruiting agency with known end client: `<agency>-<client>-<position>`.
- Find existing folder by offer URL in `offer.md` first, then by company and position (ignore the date).
  If unsure whether it is the same offer, ask candidate.
- Never overwrite `rating-*.md` or `cover-letter-*.md`. Second file on the same day gets suffix `-2`, `-3`.
- `offer.md` is written once. If the offer text changed since (new salary, changed requirements), save the new
  text as `offer-<yyyy-mm-dd>.md` next to it. Printed page of changed offer is `offer-page-<yyyy-mm-dd>.pdf`.
- Rating file contains: offer title and link, date, `Type: first rating` or `Type: reevaluation of <previous file>`,
  then everything from *Output* below, as shown to candidate, plus the clarifications asked and answered for this offer.
- Batch overviews of many offers stay in `~/JobOfferHelper/offer-batches/`. When an offer from a batch gets a full rating,
  it gets its own folder.

### Saving the offer

Offers disappear from the web, so the original is saved before rating. `offer.md` is the original word for word,
never summarized, shortened, translated or retyped from memory.

- URL: run `save-offer <url>` (add `--folder <path>` if the folder is already known). It finds the
  folder by link or creates a new one, writes `offer.md` and `offer-page.pdf`, and prints their names. Then read `offer.md`.
  Do not fetch the URL or read page source yourself, that is what the script saves tokens on.
  First run downloads the prebuilt script, so it takes a bit longer. In PowerShell the command is
  `powershell -NoProfile -ExecutionPolicy Bypass -File "${CLAUDE_PLUGIN_ROOT}/bin/save-offer.ps1" '<url>'`.
- Recruiting agency with known end client: rename the created folder as described above.
- Script prints `extractor: generic` (portal without own extractor): check that `offer.md` really is the offer. If it is
  not, or the portal comes back often, look at the page once and add `~/JobOfferHelper/portals/<portal>/extract.py` with `HOSTS` and
  `extract(soup)`, `${CLAUDE_PLUGIN_ROOT}/scripts/<portal>/` has examples. Portal folder name is its domain with `_`, for example `jobs_cz`.
- Script fails (exit code 2 or 3, nothing written, or Python libraries are missing), `pdf: failed`, or candidate pasted the text: ask candidate to paste the full
  offer if it is not pasted yet and write it to `offer.md` unchanged: `# <title>`, `- Link: <url>`, `- Saved: <date>`,
  `## Original text`, then the text. With a URL also try `save-offer <url> --folder <path> --pdf-only`.
  Tell candidate in one line when there is no PDF.

## Reevaluation

Offer is rated again, usually after an interview or recruiter call. Triggered when candidate asks for it
(`/job-offer-helper:rate-offer <company>`, "rate it again", "after interview ...") or pastes an offer that already has a folder.

1. Read the latest `rating-*.md` and `offer.md` of the offer. Tell candidate in one line when it was rated
   and with what result, for example `Rated 2026-11-03: 58 % BORDERLINE.`
2. Ask what is new, with `AskUserQuestion` where possible: answers to interview questions from the findings
   (salary range, work mode, end client, team, on call, ...), new or changed requirements, changed candidate preferences.
   *Other* for free text. Do not ask what candidate already told in this conversation.
3. Rate again with all *Steps*, using the new facts:
   - a red flag answered well on interview is listed as `resolved` with the answer and gives no minus points,
     answered badly keeps or raises its severity
   - unknown preference that is now known is counted, met or violated
   - new facts about candidate skills go to profile as usual (*Learned from offers*)
4. Write a new `rating-<yyyy-mm-dd>.md`, never change the old one. Add a section *Changes since previous rating*:
   previous and new total and verdict, and a table: item | before | now | source (interview, recruiter, new offer text).
5. In *Output* show *Changes since previous rating* right after the statistics table.

## Scoring

Points as defined in *Rating offer* in `${CLAUDE_PLUGIN_ROOT}/assignments/task1.md`:

- Hard skills: every requirement where candidate level >= required level = 1 point.
  `partial` (one level below required) and `related` = 0.5 point, `no` and `unknown` = 0.
  Count separately for must have, nice to have and total.
- Preferences: every met preference = 1 point. Preferences with weight `don't care` and preferences
  the offer says nothing about are not counted, not even into maximum.
- Red flags by severity: `info` = 0, `warning` = -1, `alert` = -2 points.
  `info` flags are still listed in output, they only do not lower the score.
- Missing *must have* (`no` or `unknown`) = -2 points on top of the 0 points, same weight as `alert`.
  Partial and related *must have* get no penalty. Missing *nice to have* gets no penalty.
- Total = (hard skill points + preference points - red flags - missing must haves) / (max hard skill points + max preference points), in %.
  Total can not go below 0 %.

## Clarification

Ask candidate when profile can not answer what offer requires. Typical cases:

- technology from offer is not in profile at all
- offer asks for specific sub-skill not covered by *Skill details*, for example offer wants
  "Spring WebFlux", "event sourcing", "Kafka Streams" and profile has only general level
- offer requires higher level or more years than profile shows and *Notes* are `unsure`
- domain or soft skill requirement (banking, team lead, customer communication) not in *Preferences*

Rules:

- Ask clarifications with `AskUserQuestion` tool, same way as in `/job-offer-helper:interview`: single select `Yes` / `No`
  for yes/no questions, option lists for years, context and preferences. Max 4 questions per call,
  max 2 calls per offer (8 questions). Prioritise *must have* requirements. `header` names the requirement.
- Unknown technology - ask the common questions plus its calibration questions (create them in `~/JobOfferHelper/technologies-added.md`
  if missing, with Tier and question count as in `/job-offer-helper:interview`). Core technology has 8-10 questions, which
  can exceed the 8 question limit per offer: then ask the must have core technology fully and leave other
  unclear requirements `unknown`, offering `/job-offer-helper:interview <technology>` for them.
- Candidate can type `skip` into *Other* - then treat requirement as not met and mark it `unknown`.
- If `AskUserQuestion` is not available, ask in one numbered message answered like `1: y 2: n`.
- Save every answer before writing the rating:
  - new or changed technology - update *Technologies* table and *Skill details*
  - new question that is useful for other candidates - append it under the name of that technology in
    `~/JobOfferHelper/technologies-added.md` with proper level tag
  - always add one row into *Learned from offers* (date, company / position, question, answer, where saved)
- Never ask again what is already in *Learned from offers* or *Skill details*.

## Output

Follow *Calculation and results presentation* in `${CLAUDE_PLUGIN_ROOT}/assignments/task1.md`, in this order:

1. Summary part from `${CLAUDE_PLUGIN_ROOT}/assignments/task1.md`, including seniority: offer level vs candidate target level,
   and field: offer field and core stack vs candidate *Job target*, for example
   `backend, Java + Spring Boot (target: backend, Java + Spring Boot)`.
2. Requirement table: requirement | must / nice | required level | candidate level | match (yes / partial / no / unknown).
3. Statistics table, exactly with rows from `${CLAUDE_PLUGIN_ROOT}/assignments/task1.md`. Show points next to percentage,
   for example `75 % (6 / 8)`.
   - *Hard skills fit* shows must have, nice to have and total.
   - *missed* rows = maximum points minus gained points, so partial match counts half as missed.
   - *hard skills missed* row also shows the penalty, for example `36 % (5 / 14), 3 must have missing: -6`.
   - *total* row shows the formula, for example `43 % ((9 + 6 - 1 - 6) / 21)`.
4. Findings table: finding | category | severity | detail
   - missing skill - severity `required` (must have) or `optional` (nice to have),
     detail = required vs candidate level
   - missing requirement (preference) - severity = preference weight, detail = margin, for example
     `salary 10 000 CZK below expected`, `2 office days, wanted full remote`
   - red flag - severity `info` / `warning` / `alert`, detail = question for interview
   - sort by category, inside category from most severe
5. Final verdict - one line:
   - any violated `deal-breaker` -> **NOT SUITABLE** and which deal-breaker
   - total below 50 % -> **NOT SUITABLE**, total % and the main missing must haves
   - total 50-69 % -> **BORDERLINE**, total % and what decides it (usually missing must haves to ask about)
   - total 70 % and more -> **SUITABLE**, total % and the most important finding to verify on interview
6. One line listing what was newly saved to profile, and the path of the saved rating file
   (see *Offer folder*). Save it before showing the output.
7. If verdict is **SUITABLE** or **BORDERLINE**, offer `/job-offer-helper:cover-letter` for this offer.
