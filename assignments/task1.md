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
  - Rate candidate preference

