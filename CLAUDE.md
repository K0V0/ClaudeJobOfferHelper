# ClaudeJobOfferHelper

App purpose and expected output are described in `assignments/task1.md`, user manual in `README.md`.

- Candidate knowledge lives in `profile/candidate-profile.md` (created from `templates/candidate-profile.md`).
- Technology catalog with calibration questions: `templates/technologies.md`.
- Static tables for rating: `templates/constants.md`.
- `/interview` - fill or update candidate profile.
- `/rate-offer` - summarize and rate offer, ask about unclear skills and save answers to profile.
- If candidate pastes a job offer without command, follow `/rate-offer`.
- If profile does not exist on first message, start `/interview` - it begins by asking for CV, LinkedIn or other sources.
