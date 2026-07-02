# use daf
def hello(name):
    print("hello", name)


hello("jim")
hello("bob")

import random


def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is certain"
    elif answerNumber == 2:
        return "It is decidely so"
    elif answerNumber == 3:
        return "Ok"
    elif answerNumber == 4:
        return "Reply hazy try again"
    elif answerNumber == 5:
        return "Ask again later"
    elif answerNumber == 6:
        return "Concertrate and ask again"
    elif answerNumber == 7:
        return "My reply is no"
    elif answerNumber == 8:
        return "Outlook not so good"
    elif answerNumber == 9:
        return "Very dountful"


r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

# Local and Global varibles whit the same name


def spem():
    eggs = "spem local"
    print(eggs)


def bacon():
    eggs = "bacon local"
    print(eggs)
    spem()
    print(eggs)


eggs = "global"
bacon()
spem()
print(eggs)

# The global statement


def ham():
    global eggs
    eggs = 22


eggs = 55
print(eggs)
ham()
print(eggs)
print(eggs)

# Exception handing


def bob(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: Ivalid argument")


print(bob(2))
print(bob(12))
print(bob(0))
print(bob(1))
