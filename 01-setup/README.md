# 01 — Setup

Prove Python runs on this machine and learn to run a script. Theme: the **Warehouse Management Learning Lab**.

## Files

| File | Level | What it is |
|---|---|---|
| `intermediate1.py` | Intermediate | First script: two `print()` lines confirming Python works |
| `intermediate2.py` | Intermediate | Banner, separators and a six-product SKU table |
| `advanced1.py` | Advanced | Developer profile card printed with `print()` |
| `advanced2.py` | Advanced | Profile card, Python version and a lab progress list |

The number is the order each version was built: 1 is the simpler version of the level, 2 is the fuller one.

## Choosing how to run a script

| Way | Command | Use when |
|---|---|---|
| Terminal | `python intermediate1.py` | Default, learn this first |
| Terminal, launcher | `py intermediate1.py` | `python` opens the Microsoft Store instead |
| VS Code Run button | ▶ in the editor | Quick test once the terminal way works |
| Interactive mode | `python`, then `exit()` | Trying one line |

## Intermediate version: first scripts

**Goal:** run a script and print organized text.

- `intermediate1.py`: `print()` with text between quotes, two lines of output
- `intermediate2.py`:
  - `print("-" * 40)` draws a separator line
  - `print("SKU", "Product", sep=" | ")` joins several values into one table row
  - the first rows of the shared dataset (LAP-001 to PRT-001, locations A-01 to A-06)

## Advanced version: profile card

**Goal:** print a structured profile, then read information from Python itself.

- `advanced1.py`: a "Developer Profile" card (name, track, current focus, status) made of several `print()` lines
- `advanced2.py`:
  - `import sys` and `sys.version.split()[0]` read the Python version
  - `"\n"` inside text starts a new line, so a blank line separates sections
  - `end=" "` keeps the next `print()` on the same line
  - `"=" * 40` draws a header border
  - status written as words (`[done]`, `[next]`), never by symbol alone

## What improved from intermediate to advanced

- **Structure:** the profile card groups information under a heading, where the first scripts printed single lines.
- **Information from Python:** `advanced2.py` reads the version from the machine instead of typing it.
- **Layout control:** `\n` and `end=` shape the output without extra `print()` lines.

## What improved from version 1 to version 2

- **Intermediate:** from two lines to a banner, separators and a data table.
- **Advanced:** from a fixed card to a card with sections, a live version line and a progress list.

## What I learned

- A script runs from the terminal with `python filename.py`.
- `sep=`, `end=` and `"-" * 40` give control over how output looks.
- Mistakes that happened: running `git init` in my home folder instead of the project folder, a typo in a file name (`intermedite2.py`), and a GitHub repo name that did not match my local remote.

## Known issues / next improvements

- [ ] Confirm whether `python` or `py` works on this machine
- [ ] Select the Python interpreter in VS Code
- [ ] Rebuild the environment check with functions after topic 08
