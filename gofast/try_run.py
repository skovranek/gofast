"""Module providing function to try invoking shell subprocesses."""
from subprocess import run


def try_run(cmd: str) -> bool:
    """Invoke shell subprocess and return bool for success."""
    try:
        run(cmd, shell=True, check=True)
    except Exception as e: # pylint: disable=broad-exception-caught
        print(e)
        return False
    return True
