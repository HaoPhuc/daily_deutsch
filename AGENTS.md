# AGENTS.md: rules for each run

These are the rules for the run that checks Phuc's answers and posts each day's German exercise. [CURRICULUM.md](CURRICULUM.md) is the plan; this file says how to carry it out. Phuc can edit this file to change how runs behave. The task prompt supplies only what shouldn't sit in a public repo: the git author identity and the email address.

## 1. The learner
- University student, learning German as a side project for a master's in Germany. Starts from zero.
- Speaks English well. Explain in English, keep examples in German.
- Time: 15 minutes on weekdays (5 of them for Anki), 2 hours on Saturday and Sunday.
- Be direct and brief. No filler.

## 2. Settings
```yaml
TIMEZONE: Europe/Amsterdam
WEEK_1_START: 2026-10-31     # a Saturday; weeks run Saturday to Friday
GOAL_DATE: 2027-07-27
EXAM_MODE_UNTIL: 2026-11-08  # TU/e exam period, inclusive; update each quarter
SUMMER_PUSH_FROM: null       # set to the date Q4 exams end
```

## 3. Each run, in order
1. Check every submitted exercise and exam that has no feedback yet (section 7).
2. Post today's exercise, unless one dated today already exists or today is before `WEEK_1_START` (sections 4–6).
3. Update `LOG.md`, `mistakes.md` and `progress.json`, then run `python3 tools/progress.py`.
4. Commit, push and email (section 10).

## 4. Weekly schedule
Every task is tagged with one skill, and only that skill gets a score from it.

| Day | Exercise | Skills | Size |
|-----|----------|--------|------|
| Sat | New grammar topic (theory + exercises), next Nicos Weg lesson, writing | Lesen, Hören, Schreiben | ~1 h 45 min (plus Anki) |
| Sun | Voice-chat prompts, listening and reading, review | Sprechen, Hören, Lesen | ~1 h 45 min (plus Anki) |
| Mon | Practice on Saturday's grammar | Schreiben | 10 min |
| Tue | Theme vocabulary used in sentences, short reading | Lesen | 10 min |
| Wed | Write 3–5 sentences on a prompt | Schreiben | 10 min |
| Thu | One short clip with questions | Hören | 10 min |
| Fri | Mixed quiz on the week | mixed | 10 min |

- **Exam mode** (today ≤ `EXAM_MODE_UNTIL`): no weekday exercises (Anki only). Weekend exercises take about 30 minutes, with the same mix.
- **Summer push** (today ≥ `SUMMER_PUSH_FROM`): weekday exercises take 45–60 minutes and may combine two skills. Add a second speaking session on Wednesdays.

## 5. Choosing topics
- Topics are in `topics/A1.md`, `topics/A2.md` and `topics/B1.md`, in order. The current level is the first one without a passed exam in `progress.json`.
- **Grammar:** each Saturday introduces the next G topic that has no exercise yet (check the Topics column of `LOG.md`). Weekdays practise that week's topics.
- **Vocabulary:** W themes run in order, about one every two weeks. They're used on Tuesdays and in weekend reading and writing.
- **Review:** every Sunday reviews the week. On every 4th Sunday (weeks 4, 8, 12, …), the review instead mixes 2–3 older topics, preferring those with low scores or rows in `mistakes.md`.
- Never skip, reorder or invent topics. When all of a level's topics are posted, keep practising the weakest ones until the level exam.
- **Level exam:** when every skill bar for the level is at 100% and Phuc's Anki count covers most of the level's word list, the next weekend is the level exam instead of the normal exercises (section 8).

## 6. Writing the exercise
One file: `exercises/YYYY-MM-DD.md`.

```markdown
# <Ddd D Mon YYYY> · Week <n> · <topic IDs> · ~<min> min
**Goal:** <one line>

## Theory
<only when a topic is new>

## Tasks
### 1. <title> · <Lesen | Hören | Schreiben | Sprechen>
...

## Answers
<!-- write your answers here -->

## Feedback
<!-- Claude fills this in -->
```

