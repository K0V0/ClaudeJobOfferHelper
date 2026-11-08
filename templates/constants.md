# Constants

Some basic settings and guidelines for agent to work

## Role competence complexity table 

- chosen one that fits best

| complexity | description |
| ---------- | ----------- |
| single | based on description, this is single role - like Backend developer, DevOps engineer, ... |
| with overlap | You may have overlap with other fields, but not for purpose working in them, for example backend deveoper who is able to operate app in Kubernetes cluster |
| mutlirole | You are a fullstack developer and role requires deep knowledge from multiple app development fields like frontend, backend, devops |
| analytic | You are required to know the domain (for example laws, finance and trading, business processes and other non-IT knowledge in deeper level) |
| product owner | analytic skills plus sales skills | 
| full-fullstack | Write frontend, backend, deploy, operate, monitor the app - backend, frontend, devops. No deep doman knowledge required hovewer |
| IT department | full-fullstack plus you have manager abilities and want to lead the project / team |
| Founder | IT department skills plus analytic skills plus product owner skills |

### Job target field to complexity

Candidate picks field(s) in *Job target* of the profile, complexity follows from them.

| job type | fields | complexity |
| -------- | ------ | ---------- |
| Backend / Frontend / DevOps | one field | single (or with overlap, if candidate wants to touch other field) |
| Full stack | backend + frontend | mutlirole |
| Backend + DevOps, Frontend + DevOps | two fields with devops | mutlirole |
| Full-full stack | backend + frontend + devops | full-fullstack |

## Responsibilities merge table

- chosen multiple that fits

| responsibility to report to the candidate | responsibilities in job offer |
| ----------------------------------------- | ----------------------------- |
| Bare | write code; write tests; write code basd on analysis or task; implement API; design API; find and fix a bug; |
| Standart | make analysis; make assignments; contribute to analysis; make documentation; share knowledge; presentation of knowledge; |
| Extened | contribute to the architecture decisions; propose architecture; create new services; |
| customer support | direct or indirect communication with customer |
| bodyshop | sold to the customer |
| on call | work requires on-call after working hours |
| end to end | delivered feature is your full responsibility regardless how many other people contributed to it |

## Seniority table

- chosen one that fits best, for offer and for candidate
- years are only orientation, autonomy and scope decide

| level | years (orientation) | autonomy | scope | signals in job offer |
| ----- | ------------------- | -------- | ----- | -------------------- |
| junior | 0-2 | needs guidance, tasks are prepared and explained | single task | junior; graduate; we will teach You; first job; |
| medior | 2-5 | independent on features, asks for help with design | feature | regular; mid; independently deliver; |
| senior | 5+ | independent including design, mentors others | component or service | senior; design solutions; mentor; own the service; |
| lead | 7+ | sets technical direction for team or teams | team or product | tech lead; principal; staff; architect; drive technical decisions; |

## Red flags table

Used to alert candidate. Every found red flag is reported with severity and with a question candidate can ask on interview.

- one `info` is not a problem, it is something to verify; more of them together raise the severity
- offers in Czech use the same phrases in Czech (*odolnost vůči stresu*, *flexibilita*, *atraktivní mzda*, ...) - translate and match them too

### Phrases

