# ClaudeJobOfferHelper
Agent to help You with process of rating job offers and applying for them

    ## User manual

Open this project in Claude Code and write anything - if You have no profile yet, interview starts automatically.

1. **Give me Your sources**
   - CV (file path or pasted text), LinkedIn PDF export, GitHub / GitLab profile, portfolio, certificates, ...
   - or `skip` and just list Your technologies
2. **Answer a few questions per technology**
   - just click `Yes` / `No`, like `[Y/n]` in good old Linux and MS-DOS times, for example
     `Did You implement Your own Spring Boot starter module ? [Y/n]`
   - years, context and preferences are also clickable options, up to 4 questions on one screen
   - type `skip` into *Other* to skip technology, `done` to end interview, `/interview` continues later or adds a technology
   - result is saved to `profile/candidate-profile.md` - You can read and edit it any time
3. **Show me the offer**
   - paste offer text or URL, or run `/rate-offer`
   - if offer needs something Your profile does not cover, I will ask a few clickable `Yes` / `No` questions first
     and remember answers for next offers
4. **Results**
   - offer summary, match rating and red flags (format will be specified in assignments)
