import sys
import unittest

import main


# autograding submodule might not be successfully pulled on init
# if unsuccessful, we have to pull it manually
# limit number of retries
MAX_RETRIES = 5
retries = 0

while "autograding" not in sys.modules:
    try:
        import autograding
        from autograding.case import FuncCall, InOut, RecursiveCall
    except ImportError:
        import subprocess
        subprocess.run(["git", "submodule", "update", "--init"])
        retries += 1
    if retries >= MAX_RETRIES:
        sys.exit("[import autograding] Too many retries, exiting")


class TestMyRecursive(autograding.TestRecursive):
    def setUp(self):
        self.testcases = [
            RecursiveCall(module=main,
                          func=main.reverse,
                          args=("",),
                          ans="",
                          output="",
                          basecase=True),
            RecursiveCall(module=main,
                          func=main.reverse,
                          args=("1",),
                          ans="1",
                          output="",
                          basecase=True),
            RecursiveCall(module=main,
                          func=main.reverse,
                          args=("12345",),
                          ans="54321",
                          output="",
                          basecase=False),
            RecursiveCall(module=main,
                          func=main.is_palindrome,
                          args=("",),
                          ans=True,
                          output="",
                          basecase=True),
            RecursiveCall(module=main,
                          func=main.is_palindrome,
                          args=("a",),
                          ans=True,
                          output="",
                          basecase=True),
            RecursiveCall(module=main,
                          func=main.is_palindrome,
                          args=("racecar",),
                          ans=True,
                          output="",
                          basecase=False),
            RecursiveCall(module=main,
                          func=main.is_palindrome,
                          args=("aloe vera",),
                          ans=False,
                          output="",
                          basecase=False),
    ]


if __name__ == '__main__':
    import os
    if not os.listdir("autograding"):
        import subprocess
        subprocess.run(["git", "submodule", "update", "--init"])
    unittest.main()
