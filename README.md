# ClaudeJobOfferHelper
Agent to help You with process of rating job offers and applying for them

    ## User manual

### Install

You need [Claude Code](https://code.claude.com) and a paid Claude plan. Then run once:

```
claude plugin marketplace add K0V0/ClaudeJobOfferHelper
claude plugin install job-offer-helper@k0v0
```

Later versions come with `claude plugin update job-offer-helper@k0v0`.

Nothing else has to be installed, saving offers from links downloads its own small program the first time (11 to 25 MB, depending on the system).
Chrome, Chromium, Edge or Brave is needed only for the PDF of the offer page and for pages that need JavaScript.

### Your data

Everything about You stays in the folder `JobOfferHelper` in Your home directory, updates never touch it. Start Claude
Code in that folder (`mkdir -p ~/JobOfferHelper && cd ~/JobOfferHelper && claude`) so it does not ask for permission
for every file. It works from any other folder too, with more questions.

Coming from a cloned version of this app ? Move content of its `profile/` folder there.

### Usage

Run `/job-offer-helper:interview` first.

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
   - type `skip` into *Other* to skip technology, `done` to end interview, `/job-offer-helper:interview` continues later or adds a technology
   - result is saved to `~/JobOfferHelper/candidate-profile.md` - You can read and edit it any time
4. **Show me the offer**
   - paste offer text or URL, or run `/job-offer-helper:rate-offer`
   - if offer needs something Your profile does not cover, I will ask a few clickable `Yes` / `No` questions first
     and remember answers for next offers
5. **Results**
   - offer summary, match rating, red flags and final verdict
   - saved to `~/JobOfferHelper/offer-results/<date>-<company>-<position>/` together with the original offer text and PDF of the
     offer page, so You have it even after the offer disappears from the web
   - links from jobs.cz, prace.cz, profesia.sk, startupjobs.cz and LinkedIn are read by scripts, see *Install*
   - after interview or recruiter call say *rate it again* (or `/job-offer-helper:rate-offer <company>`) and tell what You learned -
     You get a new rating with changes against the old one, old rating stays
6. **Cover letter**
   - run `/job-offer-helper:letter-interview` once before first letter, it asks what the CV can not show: do You want to own a whole
     service or get clear tasks, in what team You work best, why You are looking, and a few short answers in Your own words
   - run `/job-offer-helper:cover-letter` after rating, or ask for cover letter, motivation letter or answer to application question
   - first time I ask for letters You wrote Yourself (ideally with the offers they were for), to learn Your style
   - tell me if the form asks something specific, like *Why you ?* or *How will you be useful for us ?*, and if You want the letter as prose or as bullets
   - You get two versions to compare: normal one for a human and one optimized for the ATS the company uses
   - letters are saved to the offer folder in `~/JobOfferHelper/offer-results/`, paste back Your final edited version and it becomes Your writing sample
