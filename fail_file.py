import sys
import os

FAIL_PATH = "FAIL"

# ---------------------------------------------------------------------------
# FAIL file handling
# ---------------------------------------------------------------------------

def write_fail_file(process_returncode: int, command: str, cwd: str):
    """Write a FAIL file describing the failed command and exit with code 0.

    This is used in CI mode so that logs can still be collected even if a
    command fails.
    """
    with open(FAIL_PATH, "w") as fp:  # Overwrite existing fail file
        fp.write(str(process_returncode) + "\n")
        fp.write(str(command) + "\n")
        fp.write(str(cwd) + "\n")
    sys.exit(0)  # bypass errors to can get logs if the command fails


def read_fail_file():
    """Read FAIL file and return a dict with returncode, command, workdir, or None."""
    if not os.path.exists(FAIL_PATH):
        return None

    with open(FAIL_PATH) as fail_file:
        returncode = fail_file.readline().strip()
        command = fail_file.readline().strip()
        workdir = fail_file.readline().strip()

    try:
        returncode = int(returncode)
    except ValueError:
        returncode = -1

    return {
        "returncode": returncode,
        "command": command,
        "workdir": workdir,
    }


def fail_if_ci_build_failed():
    """Fails CI if last build had errors."""
    fail = read_fail_file()
    if fail is None:
        return

    print(
        "In directory "
        + fail["workdir"]
        + " : Command "
        + fail["command"]
        + " failed with return code "
        + str(fail["returncode"])
        + " ."
    )
    sys.exit(-1)
