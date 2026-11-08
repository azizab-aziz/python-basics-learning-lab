# 01 — Setup

Prove Python runs on this machine and learn to run a script. Theme: the **Warehouse Management Learning Lab**.

## Files

| File | Level | What it is |
|---|---|---|
| `intermediate1.py` | Intermediate | First script: two `print()` lines confirming Python works |
| `intermediate2.py` | Intermediate | Banner, Python version and a six-product SKU table |
| `advanced1.py` | Advanced | Developer profile card printed with `print()` |
| `advanced2.py` | Advanced | Environment check: version rule, OS, script folder, OneDrive warning, exit code |

## Choosing how to run a script

| Way | Command | Use when |
|---|---|---|
| Terminal | `python intermediate1.py` | Default, learn this first |
| Terminal, launcher | `py intermediate1.py` | `python` opens the Microsoft Store instead |
| VS Code Run button | ▶ in the editor | Quick test once the terminal way works |
| Interactive mode | `python`, then `exit()` | Trying one line |

## Intermediate version: first scripts

**Goal:** run a script, read its output, and print structured text.

- `intermediate1.py`: `print()` with text between quotes, two lines of output
- `intermediate2.py`:
  - `import sys` to read the Python version with `sys.version.split()[0]`
  - `print()` with several values separated by commas
  - `sep=" | "` to build table rows
  - `"-" * 40` to draw separator lines
  - the first rows of the shared dataset (LAP-001 to PRT-001, locations A-01 to A-06)

## Advanced version: profile card and environment check

**Goal:** show a simple output script, then a script that checks the environment and fails clearly when it is wrong.

- `advanced1.py`: a "Developer Profile" card (name, track, current focus, status) printed with `print()`
- `advanced2.py`:
  - constants `MIN_PYTHON` and `LINE`
  - small functions with type hints (`python_is_recent_enough`, `build_rows`, `print_report`) and a `main()` that returns an exit code
  - `platform` and `pathlib.Path` to report the OS and the script's real folder
  - a OneDrive warning, because the repo lives inside OneDrive
  - f-string alignment (`{label:<{width}}`) for a neat report
  - `if __name__ == "__main__":` and `sys.exit(main())`

## What improved from intermediate to advanced

- **Checks, not just prints:** `advanced2.py` decides READY or FAILED instead of always printing the same text.
- **Exit codes:** other tools can tell success (0) from failure (1).
- **Real values:** the script reads the version, OS and folder from the machine, not from fixed text.
- **Structure:** small functions and constants replace one long list of `print()` lines.
- **Status in words:** "OK", "TOO OLD", "WARNING".

## What I learned

- A script runs from the terminal with `python filename.py`, and `print()` is the first way to see results.
- `sep=` and `"-" * 40` build table-like output without any library.
- A function can return a value (`main()` returns 0 or 1) and the terminal can read it as an exit code.
- Mistakes that happened: running `git init` in my home folder instead of the project folder, a typo in a file name (`intermedite2.py`), and a GitHub repo name that did not match my local remote.

## Known issues / next improvements

- [ ] `intermediate2.py`: `Mon-001` should be `MON-001` and `laptop` should be `Laptop`, to match the shared dataset.
- [ ] `intermediate2.py`: the banner and last line start with lowercase words, unlike the rest of the lab.
- [ ] `advanced1.py` uses only `print()`, the same skill as intermediate; rework it after topic 02 with variables.
- [ ] `advanced2.py`: the docstring says `python advanced.py`, but the file is named `advanced2.py`.
- [ ] Confirm whether `python` or `py` works on this machine.
- [ ] Select the Python interpreter in VS Code.