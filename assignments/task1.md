# ClaudeJobOfferHelper

## App purpose and goals

- Help candidate to summarize given job offer with long and exhausting description for him.
- Rate given job offer from multiple standpoints and present data to the candidate.
- Capture possible red flags and inconsitencies and alert candidate.
- Based on candidate match and preferences write Intro / "Motivation" letter.

## How app should generally work ? 

- Some criteria are static and are provided here, but it is expected that candidate will be asked questions
  and responses will then be saved into tables that will serve as knowledge and context base for examining how well 
  suited is given position for candidate.
  - Agent will ask and gain informations from the candidate.
  - Agent will tell the candidate what to tell if asking questions for given topic is complete 
    and candidate has nothing more to say.
 
## Execution / analysis of goals

### Summarize

Create short job description intro from given offer, extract basic information:
  - Position name and title.
  - Position competence rated based on *Role competence complexity table*.
  - Position responsibilities shortlist based on *Responsibilities merge table*.
  - If is it recruiting agency, write it and try to find real customer of this project.
  - If it is software house, try to find for who that project is going to be build.
  - HPP or IČO.
  - Company location.

### Rating offer
  - Rate match of candidate knowledge vs. requirements in given advertisement
    - If possible by information given in advert, split that rating into following categories:   
        - Must have
        - Nice to have
        - Total
    - match = 1 point, partial match (one level below required or related technology) = 0.5 point
  - Rate according to user preferences
    - preference met = 1 point

#### Calculation and results presentation:

The presentation should follow this format, everything nicely in the table:

| measured property | result |
| ----------------- | ------ |
| Hard skills fit | percentage of total skills & requirements captured vs. candidate profile, total numbers |
| requirements fit | percentage of candidate preferences met, total numbers |
| hard skills missed                  |  percentage, total number      |
| requiremetns missed                  | percentage, total number       |
| captured red flags                  |  count, minus points by severity: info = 0, warning = -1, alert = -2      |
| total                  |    percentage of maximum possible points vs counted    |

then after table with statistical data, add another table:

- missing skills and its severity (required, optional)
- missing requirements (and margin in for example for salary and homeoffice)
- captured red flags list
- the final verdict - check if there is some deal-breaker severity