# Cover letter rules

Static rules for `/cover-letter`. Candidate style learned from samples is in *Writing style* section of
`profile/candidate-profile.md` and has priority over *Tone by employer type* below.

## Punctuation and AI cliché

Recruiters recognize AI written letters by the same few habits. Avoid them always, even if candidate
uses some of them in own writing.

| habit | rule |
| ----- | ---- |
| long dash `—` and medium dash `–` | never, not even between numbers, use `-` or words (`5 to 7 years`) |
| hyphen used as sentence separator (` - `) | max 1 per letter, prefer comma, period or new sentence, even if samples use it more |
| semicolons | max 1 per letter |
| lists of exactly three (`fast, reliable and scalable`) | max 1 per letter, use two or four items, or one with an example |
| `not only X, but also Y`; `it is not X, it is Y` | never |
| every paragraph of the same length | vary paragraph and sentence length like in samples |
| bullet points and bold text in letter body | never, unless form asks for list |
| emoji, exclamation marks | never, max 1 exclamation mark for startup tone |
| opening with own name (`My name is ...`) | never, name is in signature |
| closing summary that repeats the letter | never |

### Phrases

Do not use these or their translations. Replace with concrete fact from candidate profile.

| phrase | Czech version | replace with |
| ------ | ------------- | ------------ |
| I am writing to express my interest | píši Vám, abych vyjádřil zájem | first sentence about the role or company itself |
| I am excited / thrilled to apply | s nadšením reaguji | why this role, in one concrete sentence |
| passionate about | jsem zapálený pro | what candidate did with it in free time or at work |
| proven track record; results-driven | prokazatelné výsledky | one concrete result with number or system name |
| team player; proactive; detail-oriented | týmový hráč; proaktivní; pečlivý | situation that shows it |
| fast-paced; dynamic | dynamický | nothing, skip it |
| leverage; utilize; harness | využít svých zkušeností | use, work with |
| delve; navigate the landscape; tapestry; realm | - | plain verb |
| robust; seamless; cutting-edge; innovative | robustní; inovativní | name of the technology or what it does |
| spearheaded; championed | stál jsem v čele | led, started, built |
| I believe I would be a great fit | věřím, že bych byl skvělou posilou | the match itself, let reader decide |
| in today's rapidly evolving world | v dnešní rychle se měnící době | nothing, skip it |
| I look forward to the opportunity to discuss | těším se na možnost osobního setkání | short, plain closing from samples or *Tone* table |
| Furthermore; Moreover; Additionally (at sentence start) | Navíc; Dále | nothing, or `also` inside sentence |

## Reader

First contact person is usually not technical: recruiter, HR, agency. They decide if the letter goes
further, and they can not judge `Flyway migrations` or `OpenAPI error format`. Tech details are in the CV.

| reader | what the letter should do |
| ------ | ------------------------- |
| recruiter, HR, agency (default, also when a name without a role is given) | how candidate works and what they care about, mapped to soft *must haves* of the offer (ownership, maintainability, sharing knowledge, learning), each claim with one concrete fact in plain words; technologies only as names (Java, Spring Boot, DevOps), no deep tech detail |
| CTO, tech lead, developer (only when offer or candidate says so) | technical proof is fine: systems, technologies, design decisions |

### Keep stories for interview

Do not disclose exact situations from past work projects in a letter. Those are for the next rounds,
where candidate tells them in person with context.

- Allowed: summary level facts - years, role, share of work (`90 % DevOps`), type of system or domain
  (`state administration`), technologies, own public projects (Tabilinks, kovo.space).
- Not allowed: concrete incidents and what went wrong, client or employer internals, internal numbers
  (`110 repositories`, times of night), step by step stories from *Stories* in profile.
- A story from *Stories* can be turned into one summary sentence about how candidate works, without
  the situation itself (`when something breaks in my own solution, I fix it and change the process`).
- Exception: the form explicitly asks for a specific situation (for example *describe your worst
  incident*). Then answer it, but only with what candidate is fine to share.

- Bare slogans (`I am responsible`, `I do things end to end`) are not enough, every claim needs a fact behind it.
- CV overview (list of technologies and what was done with them) is not a letter, it repeats the CV.

## Tone by employer type

Used when candidate has no sample for this employer type. Detect type from offer and company research
done in `/rate-offer`.