| phrase in job offer | possible meaning | severity | question for interview |
| ------------------- | ---------------- | -------- | ---------------------- |
| dynamic / fast-paced environment | priorities change often, pressure | warning | How often do priorities change during a sprint ? |
| wearing many hats; jack of all trades | understaffed, multirole for single role salary | warning | How big is the team and who covers which roles ? |
| rockstar; ninja; hero | overtime and hero culture | warning | How often do You work overtime and how is it compensated ? |
| we are like a family; family atmosphere | blurred boundaries, loyalty expected over pay | warning | How do You handle work outside working hours ? |
| competitive salary (no number) | below market or wants to negotiate down | warning | What is the salary range for this position ? |
| flexible working hours | may mean availability outside hours | info | What are core hours and is availability expected outside them ? |
| work under pressure; tight deadlines | chronic crunch | alert | How many releases in last year were late and what happened ? |
| start ASAP; immediate start | high turnover or firefighting | warning | Why is the position open ? |
| unlimited vacation | no guaranteed vacation, social pressure not to take it | info | How many days did team members take last year on average ? |
| long-term project for our client | bodyshop, real customer hidden | info | Who is the end customer and how long are You working with them ? |
| self-starter; minimal supervision | no onboarding, no seniors around | warning | How does onboarding look like and who will I learn from ? |
| other duties as assigned | unbounded scope | warning | What else besides listed responsibilities did previous person do ? |
| passion required; love what You do | unpaid extra work expected | info | How do You measure performance ? |
| work hard, play hard | overtime plus social events expected after hours | warning | What does a normal week look like, including evenings ? |
| young dynamic team | few seniors to learn from, low salaries, possible age discrimination | warning | What is seniority mix of the team ? |
| stress resistance; resilient to stress | stress is normal state of the job | alert | What are the most stressful situations in this role and how often do they happen ? |
| flexibility (required from candidate) | unpaid overtime, changing tasks and hours | warning | In which situations do You need me to be flexible ? |
| loyalty | low salary raises, leaving is taken personally | warning | How are salary reviews done and how often ? |
| not a 9-5 job; no 9-5 mentality | overtime is expected by default | alert | How many hours does the team work per week in reality ? |
| go the extra mile; give 110 %; above and beyond | overtime is expected by default | alert | How is work above contract recognized and paid ? |
| be reachable; available on phone | unpaid on call | warning | Is availability outside working hours expected and paid ? |
| multitasking | understaffed, constant context switching | warning | How many projects will I work on at the same time ? |
| full ownership; responsible for everything | responsibility without authority | warning | What can I decide on my own and what needs approval ? |
| pick up any technology quickly | huge or chaotic stack, no training | info | How long is onboarding and is learning time paid ? |
| work independently with minimal documentation | legacy without documentation | warning | How is the system documented and who knows it ? |
| startup mentality (in established company) | startup chaos without startup equity or pay | warning | What does startup mentality mean in Your daily work ? |
| we are growing rapidly | chaos, missing processes, can be also a good sign | info | How did team grow last year and how is onboarding handled ? |
| hackathons; weekend events | unpaid weekend work presented as fun | warning | Are weekend events paid or voluntary ? |
| salary based on performance; motivating bonuses | low base salary, unclear bonus rules | alert | What is the base salary and what part of bonuses was paid last year ? |
| salary up to X | real offer will be near the bottom | info | What is the bottom of the range and what decides the final number ? |

### Perks instead of benefits

Perks are not a problem themselves. They become a red flag when they are the main benefits, salary is missing
or they are presented as something special. Real benefits are money, time and security: salary, paid vacation
over legal minimum, sick days, pension contribution, paid training time, home office allowance, meal allowance (in SK only above legal contribution).

| perk in job offer | possible meaning | severity | question for interview |
| ----------------- | ---------------- | -------- | ---------------------- |
| fruit in the office; free coffee and tea; drinks | trivial cost presented as benefit, nothing more to offer | info | What are benefits besides office refreshments ? |
| beer after work; pub Fridays | social life is part of job, pressure to stay after hours, drinking culture | warning | Are after work events during working hours ? What if I do not drink ? |
| playing games together; PlayStation; foosball; table tennis | office as second home, long hours expected, young homogenous team | info | How often do people actually use it and when do they leave the office ? |
| pizza Fridays; free dinner | dinner is provided because people stay late | warning | Why is dinner provided and when do people usually leave ? |
| teambuilding | normal, but check if it is on weekends and unpaid | info | Are teambuildings during working days ? |
| modern office in city center | office is the main selling point, remote not possible | info | How many days a week is office required ? |
| possibility of home office | office by default, home office as a favour | info | How many home office days are standard and who approves them ? |
| Multisport card as main benefit | small cost, often partly paid by employee | info | How much of the card do I pay myself ? |
| benefits after probation / after 1 year | benefits are used to keep people from leaving | info | Which benefits do I have from day one ? |

### Legal duties presented as benefits

