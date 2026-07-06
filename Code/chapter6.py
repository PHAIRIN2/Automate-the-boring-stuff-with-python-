# Woking With String

spam = "that is alice's \tcat."
print(spam)  # result that is alice's    cat.
print(r"that is alice\'s cat.")

print("""hello
what is 
your name?""")


# comment multiline
def spam():
    """this is multiline comment to help explain what the spam() function does."""
    print("hello")


spam()

# indexing and slicing strings
spam = "Hello World!"
fizz = spam[:5]
print(fizz)  # result is Hello

# The upper(), lower(), isupper() and islower() String Methous.

spam = "Hello World"
spam = spam.upper()  # result is HELLO WORLD
spam = spam.lower()  # result is hello world

print("How are you?")
feeling = input()
if feeling.lower() == "great":
    print("I feel great too.")
else:
    print("I hope the rest of your day is good.")

# The isX string Methous

while True:
    print("Enter your age:")
    age = input()
    if age == "":
        break
    elif age.isdecimal():
        print("your age is", str(age), "Thinkyou.")
        break


while True:
    print("Select a new password (letters and numbers only):")
    password = input()
    if password == "":
        break
    elif password.isalnum():
        break
    print("Password can only have letters and numbers.")

# The startswith() and endswith() String Methous.

spam = "Hello World"
spam = spam.startswith("Hello")
print(spam)

# The join() and split() String Methous

print(" ".join(["ff", "dd", "oo"])) # result  ff dd oo
print("myABCisABCSimonABC".split("ABC")) # result ['my', 'is', 'Simon', '']
spam = """H
E
L
L
O"""
print(spam.split("\n")) #result ['H', 'E', 'L', 'L', 'O']

# Justifying Text with rjust(), ljust() and center()

print("Hello".rjust(20,"*")) #result ***************Hello

print("Hello".ljust(20,"-")) # result Hello---------------

print("Hello".center(20,"=")) # result =======Hello========

# PicnicTable

def printPicnic(itemsDict, leftWidth, rightWidth):
    print("Picnic Items".center(leftWidth + rightWidth, "."))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, ".") + str(v).rjust(rightWidth, " "))

PicnicItems = {"sandwiches": 4, "apples": 3, "cups": 4, "cookies": 1000}
printPicnic(PicnicItems, 20, 6)

# strip(), rstrip() and lstrip()

spam = "Hello"
spam = spam.rstrip("o")
print(spam) # result Hell

spam = spam.lstrip("H")
print(spam) # result ell

spam = spam.strip("l")
print(spam) # result e

# copying and pasting String with pypercilp Module
import pyperclip
pyperclip.copy("bacon")
pyperclip.paste()

