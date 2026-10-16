# Curriculum

German is my second foreign language, mainly for a master's in Germany. It's a steady side project, not a priority.

Goal: solid A2, and B1 if possible, by **27 July 2027**.
Start: Saturday 31 October 2026, as a complete beginner (A0).
Time: 15 minutes on weekdays, 2 hours on Saturday and Sunday. That's about 5 hours a week, roughly 200 hours by late July including the summer push.

The weekends carry the plan. If they shrink, the target drops toward A2.

## Phases

| Phase | Dates | Level |
|---|---|---|
| 1 | 31 Oct – 31 Jan | A1 |
| 2 | 1 Feb – 30 May | A2 |
| 3 | 31 May – end of Q4 exams | B1 (start) |
| 4: summer push | end of Q4 exams – 27 Jul | B1, exam practice |

### Grammar by phase

- **A1:** pronunciation, sein/haben, present tense (regular and irregular), word order (verb second, questions), articles and gender, nominative/accusative, nicht/kein, modal verbs, separable verbs, possessives, basic dative, Perfekt (intro), numbers, time, dates.
- **A2:** Perfekt in full, dative, two-way prepositions, comparative/superlative, weil/dass/wenn clauses, reflexive verbs, Präteritum of sein/haben/modals, imperative, future with werden, polite Konjunktiv II (würde/hätte/wäre), adjective endings (intro).
- **B1:** adjective declension in full, relative clauses, Präteritum, passive, Konjunktiv II (wishes, hypotheticals), zu + infinitive, um…zu/damit, two-part connectors (entweder/oder, weder/noch, sowohl/als auch), verbs with prepositions (da-/wo- forms).

### Vocabulary themes

- **A1:** self, family, food, shopping, time, city, home.
- **A2:** work, travel, health, housing, free time, appointments.
- **B1:** study and university life, jobs, media, environment, giving opinions.

## Materials

| What | Used for | Link |
|---|---|---|
| DW Learn German, *Nicos Weg* | Main course spine (A1–B1), listening, story | https://learngerman.dw.com |
| Goethe-Institut word lists | Official vocabulary per level, source for Anki cards | https://www.goethe.de (A1/A2/B1 exam pages) |
| Goethe practice tests | Checkpoints | https://www.goethe.de/de/spr/prf/ueb/pb1.html (B1) |
| Anki | Daily vocabulary, about 7 new words a day | https://apps.ankiweb.net |
| Easy German (YouTube) | Real spoken German, from A2 | https://www.youtube.com/@EasyGerman |

All materials are free. No books to buy.

Two paid books were recommended: *Grammatik aktiv A1–B1* (Cornelsen) and *Deutsch intensiv Wortschatz* (Klett). Claude doesn't use their content, but the exercises copy their approach:
- **Grammar** works like Grammatik aktiv: one topic per unit, a short explanation, then exercises.
- **Vocabulary** works like Wortschatz intensiv: words grouped by theme and practised in sentences, not as bare lists.

## How it is taught

Claude teaches. No apps besides Anki.

### Weekdays (15 min)

About 5 minutes of Anki, then a 10-minute exercise.

| Day | Focus |
|---|---|
| Mon | Grammar practice on the weekend's topic |
| Tue | Vocabulary and a short reading |
| Wed | Writing 3–5 sentences |
| Thu | Listening: one short clip |
| Fri | Quick mixed quiz on the week |

### Weekends (2 hours each)

| Day | Rough split |
|---|---|
| Sat | 15 min Anki · 45 min new grammar lesson with theory and exercises · 30 min Nicos Weg · 30 min writing |
| Sun | 15 min Anki · 30 min speaking (voice chat with Claude) · 30 min listening/reading · 45 min review of the week and older topics |

New grammar is introduced on Saturday, when there's time for the theory. Weekdays practise it.

### Exercise files

- One file per day in `exercises/`, named `YYYY-MM-DD.md`. Weekday files fit in 10 minutes; weekend files are the long ones.
- Each file has the goal, a short theory section (only when the topic is new), the tasks, and an empty answer section.
- I write my answers in the file and push.
- Claude checks the answers in the file: marks each error, gives the corrected version, and a one-line reason. Repeated mistakes go into `mistakes.md`.
- Instructions are in English during A1, mixed in A2, German only from B1.

### Exam weeks

During TU/e exam periods: weekdays are Anki only, weekends drop to about 30 minutes each.

### Review

- Every Sunday reviews the week and older material.
- Every 4th Sunday, the review mixes topics from weeks or months earlier.

### Speaking

- Sunday voice chat on a topic from that week.
- Claude speaks slowly at first and speeds up over time.
- No corrections mid-sentence. The main 2–3 mistakes come at the end.

### Summer push

- 45–60 minutes on weekdays, weekends unchanged.
- Two speaking sessions a week, plus timed practice-test sections.

## Level exams

There's an exam for each level: A1, A2, B1. Claude sets it when it judges I'm ready, not on a fixed date.

**Ready means:** all four skill bars for the level are at 100% (see Progress below), and most of the level's word list is in Anki.

**The exam:**
- It follows the Goethe-Zertifikat format: Lesen, Hören, Schreiben, Sprechen. The Sprechen part is done in a voice chat.
- It's built from the official Goethe practice tests where possible.
- It goes in `exams/`, for example `exams/A1.md`, and is done on a weekend.
- To pass, I need 60%+ in each part, the same as the real exam.

**After the exam:**
- **Pass:** move on to the next level.
- **Fail:** 2–3 weeks of targeted review on the weak parts, then a retake.

**Target dates** (a guide only, readiness decides): A1 by end of January, A2 by end of May, B1 by late July.

## Progress

The README shows a panel with one bar per skill: Lesen, Hören, Schreiben, Sprechen. Each full bar covers only the current level: A0 → A1 first. After the A1 exam is passed, all four bars reset to A1 → A2, then to A2 → B1.

**How a skill's percentage is set**, for the current level:
- 50% comes from coverage: the share of the level's topics practised in that skill.
- 50% comes from accuracy: my average score in that skill over the last 4 weeks, counted against 80% (80% or better gives the full 50).
- So 100% means everything is covered and I'm scoring 80%+.

**Where the scores come from:**
- Lesen and Hören come from the reading and listening tasks.
- Schreiben comes from the writing tasks.
- Sprechen comes from the Sunday voice chats, where Claude scores each one.

**Updating:**
- Claude updates `progress.json` when checking exercises, at least every Sunday.
- Then Claude runs `python3 tools/progress.py` to redraw `progress.svg`. Never edit the SVG by hand.
- After a passed level exam, Claude records it in `progress.json` and the bars switch to the next level.
