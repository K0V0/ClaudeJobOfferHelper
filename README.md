# ClaudeJobOfferHelper
Agent to help You with process of rating job offers and applying for them

    ## User manual

Open this project in Claude Code and write anything - if You have no profile yet, interview starts automatically.

1. **Give me Your sources**
   - CV (file path or pasted text), LinkedIn PDF export, GitHub / GitLab profile, portfolio, certificates, ...
   - or `skip` and just list Your technologies
2. **Tell me what job You are looking for**
   - field (backend, frontend, devops, more of them for full stack), main stack and level You apply for
   - it only filters offers, the questions and Your estimated level stay the same, so applying for
     an easier job than You could get is fine
3. **Answer a few questions per technology**
   - core technologies of the field (Java, Spring Boot, TypeScript, Angular, SQL, Docker, Kubernetes, ...)
     get 8-10 questions, adjacent ones (Kafka, Redis, Keycloak, SharePoint, ...) get 4-6
   - just click `Yes` / `No`, like `[Y/n]` in good old Linux and MS-DOS times, for example
     `Did You implement Your own Spring Boot starter module ? [Y/n]`
   - years, context and preferences are also clickable options, up to 4 questions on one screen
   - type `skip` into *Other* to skip technology, `done` to end interview, `/interview` continues later or adds a technology
   - result is saved to `profile/candidate-profile.md` - You can read and edit it any time
4. **Show me the offer**
   - paste offer text or URL, or run `/rate-offer`
   - if offer needs something Your profile does not cover, I will ask a few clickable `Yes` / `No` questions first
     and remember answers for next offers
5. **Results**
   - offer summary, match rating, red flags and final verdict
   - saved to `profile/offer-results/<date>-<company>-<position>/` together with the original offer text and PDF of the
     offer page, so You have it even after the offer disappears from the web
   - links from jobs.cz, prace.cz, profesia.sk, startupjobs.cz and LinkedIn are read by scripts in `scripts/`,
     they need Python 3.10 or newer with `requests` and `beautifulsoup4`, and Chrome, Chromium, Edge or Brave
   - after interview or recruiter call say *rate it again* (or `/rate-offer <company>`) and tell what You learned -
     You get a new rating with changes against the old one, old rating stays
6. **Cover letter**
   - run `/cover-letter` after rating, or ask for cover letter, motivation letter or answer to application question
   - first time I ask for letters You wrote Yourself (ideally with the offers they were for), to learn Your style
   - tell me if the form asks something specific, like *Why you ?* or *How will you be useful for us ?*
   - You get two versions to compare: normal one for a human and one optimized for the ATS the company uses
   - letters are saved to the offer folder in `profile/offer-results/`, paste back Your final edited version and it becomes Your writing sample
