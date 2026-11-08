---
name: interview
description: Interview the candidate about technologies, skills and preferences and save answers into candidate profile. Use when candidate runs the app first time, wants to add a technology, or says profile is outdated.
argument-hint: "[technology to add or update]"
allowed-tools: Read(~/.claude/plugins/**) Read(~/JobOfferHelper/**) Edit(~/JobOfferHelper/**)
---

# Candidate interview

Goal is to fill `~/JobOfferHelper/candidate-profile.md` with comparable knowledge levels, using as few questions as possible.

## Data folder

Everything about the candidate lives in `~/JobOfferHelper/` in the home directory of candidate (on Windows
`C:\Users\<name>\JobOfferHelper`). Use the full path with file tools and create the folder when it is missing.
Never write into `${CLAUDE_PLUGIN_ROOT}`, the plugin folder is replaced on every update.

## Before start

1. If `~/JobOfferHelper/candidate-profile.md` does not exist, copy `${CLAUDE_PLUGIN_ROOT}/templates/candidate-profile.md` there.
2. Read the profile and the catalog: `${CLAUDE_PLUGIN_ROOT}/templates/technologies.md` and, when it exists, `~/JobOfferHelper/technologies-added.md`.
3. If argument with technology was given, go straight to *Technology questions* for that technology only.

## Bootstrap from candidate sources

Always start with this, before any technology question. Ask in one message for any of these, more is better:

- CV - path to file in project or on disk (PDF, DOCX, MD, TXT) or pasted text
- LinkedIn profile - LinkedIn usually blocks reading without login, so ask for PDF export
  (profile -> *More* -> *Save to PDF*) or pasted text. If URL is given, try to fetch it, and if it fails,
  ask for the export.
- GitHub / GitLab profile or repositories - fetch public profile and repositories, read languages,
  dependencies (`pom.xml`, `build.gradle`, `package.json`, ...) and README files
- portfolio, personal web, certificates, older job descriptions or any other text
- `skip` - no sources, go to questions directly

From the sources:

1. Extract technologies, years and last usage, roles, domains and preferences. Prefill those columns,
   but still ask calibration questions - sources do not tell the level.
2. Technologies not in catalog handle the same way as during offer review:
   decide its Tier (see *Tier* in catalog), write calibration questions in catalog style (8-10 for core,
   4-6 for adjacent), append the technology to `~/JobOfferHelper/technologies-added.md` and ask the questions
   in *Technology questions* like for any other technology.
3. Show extracted list (mark newly added catalog entries as `new`) and ask candidate to add missing
   or remove wrong items.

Without any source ask: "Which technologies, languages and tools do You use ? List them all, comma separated."

## Job target

Right after sources, before technology questions. Skip if *Job target* in profile is already filled,
unless candidate asks to update it. Ask with `AskUserQuestion`, one call:

- `Field` (multi select) - "Which field do You want to work in ? Pick more for full stack."
  Options: `Backend`, `Frontend`, `DevOps`.
- `Core stack` (single select) - "What is Your main stack for that job ?" Options: up to 4 most likely
  stacks from sources (for example `Java + Spring Boot`, `TypeScript + Angular`, `Kubernetes + AWS`),
  *Other* for own words.
- `Level` (single select) - "Which level of positions are You applying for ?"
  Options: `Junior`, `Medior`, `Senior`, `Lead`.

Save to *Job target*:

- fields as picked, and role complexity from *Job target field to complexity* in `${CLAUDE_PLUGIN_ROOT}/templates/constants.md`
  (backend + frontend = full stack = `mutlirole`, all three = full-fullstack). Copy complexity also into
  *Preferred role complexity* value in *Preferences*, its weight is asked later in *Preferences*.
- core stack and target level as answered.

Job target never changes which calibration questions are asked, and never changes level estimated by agent.
Candidate may target a lower level than their own on purpose (less stress, slowing down), do not argue about it.
Tell candidate in one line, for example `Target: backend, single, Java + Spring Boot, medior. Saved.`

## Technology questions

Go one technology at a time, most used first.

1. Find the technology in catalog by name or alias. If one name matches more entries
   (for example "Spring" + "Hibernate"), ask both.
2. If it is not in catalog, decide its Tier (see *Tier* in catalog) and write questions in the same style
   (yes/no, "Did You ...", level tags L1-L4, concrete practical experience, not theory): 8-10 for core
   with at least 2 per level, 4-6 for adjacent. Append the technology with its Tier line to
   `~/JobOfferHelper/technologies-added.md`.
3. Ask all calibration questions of the technology, always. Core technology has 8-10 of them and they are
   asked even when candidate answers *no* on lower levels - profiles must stay comparable. Tier does not
   depend on candidate *Job target*, a frontend candidate gets all 10 Kubernetes questions if they use it.
4. Ask with `AskUserQuestion` tool so candidate only clicks. One call takes max 4 questions,
   so adjacent technology needs 2-3 calls and core technology 3-4 calls. Put technology name into `header`
   (max 12 chars, e.g. `Spring Boot`). For core technology tell candidate before first call how many
   questions are coming, for example `Java - core technology, 10 questions in 3 screens.`
   - common questions first, as single select:
     - Years: `<1` / `1-3` / `3-5` / `5+`
     - Last used: `Now` / `1-2 years ago` / `3+ years ago`
     - Context: `Production` / `Side project` / `Course / school`
     - Wants to use: `Yes` / `Neutral` / `No`
   - then calibration questions, each as single select with options `Yes` / `No`, question text
     from catalog ending with `[Y/n]`
   - candidate can type `skip` or `done` into *Other* field - respect it immediately
   - skip common questions already known from sources, ask only calibration ones
   - if `AskUserQuestion` is not available, fall back to one numbered message answered like `1: y 2: n 3: y`
5. Compute level: highest level with a *yes*, where every lower level has at least one *yes*.
   If answers are inconsistent (yes on L4, no on L2), ask one short follow-up.
6. Write immediately after each technology, do not wait to the end:
   - row into *Technologies* table (update existing row, do not duplicate)
   - answered questions into *Skill details*
7. After the technology tell candidate in one line what was saved, for example
   `Spring Boot - level 3, 5 years, prod. Saved.`

## Preferences

After technologies, fill *Seniority* and *Preferences* sections of profile with `AskUserQuestion`.

- Seniority: ask self-assessed level with options from *Seniority table* in `${CLAUDE_PLUGIN_ROOT}/templates/constants.md`
  (target level is already in *Job target*). Write own estimate from sources and calibration answers
  next to it. If self-assessed and estimated level differ by more than one level, tell candidate why.
  Target level lower than estimated is a choice, only mention it, do not try to change it.
- Preferences: follow *How to ask* column. Use *Role competence complexity table* and
  *Responsibilities merge table* as options (multi select) so candidate can pick. *Preferred role complexity*
  is prefilled from *Job target*, ask only its weight and whether to add more options.
- After every preference value ask its weight: `Deal-breaker` / `Important` / `Nice` / `Don't care`.
  Ask value and weight in the same call where possible. Survival minimum salary is always `deal-breaker`.

## Keeping it short

- Do not ask questions already answered in profile, unless candidate asks to update.
- Catalog grows (for example adjacent technology became core and got more questions). When running
  `/job-offer-helper:interview` on an existing profile, ask only catalog questions missing in *Skill details* and recompute
  the level. If *Job target* is missing in an older profile, ask it first.
- If candidate answers vaguely, save best guess and mark it in *Notes* as `unsure`, do not insist.
- At the start of interview, and whenever candidate seems tired, tell how to stop:
  "Type `done` into *Other* to finish, `skip` to skip this technology. You can continue later with `/job-offer-helper:interview`."
- When finished, print short summary table and tell that offers can be rated with `/job-offer-helper:rate-offer`,
  and that `/job-offer-helper:letter-interview` collects material for cover letters.
