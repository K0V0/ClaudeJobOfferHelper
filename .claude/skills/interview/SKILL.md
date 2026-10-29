---
name: interview
description: Interview the candidate about technologies, skills and preferences and save answers into profile/candidate-profile.md. Use when candidate runs the app first time, wants to add a technology, or says profile is outdated.
argument-hint: "[technology to add or update | stories]"
---

# Candidate interview

Goal is to fill `profile/candidate-profile.md` with comparable knowledge levels, using as few questions as possible.

## Before start

1. If `profile/candidate-profile.md` does not exist, copy `templates/candidate-profile.md` there.
2. Read the profile and `templates/technologies.md`.
3. If argument with technology was given, go straight to *Technology questions* for that technology only.
   If argument is `stories`, go straight to *Strengths and stories*.

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
2. Technologies not in `templates/technologies.md` handle the same way as during offer review:
   write 4-6 calibration questions in catalog style, append the technology to *Added by agent* section
   and ask the questions in *Technology questions* like for any other technology.
3. Show extracted list (mark newly added catalog entries as `new`) and ask candidate to add missing
   or remove wrong items.

Without any source ask: "Which technologies, languages and tools do You use ? List them all, comma separated."

## Technology questions

Go one technology at a time, most used first.

1. Find the technology in catalog by name or alias. If one name matches more entries
   (for example "Spring" + "Hibernate"), ask both.
2. If it is not in catalog, write 4-6 questions in the same style (yes/no, "Did You ...", level tags L1-L4,
   concrete practical experience, not theory), and append the technology to *Added by agent* section
   of `templates/technologies.md`.
3. Ask with `AskUserQuestion` tool so candidate only clicks. One call takes max 4 questions,
   so one technology needs 2-3 calls. Put technology name into `header` (max 12 chars, e.g. `Spring Boot`).
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
4. Compute level: highest level with a *yes*, where every lower level has at least one *yes*.
   If answers are inconsistent (yes on L4, no on L2), ask one short follow-up.
5. Write immediately after each technology, do not wait to the end:
   - row into *Technologies* table (update existing row, do not duplicate)
   - answered questions into *Skill details*
6. After the technology tell candidate in one line what was saved, for example
   `Spring Boot - level 3, 5 years, prod. Saved.`

## Preferences

After technologies, fill *Seniority* and *Preferences* sections of profile with `AskUserQuestion`.

- Seniority: ask self-assessed and target level with options from *Seniority table* in
  `templates/constants.md`. Write own estimate from sources and calibration answers next to it.
  If they differ by more than one level, tell candidate why.
- Preferences: follow *How to ask* column. Use *Role competence complexity table* and
  *Responsibilities merge table* as options (multi select) so candidate can pick.
- After every preference value ask its weight: `Deal-breaker` / `Important` / `Nice` / `Don't care`.
  Ask value and weight in the same call where possible. Survival minimum salary is always `deal-breaker`.

## Strengths and stories

After preferences, or alone when argument is `stories`. Goal is material for *why hire me* answers
and for soft *must haves* in offers (ownership, maintainability, sharing knowledge, learning), written
for a non-technical reader. Fill *Strengths and stories* section of profile.

1. Prefill: from sources, *Skill details*, writing samples and earlier letters propose 3-6 candidate
   stories (what happened, where). Do not invent results, leave them empty.
2. Ask with `AskUserQuestion`, one call:
   - `Strengths` (multi select, candidate picks max 3) - what colleagues come to You for, or what You do
     better than others. Options: 4 most likely from profile, for example `Owning work end to end`,
     `Long-term maintainable code`, `Automating manual work`, `Bridging dev and ops`, `Explaining and sharing
     knowledge`, `Learning new tech fast`, `Debugging hard problems`. *Other* for own words.
   - `Stories` (multi select) - which prefilled stories are real and can be told in a letter.
   - `Motivation` (multi select) - why candidate is looking now, options from profile and preferences,
     for example `Back to Java backend`, `Room to grow`, `Better pay`, `Stability`, `Product / domain`.
   - `Avoid` (single select) - is there something letters must never mention (reason for leaving, gap,
     NDA project) ? `No` / `Yes, I will write it`.
3. Then one plain numbered message, free text, answered briefly. For every picked story ask:
   - what was the problem or starting state
   - what did You do Yourself (not the team)
   - what changed after: number, time saved, who used it, what stopped breaking. `don't know` is ok
   Also ask: the result You are most proud of; what a colleague or manager praised You for;
   what You do that other candidates on Your level usually do not; and the *Avoid* detail if `Yes`.
4. Write a story only with facts candidate gave or confirmed. Missing result stays empty, mark `unsure`
   if candidate guessed. Map every story to strengths and to offer phrases it proves
   (Czech and English, for example `ownership`, `dotahování do konce`).
5. Ask max 3 stories in first run. Candidate can add more later with `/interview stories`.

## Keeping it short

- Do not ask questions already answered in profile, unless candidate asks to update.
- If candidate answers vaguely, save best guess and mark it in *Notes* as `unsure`, do not insist.
- At the start of interview, and whenever candidate seems tired, tell how to stop:
  "Type `done` into *Other* to finish, `skip` to skip this technology. You can continue later with `/interview`."
- When finished, print short summary table and tell that offers can be rated with `/rate-offer`.
