---
name: rate-offer
description: Summarize and rate a job offer against candidate profile, ask candidate about unclear skills and save answers for next offers. Use when candidate pastes a job offer or a link to one.
argument-hint: "[offer text or URL]"
---

# Rate job offer

## Inputs

- Offer text or URL (fetch it if URL is given). If nothing given, ask candidate to paste the offer.
- `profile/candidate-profile.md` - if missing, tell candidate to run `/interview` first, but offer
  to continue with only questions needed for this offer.
- `templates/technologies.md` - aliases, related technologies, levels.
- `templates/constants.md` - role complexity and responsibilities tables.
- `assignments/task1.md` - required parts of summary and rating.

## Steps

1. Extract requirements from offer and split them to *must have* and *nice to have*.
   Estimate required level 0-4 for each from wording (years, "senior", "expert", "basic knowledge", ...).
2. Normalize names using catalog aliases.
3. Match every requirement against profile:
   - exact technology in profile - use its level
   - only related technology in profile - one level lower, max level 2, mark as `related`
   - nothing in profile - **unclear**
4. Determine offer seniority using *Seniority table* in `templates/constants.md` - from responsibilities
   and requirements, not only from title. Compare with candidate target level.
5. Check offer against all sections of *Red flags table*. Posting date only from what the page states
   (text or structured data), never decoded from offer IDs or URLs - those are guesses. If candidate target level is *junior*, explain
   every red flag in plain words: what it means in practice and why accepting it hurts candidate and market.
6. Check preferences: any violated `deal-breaker` marks offer as **not suitable**.
   If offer does not say anything about a preference, count it as unknown, not as violated.
7. Run *Clarification* below before computing final rating.
8. Compute points as described in *Scoring* below.
9. Produce summary and rating as described in `assignments/task1.md`.

## Scoring

Points as defined in *Rating offer* in `assignments/task1.md`:

- Hard skills: every requirement where candidate level >= required level = 1 point.
  `partial` (one level below required) and `related` = 0.5 point, `no` and `unknown` = 0.
  Count separately for must have, nice to have and total.
- Preferences: every met preference = 1 point. Preferences with weight `don't care` and preferences
  the offer says nothing about are not counted, not even into maximum.
- Red flags by severity: `info` = 0, `warning` = -1, `alert` = -2 points.
  `info` flags are still listed in output, they only do not lower the score.
- Total = (hard skill points + preference points - red flags) / (max hard skill points + max preference points), in %.
  Total can not go below 0 %.

## Clarification

Ask candidate when profile can not answer what offer requires. Typical cases:

- technology from offer is not in profile at all
- offer asks for specific sub-skill not covered by *Skill details*, for example offer wants
  "Spring WebFlux", "event sourcing", "Kafka Streams" and profile has only general level
- offer requires higher level or more years than profile shows and *Notes* are `unsure`
- domain or soft skill requirement (banking, team lead, customer communication) not in *Preferences*

Rules:

- Ask clarifications with `AskUserQuestion` tool, same way as in `/interview`: single select `Yes` / `No`
  for yes/no questions, option lists for years, context and preferences. Max 4 questions per call,
  max 2 calls per offer (8 questions). Prioritise *must have* requirements. `header` names the requirement.
- Unknown technology - ask the common questions plus its calibration questions (create them in catalog
  if missing, as in `/interview`).
- Candidate can type `skip` into *Other* - then treat requirement as not met and mark it `unknown`.
- If `AskUserQuestion` is not available, ask in one numbered message answered like `1: y 2: n`.
- Save every answer before writing the rating:
  - new or changed technology - update *Technologies* table and *Skill details*
  - new question that is useful for other candidates - append it to that technology in
    `templates/technologies.md` with proper level tag
  - always add one row into *Learned from offers* (date, company / position, question, answer, where saved)
- Never ask again what is already in *Learned from offers* or *Skill details*.

## Output

Follow *Calculation and results presentation* in `assignments/task1.md`, in this order:

1. Summary part from `assignments/task1.md`, including seniority: offer level vs candidate target level.
2. Requirement table: requirement | must / nice | required level | candidate level | match (yes / partial / no / unknown).
3. Statistics table, exactly with rows from `assignments/task1.md`. Show points next to percentage,
   for example `75 % (6 / 8)`.
   - *Hard skills fit* shows must have, nice to have and total.
   - *missed* rows = maximum points minus gained points, so partial match counts half as missed.
4. Findings table: finding | category | severity | detail
   - missing skill - severity `required` (must have) or `optional` (nice to have),
     detail = required vs candidate level
   - missing requirement (preference) - severity = preference weight, detail = margin, for example
     `salary 10 000 CZK below expected`, `2 office days, wanted full remote`
   - red flag - severity `info` / `warning` / `alert`, detail = question for interview
   - sort by category, inside category from most severe
5. Final verdict - one line:
   - any violated `deal-breaker` -> **NOT SUITABLE** and which deal-breaker
   - otherwise **SUITABLE**, total % and the most important finding to verify on interview
6. One line listing what was newly saved to profile.
7. If verdict is **SUITABLE**, offer `/cover-letter` for this offer.
