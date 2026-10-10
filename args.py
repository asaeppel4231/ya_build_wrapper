import argparse

# ---------------------------------------------------------------------------
# Argument parsing and main logic
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ci", action="store_true", help="Enable CI mode")
    parser.add_argument("--fail-if-build-failed", action="store_true", help="Fails CI if last build had errors")
    parser.add_argument("--quiet", action="store_true", help="Disable output to stdout")
    parser.add_argument("--output-job-time-as-json", action="store_true", help="Stores the execution times of the jobs as JSON")
    parser.add_argument("--gui", action="store_true", help="Opens the graphical user interface frontend")
    return parser.parse_args()