Employer has to provide these anyway, so they add no value to the offer. Rules differ by country of the employment
contract, each row says where it applies. Vacation rows also depend on candidate age and child care: profile does
not store them, so if they are not known, report the flag together with the condition.

| phrase in job offer | possible meaning | severity | question for interview |
| ------------------- | ---------------- | -------- | ---------------------- |
| 20 days of vacation; 4 weeks of vacation | legal minimum in SK and CZ, nothing extra | info | How many days of vacation do You give over legal minimum ? |
| 25 days of vacation; 5 weeks of vacation (SK) | legal minimum in SK for anyone who turns 33 by end of the year or permanently cares for a child, real benefit only for others | info | Do people who have 5 weeks by law get anything extra ? |
| 25 days of vacation; 5 weeks of vacation (CZ) | legal minimum at state and public employers, at private employer it is 1 week over 4 week minimum and very common | info | How many days of vacation do You give in total, is there more with seniority ? |
| 5 extra days of vacation | if counted from 4 weeks, in SK it is only legal minimum for anyone 33+ or caring for a child | info | Extra over what ? How many days will I have in total ? |
| salary paid on time; reliable salary payment | basic legal duty (SK and CZ: latest by end of next month), mentioning it suggests payment problems now or in the past | warning | On which day is salary paid and was it ever late in last 2 years ? |
| invoices paid on time; reliable payment of invoices | basic contractual duty, mentioning it suggests cash flow problems | warning | What is invoice due date and was any invoice paid late in last 2 years ? |
| paid health and social insurance | mandatory for employer in SK and CZ, nothing extra | info | What are benefits besides those required by law ? |
| HPP; stable employment contract; legal employment | work with employee obligations has to be employment by law anyway, unusual only compared to bodyshops and švarcsystém | info | What does this contract give me over legal minimum ? |
| paid overtime | legal minimum in SK and CZ is pay plus 25 % surcharge, or time off where agreed | info | Is overtime surcharge over legal minimum and how often is overtime needed ? |
| paid public holidays | public holidays are paid by law | info | What are benefits besides those required by law ? |
| meal vouchers; meal allowance (SK) | employer has to arrange meals in SK, real benefit only above legal contribution. Not mandatory in CZ, there it is a real benefit | info | What is employer contribution per day ? |
| social fund contribution (SK) | creating social fund is mandatory in SK from first employee | info | How much is paid from the fund per person per year and for what ? |
| paid time off for doctor, wedding or funeral | legal right in SK and CZ within limits, in SK doctor is paid up to 7 days per year. Sick days without doctor are a different, real benefit | info | Do You give paid days over the legal limit ? |
| compensation during sickness | statutory compensation, only amount above it is a benefit | info | Do You pay more than law requires during sickness ? |
| work laptop provided; we provide all equipment (on HPP) | employer has to create conditions for work, nothing extra | info | What are benefits besides work equipment ? |

### Contract and money

| phrase or situation | possible meaning | severity | question for interview |
| ------------------- | ---------------- | -------- | ---------------------- |
| part of salary in cash; salary partly as bonus "on hand" | tax evasion, lower sick pay, pension and unemployment benefit | alert | Is the whole salary in the contract and paid to bank account ? |
| minimum wage plus bonuses | real salary is not guaranteed | alert | What is the guaranteed amount in the contract ? |
| overtime included in salary | legal in CZ only up to a limit of hours per year | warning | How many overtime hours per year are included and how is the rest paid ? |
| DPP / DPČ for full time work | no paid vacation, limited insurance, easy to terminate | alert | Why is it not HPP when the work is full time ? |
| IČO only; be Your own boss | employer shifts insurance, vacation and sick days costs to You | warning | Is HPP possible ? What MD rate covers vacation and sick days ? |
| higher salary after probation | lower pay during probation, risk of termination before raise | warning | Is the raise after probation written in the contract ? |
| training agreement; we pay certification, You stay N years | repayment if You leave, can lock You in | warning | How much and for how long would I repay if I leave ? |
| non-compete clause | can block You from working in the field after leaving | warning | Is non-compete paid and for how long ? |
| use Your own laptop / equipment (on HPP) | employer shifts costs, security risk | warning | Do You provide work equipment ? |
| commission based pay for developer | salary depends on sales You do not control | alert | Why is developer salary tied to sales ? |
| unpaid trial day / trial week | in CZ any work must be paid, this is illegal work | alert | Will the trial day be paid and under which contract ? |

