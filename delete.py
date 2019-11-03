"""
Defines the deleting process. Call delete() to call the deleting process.
Deletes what has previously been drawn so that things can be updated and
redrawn.
"""

import config
import subprocess
import sys


subprocess.call("", shell=True)


def delete_last_lines(n=1):
    """Deletes a certain number of lines back.

    Deletes n number of lines back from where the cursor is currently.
    """
    for _ in range(n):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")


def delete():
    """Main delete function. Call this to do the whole deleting thing.

    Define the variables used in delete.py for the delete() function in
    config.py.
    """
    delete_last_lines(config.lines_to_delete)
