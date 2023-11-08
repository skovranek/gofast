"""Module providing function to check Go lang is installed."""
import subprocess

def go1_21() -> bool:
    """Run 'go version' to check it is 1.21 or later."""
    try:
        go_version = subprocess.run(
            'go version',
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        if go_version.stdout[:16] == 'go version go1.2':
            if int(go_version.stdout[15:17]) > 20:
                return True
    except Exception as e:
        print(e)

    print('Go version go1.21 or later must be installed')
    return False