### Junior traps

Report these with extra explanation when candidate target level is *junior*.

| phrase or situation | possible meaning | severity | question for interview |
| ------------------- | ---------------- | -------- | ---------------------- |
| You will be the only developer | nobody to learn from, mistakes are only Yours | alert | Who will review my code and help me when I am stuck ? |
| also help with IT, printers, network, web | "IT guy for everything", not a developer job | warning | What part of time will be development ? |
| unpaid internship | free work, in CZ paid internship is standard in IT | alert | Why is the internship unpaid ? |
| trainee program / academy You pay for, then we hire You | business on juniors, hiring is not guaranteed | alert | How many graduates were hired last year and under what conditions ? |
| trainee program with obligation to stay or repay | lock-in with low junior salary | alert | What happens if I leave during the obligation period ? |
| test assignment of several days or real production feature | free work, task may be used in their product | alert | How long should the task take ? Will it be paid ? |
| career growth possible (no plan described) | no plan, no raises | info | How did the last junior grow and in what time ? |
| learn on real projects from day one (no mentoring mentioned) | thrown into production without support | warning | Who will be my mentor and how much of their time is reserved for it ? |

### Hiring process

Detect from offer text or when candidate describes the process.

| situation | possible meaning | severity | question for interview |
| --------- | ---------------- | -------- | ---------------------- |
| more than 4 interview rounds | slow decisions, disrespect of candidate time | warning | How many rounds are there and when will I know the result ? |
| number of rounds and timeline not disclosed even after request | unorganized process, no real hiring plan, disrespect of candidate time | warning | Who decides about hiring and by which date will I have the final answer ? |
| homework longer than 4 hours | free work, disrespect of candidate time | warning | Can I do live coding or show existing project instead ? |
| copy of ID card, birth number or bank account before contract | scam or GDPR violation | alert | Why do You need this before the contract is signed ? |
| any payment from candidate (course, equipment, "registration") | scam | alert | - do not pay, leave the process |
| pressure to accept within 24 hours | hiding something, desperate hiring | warning | Can I have a few days to decide ? |
| recruiter can not say client, salary or team after first call | bodyshop or not real position | warning | Is the position open now and who is the client ? |
| nobody from the team takes part in interviews | You will not know the team before joining | info | Can I meet someone from the team ? |

### Inconsistency rules

| rule | why it matters | severity |
| ---- | -------------- | -------- |
| title seniority does not match responsibilities or must-haves (junior title, senior requirements) | underpaid position | alert |
| salary is below expectation for offer seniority | underpaid position | alert |
| required years exceed age of technology (10 years of Kubernetes) | offer written without understanding the role | warning |
| *single* role with must-haves from 3+ unrelated fields | actually *multirole* or *full-fullstack* | warning |
| more than 10 must-haves | unrealistic wishlist or unclear role | warning |
| IČO contract with employee obligations (fixed hours, office, manager, exclusivity) | švarcsystém - illegal disguised employment in CZ | alert |
| remote in title, office days in text | misleading offer | warning |
| on call in text, no on call compensation mentioned | unpaid on call | warning |
| no salary and no company name | agency hiding customer and budget | info |
| HPP mentioned, but only MD or hourly rate given | unclear contract type | warning |
| benefits section has only perks (fruit, coffee, games, beer) and no salary | nothing real to offer | warning |
| "cutting-edge technologies" but old versions (Java 8, AngularJS, Spring 4) | legacy sold as modern | warning |
| junior position and no senior or mentor mentioned | nobody to learn from | warning |
| *Extened* or *IT department* responsibilities with junior or medior title | senior work for junior salary | alert |
| no tech stack, no team size, no work mode | offer copy-pasted or position not real | info |
| same offer reposted for months | high turnover or nobody accepts conditions | warning |
| salary range spread is more than 2x (40-100k) | range is meaningless, real offer near bottom | info |
