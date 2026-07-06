#! python3

PASSWORD = {"program": "fjfjfjfjfjfjfjfjjfj",
            "newprogram": "jfjfjfjfjfjfjfj",
            "oldprogram":"cn;adjfejewpo"}

import sys, pyperclip
if len(sys.argv) < 2:
    print("Using: py pw.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]

if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print("Password for" + account + "copied to cilpboard.")
else:
    print("There is no account named" + account)