| employer type | formality | greeting | what to stress | length |
| ------------- | --------- | -------- | -------------- | ------ |
| state office; public sector; university | formal, full sentences, no slang | Dear Sir or Madam / Vážená paní, vážený pane | stability, following processes, documentation, long-term interest, legal domain if any | 250-350 words |
| bank; insurance; large corporation | formal but direct | Dear Hiring Manager / name if known | reliability, security, regulated environment, delivering in large teams | 200-300 words |
| recruiting agency; bodyshop; consultancy | neutral, business like | Hello / Dobrý den | must-have match, availability, contract type, communication with customer | 120-200 words |
| product company | neutral, friendly | Hello + name if known | product and domain interest, ownership of features, quality | 150-250 words |
| startup | informal, first names | Hi + name | what candidate built alone, speed, breadth, why this product | 100-200 words |

## Prompt types

Application forms often ask a specific question instead of free letter. Ask candidate which one, the
structure changes a lot.

| prompt in form (examples) | focus | structure |
| ------------------------- | ----- | --------- |
| none, free cover letter / motivační dopis | company and role | role or company hook, 2 strongest matches with proof, motivation, closing |
| Why you ? / Why should we hire you ? / Proč právě Vy ? | candidate | must-have matches with proof first, one thing that makes candidate different, no company praise |
| How will you be useful for us ? / What will you bring ? / Čím nám budete přínosem ? | future in the role | map 2-3 responsibilities from offer to concrete past work, what candidate can do in first months |
| Why us ? / Why do you want to work here ? / Proč chcete pracovat u nás ? | company | product, domain, team or tech stack, preferences that the offer meets, no skill list |
| Tell us about yourself / short intro / krátké představení | candidate summary | 3-5 sentences: current role, main stack, strongest result, what candidate looks for |
| other question | as asked | answer the question in the first sentence, then proof |

If form has character or word limit, respect it and show the count next to the letter.

## ATS optimization

ATS (Applicant Tracking System) parses the application and often ranks or filters it by keywords before
any human reads it. ATS version of the letter is written for that, normal version for a human reader.

### Detect the system

Detect from application URL or form page. If unknown, ask candidate and fall back to *generic*.

| ATS | URL hints | notes |
| --- | --------- | ----- |
| Workday | `myworkdayjobs.com`, `wd1.`, `wd3.`, `wd5.` | strict parsing, recruiters filter by keywords and knockout questions, plain text matters most |
| Oracle Taleo | `taleo.net` | old parser, very sensitive to formatting, exact keyword match |
| SAP SuccessFactors | `successfactors.com`, `successfactors.eu`, `jobs.sap.com` | keyword ranking, common in corporations and banks |
| iCIMS | `icims.com` | keyword ranking against offer |
| Greenhouse | `greenhouse.io` | recruiter searches by keywords, letter is often read by human, readability matters |
| Lever | `jobs.lever.co` | recruiter searches by keywords, letter is often read by human |
| SmartRecruiters | `smartrecruiters.com` | keyword matching and scoring |
| Workable | `apply.workable.com` | keyword matching, scoring and screening questions |
| Teamtailor | `teamtailor.com` | common in Czech and Nordic companies, recruiter searches by keywords |
| Recruitee | `recruitee.com` | recruiter searches by keywords |
| Personio | `jobs.personio.com`, `jobs.personio.de` | common in Central European SMEs, mostly human screening |
| Teamio (LMC) | `teamio.com`, responses through `jobs.cz` / `prace.cz` | Czech, recruiter filters by keywords and questionnaire answers |
| generic | anything else, e-mail application | apply all rules below |

### Rules

- Use the job title exactly as written in the offer, at least once, best in the first paragraph.
- Use technologies and skills spelled exactly as in the offer (`Spring Boot`, not `SpringBoot` or `Spring`).
  Write acronym and full name once each, for example `Continuous Integration (CI)`.
- Cover every *must have* the candidate matches (level >= 1 or `related`), most important first.
  Each important keyword 1-2 times, no keyword stuffing.
- Never copy offer phrases as candidate experience (`integrations across the bank's systems is what I have done for years`)
  unless the profile confirms that exact claim. Keywords may appear only at the level the profile shows:
  L1 = `tried / called once`, L2 = `used in a project`, never stronger wording.
- Never add context or purpose that is not in the profile (`certificates *to secure communication*`,
  `deployed *on OpenShift*` when candidate only monitored there). Write what was done, nothing around it.
- Never add a skill the candidate does not have. For `related` match write it honestly
  (`I work with MySQL, which is close to the PostgreSQL you use`). Missing must-have may be mentioned
  only as something candidate is learning, and only if it is true in profile.
- Plain text only: no tables, columns, images, emoji, headers or footers, no special bullets or symbols.
- Standard words over creative ones (`experience`, `skills`, `responsibilities`).
- For file upload use `.docx` or text based PDF, file name `Firstname-Lastname-Cover-Letter-Position`.
- ATS mostly scores the CV, not the letter. If a matched must-have keyword is missing in candidate CV,
  tell candidate to add it there too.
