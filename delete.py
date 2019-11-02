"""
Defines the deleting process. Call delete() to call the deleting process.
Deletes what has previously been drawn so that things can be updated and
redrawn. Not much code here - but it can be edited if you want to some fancy
deleting (?)
Note that this requires the subprocess and sys modules in order to work.
All variables are defined in config.py and can be updated in there.
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
