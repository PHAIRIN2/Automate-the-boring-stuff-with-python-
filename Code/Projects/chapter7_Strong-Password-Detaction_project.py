import re


def strongPassword(password):
    upperRegex = re.compile(r"[A-Z]")
    lowerRegex = re.compile(r"[a-z]")
    digitRegex = re.compile(r"\d")
    if len(password) >= 8:
        if upperRegex.search(password):
            if lowerRegex.search(password):
                if digitRegex.search(password):
                    return True
    return False


while True:
    print("Enter yor password:")
    password = input()
    if len(password) < 8:
        print("You must Enter password having at least eight characters")
        continue
    elif strongPassword(password):
        print("Well Done")
        break
    else:
        print("You must have a strong password")
