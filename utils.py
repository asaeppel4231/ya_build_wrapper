from rich.panel import Panel
from rich.console import Console
import sys
import os
import subprocess
import time
import shutil
from . import fail_file as failure_handling
from datetime import datetime

LOGS_DIR = "logs"

console = Console()

# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------

def cmd_tries_to_call_build_script(command: str) -> bool:
    """Return True if the command tries to call this build script."""
    return (
        command.find(sys.argv[0]) != -1
        or command.find(os.path.abspath(sys.argv[0])) != -1
        if command
        else False
    )


def command_exists(command: str) -> bool:
    """Check if the first token of the command exists in PATH."""
    if not command:
        return False
    first = str(command).split(" ")[0]
    return shutil.which(first) is not None


def prepare_logs_dir():
    """Ensure a clean logs directory."""
    if os.path.exists(LOGS_DIR):
        shutil.rmtree(LOGS_DIR)
    os.mkdir(LOGS_DIR)


def cleanup_empty_logs(logfile: str):
    """Prevents that empty files are stored in the logs (ZIP file) of the CI."""
    for suffix in ("", "_error"):
        path = os.path.join(LOGS_DIR, f"{logfile}{suffix}.log")
        if os.path.exists(path) and os.stat(path).st_size == 0:
            os.remove(path)


# ---------------------------------------------------------------------------
# Step execution
# ---------------------------------------------------------------------------

def execute_command(command: str, logfile: str, cwd: str | None) -> int:
    """Execute a shell command and return its exit code."""
    log_path = os.path.join(LOGS_DIR, f"{logfile}.log")
    err_path = os.path.join(LOGS_DIR, f"{logfile}_error.log")

    with open(log_path, "w") as log, open(err_path, "w") as err:
        proc = subprocess.Popen(
            command,
            shell=True,
            stdout=log,
            stderr=err,
            cwd=cwd,
        )
        proc.wait()

    cleanup_empty_logs(logfile)
    return proc.returncode


def print_done(ci_mode: int, duration: float):
    """Print DONE message."""
    if ci_mode:
        console.print("[bold green]DONE[/bold green]\n")
    else:
        console.print(f"[bold green]DONE ({duration:.2f}s)[/bold green]\n")


def run_step(
    title: str,
    command: str,
    logfile: str,
    cwd: str = None,
    ci_mode: bool = False,
    timings: list = None,
    auto_fail: bool = False,
    quiet: bool = False,
):
    """Run a single build step."""
    if not title or not command or not logfile:
        return

    if not quiet:
        console.print(Panel(title, title=datetime.ctime(datetime.now()), style="bold blue"))

    start_time = time.time()
    returncode = execute_command(command, logfile, cwd)

    if returncode != 0 or auto_fail:
        if not quiet:
            console.print(f"[bold red]FAILED (exit code {returncode})[/bold red]")
        if ci_mode:
            failure_handling.write_fail_file(returncode, command, cwd)
        else:
            sys.exit(returncode)

    duration = time.time() - start_time

    if timings is not None:
        timings.append((title, duration))

    if not quiet:
        print_done(ci_mode, duration)

