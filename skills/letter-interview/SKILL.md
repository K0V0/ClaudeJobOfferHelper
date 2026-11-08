---
name: letter-interview
description: Second interview of the candidate, collects what a CV can not show (way of working, ownership, motivation, career path, stories, own words) for cover letters. Use after the first interview, when cover letters sound generic, or when candidate wants to add a story.
argument-hint: "[stories]"
allowed-tools: Read(~/.claude/plugins/**) Read(~/JobOfferHelper/**) Edit(~/JobOfferHelper/**)
---

# Letter interview

Technologies and years are in the CV and in *Technologies*. This interview collects the rest: how the candidate
works, what they want, why, and how they say it in their own words. `/job-offer-helper:cover-letter` writes letters from it.

## Data folder

Everything about the candidate lives in `~/JobOfferHelper/` in the home directory of candidate (on Windows
`C:\Users\<name>\JobOfferHelper`). Use the full path with file tools and create the folder when it is missing.
Never write into `${CLAUDE_PLUGIN_ROOT}`, the plugin folder is replaced on every update.

## Before start

1. Read `~/JobOfferHelper/candidate-profile.md`. If it is missing, tell candidate to run `/job-offer-helper:interview` first.
2. If section *Letter material* or *Strengths and stories* is missing in an older profile, copy it there from
   `${CLAUDE_PLUGIN_ROOT}/templates/candidate-profile.md`.
3. If argument is `stories`, go straight to *Strengths and stories*.
4. Skip every topic already answered in *Letter material*, unless candidate asks to update it.
5. Tell candidate how many screens are coming and how to stop:
   "Type `done` into *Other* to finish, `skip` to skip the question. You can continue later with `/job-offer-helper:letter-interview`."

## Way of working

Ask with `AskUserQuestion`, one screen per block, single select unless noted. *Other* is always there for own words,
and an answer in own words is better than a clicked one. `header` is the topic.

Block 1, ownership:

| topic | question | options |
| ----- | -------- | ------- |
| Ownership | Do You want to take ownership of a whole functionality or service, or do You prefer clearly assigned tasks ? | `Whole service, also in production` / `Whole feature, from assignment to deployment` / `Clearly assigned tasks` / `Depends on the project` |
| Autonomy | When You get a task, how much do You want to decide Yourself ? | `Only the goal, the rest is mine` / `Agree on the approach, then alone` / `Clear assignment and review` |
| Beyond task | You notice a problem outside Your task. What do You usually do ? | `Fix it myself` / `Find the cause and hand it over` / `Report it and continue` |
| Why | Do You want to know why a feature exists and who uses it ? | `Yes, talking to users directly` / `Yes, through PO or analyst` / `Only what the task needs` |

Block 2, people:

| topic | question | options |
| ----- | -------- | ------- |
| Team | In what kind of team do You work best ? | `Up to 5 people` / `5 to 10 people` / `Large organization` / `No preference` |
| Sharing | How do You like to share knowledge ? (multi select) | `Code review` / `Documentation` / `Helping juniors` / `Mostly learning from others` |
| Disagreeing | You disagree with a technical decision. What do You do ? | `Argue with facts, then accept the result` / `Try the alternative and show it` / `Accept it and move on` |
| Contact | How do You prefer to work with colleagues ? | `Mostly written` / `Short calls` / `In person` / `No preference` |

Block 3, kind of work:

| topic | question | options |
| ----- | -------- | ------- |
| Codebase | What do You like to work on ? (multi select) | `New systems from scratch` / `Improving a running system` / `Modernizing legacy` / `No preference` |
| Breadth | Depth or breadth ? | `Deep in one field` / `One main field with overlap` / `Whatever the project needs` |
| Deadline | Deadline collides with quality. What do You prefer ? | `Cut scope, keep quality` / `Ship, then come back and fix` / `Hold it until it is right` |
| Start | How do You start on a new project ? | `Read code and documentation` / `Take a small task right away` / `Ask people who know it` / `Run it and try things` |

Block 4, direction. Options come from profile and earlier answers, the ones below are examples:

| topic | question | options |
| ----- | -------- | ------- |
| Energy | Which work gives You energy ? (multi select) | `Solving hard bugs` / `Building something new` / `Automating manual work` / `Making things simpler` |
| Drains | Which work drains You ? (multi select) | `Long meetings` / `Repetitive tasks` / `Unclear assignments` / `Context switching` |
| Motivation | Why are You looking now ? (multi select) | `Back to main field` / `Room to grow` / `Better pay` / `Stability` |
| Avoid | Is there something letters must never mention (reason for leaving, gap, NDA project) ? | `No` / `Yes, I will write it` |

*Drains* and any reason like `Better pay` are never written into a letter. They only stop the letter from promising
what candidate does not want.

If `AskUserQuestion` is not available, ask in one numbered message answered like `1: a 2: c`.

## Own words

After the blocks, one plain numbered message, free text, answered briefly, in the language candidate writes letters in.
Tell candidate that it does not have to sound good, it should sound like them, as if telling a friend.

1. How did You get to this work ? Your path in 2-3 sentences, especially what the CV does not explain.
2. For Your answers on *Ownership*, *Beyond task* and *Deadline*: one time it really happened, in plain words.
   No client names or internal numbers needed.
3. What do colleagues come to You for ?
4. What do You do that others on Your level usually do not ?
5. What work would You be glad to be doing in two years ?
6. What do You like about Your work, and what would You change ?
7. The *Avoid* detail, if `Yes`.

`don't know` is fine.

## Saving

Write after every block, do not wait to the end.

- *Way of working*: one row per topic. *Answer* as clicked or typed. *Proof* only from what candidate told.
  *Offer phrases it answers* in Czech and English, for example `ownership`, `dotahování do konce`, `samostatnost`.
- *Own words*: answers word for word, fix only typos. These are the sentences letters are built from, never polish them.
- *Career path*, *In two years*: from the answers.
- *Proudest result*, *Praised by colleagues*, *Different from other candidates*, *Motivation*, *Never mention* in
  *Strengths and stories*, *Other*: fill or update, do not duplicate them in *Letter material*.
- Never invent a fact, a result or a motive. A vague answer is saved as it is and marked `unsure`.

## Strengths and stories

Goal is proof for *why hire me* answers and for soft *must haves* in offers (ownership, maintainability, sharing
knowledge, learning), written for a non-technical reader. Fill *Strengths and stories* section of profile.

1. Prefill: from sources, *Skill details*, writing samples and earlier letters propose 3-6 candidate
   stories (what happened, where). Do not invent results, leave them empty.
2. Ask with `AskUserQuestion`, one call:
   - `Strengths` (multi select, candidate picks max 3) - what colleagues come to You for, or what You do
     better than others. Options: 4 most likely from profile, for example `Owning work end to end`,
     `Long-term maintainable code`, `Automating manual work`, `Bridging dev and ops`, `Explaining and sharing
     knowledge`, `Learning new tech fast`, `Debugging hard problems`. *Other* for own words.
   - `Stories` (multi select) - which prefilled stories are real and can be told in a letter.
3. Then one plain numbered message, free text, answered briefly. For every picked story ask:
   - what was the problem or starting state
   - what did You do Yourself (not the team)
   - what changed after: number, time saved, who used it, what stopped breaking. `don't know` is ok
4. Write a story only with facts candidate gave or confirmed. Missing result stays empty, mark `unsure`
   if candidate guessed. Map every story to strengths and to offer phrases it proves
   (Czech and English, for example `ownership`, `dotahování do konce`).
5. Ask max 3 stories in one run. Candidate can add more later with `/job-offer-helper:letter-interview stories`.

## Finish

Print a short summary: 3-4 lines on how the candidate works, as it would be said about them, and ask if it sounds right.
Fix what does not. Then tell that letters can be written with `/job-offer-helper:cover-letter`.
