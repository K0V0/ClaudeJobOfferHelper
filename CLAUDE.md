# ClaudeJobOfferHelper

Claude Code plugin `job-offer-helper`. This file is for developing it, plugins do not load their `CLAUDE.md`, so every
rule candidates need must be in `skills/` or `templates/`. Test with `claude plugin validate .` and `claude --plugin-dir .`.

App purpose and expected output are described in `assignments/task1.md` and `assignments/task2.md`, user manual in `README.md`.

- Plugin root is replaced on every update, so skills read it through `${CLAUDE_PLUGIN_ROOT}` and never write there.
- Candidate data lives in `~/JobOfferHelper/`: `candidate-profile.md` (created from `templates/candidate-profile.md`),
  `offer-results/`, `writing-samples/`, `technologies-added.md`, `portals/`.
- Technology catalog with calibration questions: `templates/technologies.md`, grown per candidate in `technologies-added.md`.
- Static tables for rating: `templates/constants.md`.
- Cover letter rules, tone and ATS tables: `templates/cover-letter.md`.
- `/job-offer-helper:interview` - fill or update candidate profile.
- `/job-offer-helper:rate-offer` - summarize and rate offer, ask about unclear skills and save answers to profile.
- Everything about one offer lives in `~/JobOfferHelper/offer-results/<yyyy-mm-dd>-<company>-<position>/` - offer text,
  ratings, cover letters. See *Offer folder* in `skills/rate-offer/SKILL.md`. Never overwrite a rating or letter there, add a new file.
- `bin/save-offer` runs `scripts/save_offer.py` - saves offer from URL word for word and as PDF, one extractor per portal
  in `scripts/<portal>/`, candidate's own ones in `~/JobOfferHelper/portals/<portal>/`.
- `/job-offer-helper:cover-letter` - write cover letter or answer to application question in candidate style, normal and ATS version.
- Never use `—` or `–` in any text written for the candidate to send.