- **Instructions language:** English during A1, mixed in A2, German only from B1.
- **Theory** follows the *Grammatik aktiv* style: one topic, a short explanation with a table if it helps, 3–5 example sentences (with English translations in A1–A2), then 1–3 common pitfalls.
- **Vocabulary** follows the *Wortschatz intensiv* style: words grouped by theme, with article and plural for nouns, practised in sentences rather than bare lists. Tuesday exercises list the new words so Phuc can add them to Anki.
- **Nicos Weg (Saturday):** name the next lesson (`nicos_weg_next` in `progress.json`) with a link to it on learngerman.dw.com, then 3–5 comprehension questions. Write questions only from lesson text you can actually read. If you can't read it, ask for a 3-sentence summary in German instead. Advance `nicos_weg_next` after posting.
- **Listening clips:** use only clips whose transcript or subtitles you can read, and write questions from that. Never invent what a clip says. Link the clip.
- **Sunday** files also include:
  - `## Speaking`: a topic, 4–6 prompts, and this instruction for the voice chat: *"Paste this section into a voice chat with Claude. Claude: speak at my level (slowly at A1), don't correct me mid-sentence, and at the end give me a score out of 100 plus my 2–3 main mistakes."*
  - `## Speaking result`: empty. Phuc pastes the score and mistakes from the voice chat here.
  - `## Anki`: "Cards in Anki: ___".
- Size the exercise to the time in section 4. Don't count Anki in it.

Add a row to `LOG.md` with status `open`.

## 7. Checking
A file counts as submitted when `git log --format='%ce' -- <file>` shows a committer other than `noreply@anthropic.com` and its Feedback section is still empty. Late is fine.

For each submitted file:
- Score each task 0–100. A skill's score for the file is the mean of its tasks' scores.
- Fill in `## Feedback`:
  - per task: the score, then each error as *wrong → right* with a one-line reason;
  - one thing to focus on next.
  Keep it short.
- Never edit Phuc's answers.
- **Sunday:** the Sprechen score is the score under `## Speaking result`. If that's empty, leave Sprechen as `—`. Copy the Anki count to `anki_words` in `progress.json`.
- If an error appeared before, add it to `mistakes.md` or raise its count.
- In `LOG.md`, fill in the skill scores and set the status to `checked`.

## 8. Level exams
- File: `exams/<LEVEL>.md` (retakes: `exams/<LEVEL>-retake.md`). It's done over one weekend and is the weekend's only exercise.
- Use the Goethe-Zertifikat format: Lesen, Hören, Schreiben, Sprechen.
- Prefer the official free Goethe practice test for the level. Link it, have Phuc write his answers in the file, and check them against its official key. Don't copy its content into the repo. If none is available, write your own in the same format.
- Sprechen is done in a voice chat, like Sundays, with the result pasted into the file.
- **Pass:** 60%+ in each part. Record it in `progress.json` as `"<LEVEL>": {"date": "YYYY-MM-DD", "scores": {"Lesen": n, "Hören": n, "Schreiben": n, "Sprechen": n}}`. The bars then switch to the next level.
- **Fail:** 2–3 weeks of targeted review on the weak parts, then a retake.
- Exams don't go in `LOG.md`.

## 9. Progress
- `progress.json` holds `start`, `goal`, `anki_words`, `nicos_weg_next` and the passed `exams`.
- `tools/progress.py` computes each skill's bar from `LOG.md` and `topics/` (formula in CURRICULUM.md) and redraws `progress.svg`.
- Never edit `progress.svg` by hand.

## 10. Commit, push, email
1. Stage everything the run changed, then `git fetch origin main` and `git rebase origin/main`.
2. Make one commit, using the author identity from the task prompt, with a message like `Feedback: <dates>; new: <date> <title>`.
3. Push with `git push origin HEAD:main`. Never force-push or rewrite history.
4. If the task prompt gives an email address, send one short email:
   - **Subject:** `Deutsch — <Ddd D Mon>: <title>`.
   - **Body:**
     - one line per checked exercise: the date, the skill scores, and the main point;
     - today's exercise: title, minutes, and a link to the file on GitHub.
   - If the push failed, say so at the top.

## 11. When something goes wrong
Never end silently. If a run can't post or check something, leave the repo consistent and explain in the email what stopped and what Phuc should do.
