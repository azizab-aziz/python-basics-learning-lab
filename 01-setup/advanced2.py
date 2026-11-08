"""Environment check for the Warehouse Management Learning Lab.

Run it with:  python advanced.py
Exit code 0 means the setup is ready, 1 means something needs fixing.
"""

import platform
import sys
from pathlib import Path

MIN_PYTHON = (3, 10)
LINE = "-" * 46


def python_is_recent_enough() -> bool:
    return sys.version_info >= MIN_PYTHON


def build_rows() -> list[tuple[str, str]]:
    # resolve() gives the real absolute path, whatever folder you ran from
    script_folder = Path(__file__).resolve().parent
    in_onedrive = any("onedrive" in part.lower() for part in script_folder.parts)

    current = ".".join(str(n) for n in sys.version_info[:3])
    required = ".".join(str(n) for n in MIN_PYTHON) + "+"
    version_status = "OK" if python_is_recent_enough() else "TOO OLD"
    onedrive_status = (
        "yes - WARNING, move the repo out of OneDrive" if in_onedrive else "no"
    )

    return [
        ("Python version", f"{current} ({version_status})"),
        ("Required", required),
        ("Operating system", f"{platform.system()} {platform.release()}"),
        ("Script folder", str(script_folder)),
        ("Inside OneDrive", onedrive_status),
    ]


def print_report(rows: list[tuple[str, str]]) -> None:
    width = max(len(label) for label, _ in rows)
    print("Warehouse Management Learning Lab - Setup check")
    print(LINE)
    for label, value in rows:
        print(f"{label:<{width}} : {value}")
    print(LINE)


def main() -> int:
    print_report(build_rows())
    if not python_is_recent_enough():
        print("Result: FAILED - install a newer Python.")
        return 1
    print("Result: READY - you can start 02-variables.")
    return 0


if __name__ == "__main__":
    # sys.exit passes main()'s 0 or 1 to the terminal as the exit code
    sys.exit(main())