---
name: cover-letter
description: Write cover letter or answer to application form question (why you, how will you be useful) in candidate own style, in normal and ATS optimized version. Use after rating an offer, when candidate asks for cover letter, motivation letter, intro or answer to application question.
argument-hint: "[offer text, URL or company name of already rated offer]"
allowed-tools: Read(~/.claude/plugins/**) Read(~/JobOfferHelper/**) Edit(~/JobOfferHelper/**)
---

# Cover letter

Goal is a letter that sounds like the candidate wrote it, not like AI, in two versions to compare:
normal for a human reader and optimized for the ATS of the employer.

## Data folder

Everything about the candidate lives in `~/JobOfferHelper/` in the home directory of candidate (on Windows
`C:\Users\<name>\JobOfferHelper`). Use the full path with file tools and create the folder when it is missing.
Never write into `${CLAUDE_PLUGIN_ROOT}`, the plugin folder is replaced on every update.

## Inputs

- Offer - in this order:
  1. offer rated by `/job-offer-helper:rate-offer` earlier in this conversation, or latest `rating-*.md` from its folder in
     `~/JobOfferHelper/offer-results/` (see *Offer folder* in `/job-offer-helper:rate-offer`) when candidate names a company or offer rated before
  2. offer text or URL from argument - run `/job-offer-helper:rate-offer` first, letter needs its match, findings and company research
  3. nothing given - ask candidate to paste the offer
- `~/JobOfferHelper/candidate-profile.md` - technologies, *Skill details*, *Preferences* and *Writing style*.
  If missing, tell candidate to run `/job-offer-helper:interview` first. If *Writing style* section is missing in an
  older profile, copy it there from `${CLAUDE_PLUGIN_ROOT}/templates/candidate-profile.md`.
- *Letter material* and *Strengths and stories* in the profile. If *Letter material* is missing or empty, offer
  `/job-offer-helper:letter-interview` before writing. Letters written without it end up repeating the CV.
- `${CLAUDE_PLUGIN_ROOT}/templates/cover-letter.md` - what a letter is for, punctuation rules, cliché phrases, tone, prompt types, ATS.

## Steps

1. *Writing samples* below, only if *Samples* table is empty or candidate wants to add new ones.
2. *Letter questions* below.
3. Pick the thread and material, following *What a letter is for* and *Reader* in `${CLAUDE_PLUGIN_ROOT}/templates/cover-letter.md`:
   - one thread: what connects *Hook*, what the offer needs most and how candidate works
   - 1-2 things the offer cares about and the CV does not explain, each with one proof from *Way of working*,
     *Own words* or *Strengths and stories*, match by *Offer phrases it answers*
   - how the cooperation would work: answers from *Way of working* that the offer fits. Topic answers are labels,
     write them in candidate words from *Own words*, never copy the option text
   - soft *must haves* (ownership, maintainability, knowledge sharing, interest in learning) go first
     for a non-technical reader, tech details stay in the CV
   - never promise what candidate does not want, check *Way of working* and *Drains*
   - after saving the letter, add its offer folder name into *Used in letters* of every story used
   - never mention anything from *Never mention in letters*
   - never describe exact situations from past work projects, keep them for interview, see
     *Keep stories for interview* in `${CLAUDE_PLUGIN_ROOT}/templates/cover-letter.md`
   - `related` matches that are worth explaining honestly
   - preferences the offer meets - they are the real motivation, for *why us* type
   - vary proof points: check letters `~/JobOfferHelper/offer-results/*/cover-letter-*.md` and do not reuse a proof point
     used in one of the last 3 letters (newest by date in file name), unless it is the only proof for a must have. If profile has
     no other proof for that must have, tell candidate and suggest adding projects with `/job-offer-helper:interview`
   - never mention missing skills, red flags, salary or anything from *Findings* as weakness
4. Pick tone: style notes for this employer type, then general *Style notes*, then *Tone by employer type*.
   Language is the language of the offer, unless candidate answered otherwise.
5. Write normal version, structure from *Prompt types* and layout from *Format* in `${CLAUDE_PLUGIN_ROOT}/templates/cover-letter.md`.
6. Write ATS version from the normal one by *ATS optimization* rules. Keep the candidate voice,
   change wording only where keywords need it.
7. Run *Self check* on both versions, fix and check again.
8. Show *Output* and save.

## Writing samples

Ask once, in one message:

"Do You have some cover letters or answers to application questions You wrote Yourself (or at least
finalized Yourself, not raw AI output) ? Paste them or give file paths. Even better with the offer they
were for, as link or text, because style for a bank or state office differs from startup. `skip` to continue without."

For every sample:

1. Save it to `~/JobOfferHelper/writing-samples/<yyyy-mm-dd>-<company>.md` with the offer text or link on top.
   If date is unknown, use today.
2. Detect employer type and prompt type, from the offer if given, otherwise from the letter itself.
   Ask with `AskUserQuestion` only when it is not clear.
3. Add row into *Samples* table.
4. Fill or update *Style notes* - describe what candidate does, with short examples from samples.
   Where samples for different employer types differ, write it into the employer type table.
5. Punctuation habits are saved as they are, but rules from `${CLAUDE_PLUGIN_ROOT}/templates/cover-letter.md` still win.
   Candidate own hyphen style is allowed only within the limit there.

If candidate has no samples, use *Tone by employer type* and tell candidate that after editing and sending
the letter they can paste the final version, so the next one sounds more like them.

## Letter questions

Ask with `AskUserQuestion`, max 4 questions per call, so a second call only when more are needed. Skip what is
already known from offer, URL or earlier answers:

- `Prompt`: does application ask a specific question ? Options from *Prompt types*:
  `Free letter` / `Why you` / `How useful for us` / `Why us`. Candidate can type exact question into *Other*.
- `Limit`: `No limit` / `Up to 500 chars` / `Up to 1000 chars` / `Up to 2000 chars`, *Other* for exact
  number or words.
- `Format`: `Prose` / `Bullets`, see *Format* in `${CLAUDE_PLUGIN_ROOT}/templates/cover-letter.md`.
- `Hook`: "What caught You in this offer ?" Options: up to 4 concrete things from this offer (product, kind of work,
  team, way of working), *Other* for own words. Candidate saying `only applying because of pay / remote` is a valid
  answer: then the letter stays short and does not fake interest.
- `ATS`: shown only when not detected from application URL. Options: `Don't know` / `Workday` /
  `Teamio (LMC)` / `SuccessFactors`, *Other* for any system from *Detect the system* table.
- `Language`: only when offer language is not the language candidate usually writes in, or offer is bilingual.

First time also ask for name and contact for signature and save them into *Writing style*.
If `AskUserQuestion` is not available, ask in one numbered message.

## Self check

Check both versions before showing them, mechanically, not from memory:

- no `—` and no `–` anywhere
- the letter has one thread, read paragraph by paragraph: does each one follow from the previous ?
- every sentence: could it be read from the CV, or sent to another company unchanged ? Rewrite or delete it
- sentences read aloud sound like *Own words*, not like a translated form
- ATS version is at most 40 words longer than the normal one
- count of ` - ` used as sentence separator, semicolons and lists of three within limits
- no phrase from *Phrases* table in `${CLAUDE_PLUGIN_ROOT}/templates/cover-letter.md`, in any language
- no phrase listed in *Phrases candidate never uses*
- every claim is backed by profile, no invented project, number or skill
- check every sentence against profile: no offer phrase presented as own experience, no wording stronger than the level, no added context or purpose
- no exact situation from past work projects (incident, client internals, internal numbers), unless the form asks for it
- no proof point repeated from the last 3 letters in `~/JobOfferHelper/offer-results/*/cover-letter-*.md` (except the only proof for a must have)
- length within limit, count characters if the form has a limit
- greeting and closing match the chosen tone

## Output

1. One line: offer, employer type, prompt type, format, language, ATS and which style source was used
   (own samples for this employer type / own samples / default tone).
2. **Normal version** - the letter, in a code block so candidate can copy it, with word and character count.
3. **ATS version** - the same, ATS detected or `generic`.
4. Keyword table: keyword from offer | must / nice | in normal version | in ATS version.
   Only keywords candidate matches. Add one row with matched must-haves missing in candidate CV, if CV is known.
5. One line on what differs and when to use which, for example
   `Workday filters by keywords before anyone reads it, send ATS version. For e-mail to the CTO send normal one.`
6. Save both versions into the offer folder as `cover-letter-<yyyy-mm-dd>.md` (see *Offer folder* in
   `/job-offer-helper:rate-offer`, create the folder with `offer.md` if offer was not rated), with offer link or title on top.
   Never overwrite an earlier letter, second letter on the same day gets suffix `-2`. Tell candidate the path.
   Letter not tied to any offer (universal letter) goes to `~/JobOfferHelper/offer-results/_universal/cover-letter-<language>.md`.
7. Last line: "If You edit the letter before sending, paste the final version and I will save it as Your
   writing sample." When candidate does, save it as sample with *Written by* = `finalized by candidate`,
   also as `cover-letter-<yyyy-mm-dd>-sent.md` in the offer folder, and update *Style notes*.
