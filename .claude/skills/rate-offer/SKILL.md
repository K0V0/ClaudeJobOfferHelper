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
4. Run *Clarification* below before computing final rating.
5. Produce summary and rating as described in `assignments/task1.md`.

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

- Summary part from `assignments/task1.md`.
- Requirement table: requirement | must / nice | required level | candidate level | match (yes / partial / no / unknown).
- Rating: must have %, nice to have %, total %, preference match.
- Red flags and inconsistencies.
- One line listing what was newly saved to profile.
