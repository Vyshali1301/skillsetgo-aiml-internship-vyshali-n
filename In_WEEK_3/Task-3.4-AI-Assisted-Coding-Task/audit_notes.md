# Task 3.4 - AI-Assisted Coding Task: Audit Notes

## Objective
Build a small app with an AI coding assistant, then review, correct, and audit the generated code.

## What was built
`app.py` - a command-line Student Grade Manager: add students with scores, compute averages and letter grades,
list students ranked by average, and persist data to `students.json`.

## Tool used
Claude (Anthropic) - asked to generate a simple CLI grade manager with add/list/save-load functionality.

## Audit checklist
Go through the code yourself and check each of these. Some issues are genuinely present in the code above -
find them before reading further.

- [ ] **No input validation on scores.** `float(s)` will crash the whole program if the user types something
      that isn't a number, or enters an empty string. Try it: choose "1", type a name, then type `abc` for scores.
- [ ] **No validation that scores are in a sensible range (0-100).** A score of `150` or `-20` is silently accepted
      and will skew the average and grade.
- [ ] **No check for duplicate names.** Adding "Priya" twice silently overwrites her previous scores with no
      warning.
- [ ] **No handling for an empty scores list.** If `raw` is an empty string, `scores` becomes `[]`, and
      `average([])` will raise a `ZeroDivisionError` the next time `list_students` runs.
- [ ] **No file-corruption handling.** If `students.json` gets manually edited into invalid JSON, `load_data`
      crashes instead of giving a clear error.
- [ ] **No type hints or docstrings on most functions** - fine for a small script, but worth noting as a
      limitation if this were extended.

## What I actually fixed
*(Pick at least 2-3 of the issues above, fix them in `app.py`, and describe the fix here in your own words -
e.g. "wrapped the score input in a try/except and asked again on invalid input".)*

1.
2.
3.

## What I decided NOT to fix, and why
*(It's fine to leave something as-is for a small internship task - just say why, e.g. "didn't add a database,
a JSON file is enough for this scope".)*

-

## Key learnings
*(3-5 points on what you learned about reviewing AI-generated code - what kinds of bugs AI assistants tend to
leave out, what you now check for by habit, etc.)*

-
