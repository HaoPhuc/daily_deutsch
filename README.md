# daily_deutsch

German practice toward A2–B1 by July 2027: short weekday exercises, longer weekend lessons, and feedback from Claude.

<!-- progress:start -->
![Progress](progress.svg)
<!-- progress:end -->

## How it works
- A new exercise appears in `exercises/` each day, named by date (`2026-10-31.md`).
- Weekdays take about 15 minutes (5 for Anki, 10 for the exercise). Saturday and Sunday take about 2 hours each.
- Write your answers under `## Answers` in the same file, then commit and push. Late is fine.
- Claude checks it on the next run. It fills in `## Feedback`, scores each skill, and logs the result in `LOG.md`.
- **Sundays:** do the speaking part as a voice chat with Claude. Paste the score and mistakes Claude gives you under `## Speaking result`, and fill in your Anki card count.
- **Level exams** go in `exams/` and are set when all four bars reach 100%.

## Files
| File | What it is |
|------|------------|
| [CURRICULUM.md](CURRICULUM.md) | The plan: phases, materials, weekly schedule, exams, how progress is measured |
| [AGENTS.md](AGENTS.md) | The rules Claude follows when posting and checking |
| [topics/](topics/) | Grammar topics and vocabulary themes for A1, A2 and B1, in order |
| [LOG.md](LOG.md) | Every exercise with its skill scores |
| [mistakes.md](mistakes.md) | Repeated mistakes, used for review |
| `progress.json`, `tools/progress.py` | Data and script behind the progress panel |
