# Finding patterns of text without Regular Expressions.


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


print("444-444-4444 is a phone number:")
print(isPhoneNumber("444-444-4444"))


message = "call me at 333-333-3333 tomorrow. 222-222-222-2222 is my office."
for i in range(len(message)):
    check = message[i : i + 12]
    if isPhoneNumber(check):
        print("Phone number found:", check)
print("Done")

# Finding patterns of text with Regular Expressions.
import re

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phoneNumRegex.search("My number is 999-999-9999")
print("Phone Number is:", mo.group())

# More pattern Matching with Regular Expressions
import re

PhoneNumRegex = re.compile(r"(\(\d\d\d\)) (\d\d\d\-\d\d\d\d)")
mo = PhoneNumRegex.search("My number is (333) 333-3333")
print(mo.group(1))  # result is (333)
print(mo.groups())  # result is ('333', '333-3333')

areaCode, mainNumber = mo.groups()
print(areaCode)  # result 333
print(mainNumber)  # result 333-3333

batRegex = re.compile(r"bat(man|mobile|copter|bet)")
mo = batRegex.search("batmobile, batman ")
print(mo.group())  # result batmobile
print(mo.group(1))  # result mobile

batRegex = re.compile(r"Bat(wo)?man")
mo1 = batRegex.search("The Advantures of Batman")
print(mo1.group())  # result Batman
mo2 = batRegex.search("the Advantures of Batwoman")
print(mo2.group())  # result Batwoman

BatRegex = re.compile(r"Bat(wo)*man")
mo = BatRegex.search("is Batwowowowoman")
print(mo.group())  # result Batwowowowoman

# Greedy and Nongreedy Matching

HaRegex = re.compile(r"(Ha){3,4}")
mo = HaRegex.search("HaHaHaHaHaHa")
print(mo.group())  # result HaHaHaHa
haRegex = re.compile(r"(ha){3,5}?")
mo = haRegex.search("hahahahahaha")
print(mo.group())  # result hahaha

# The findall() Method

PhoneNumber = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")  # has no groups
mo = PhoneNumber.findall("999-888-7777, 333-444-5555")
print(mo)  # result ['999-888-7777', '333-444-5555']

PhoneNumber = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")  # has groups
mo = PhoneNumber.findall("999-888-7777, 333-444-5555")
print(mo)  # result ('999', '888', '7777'), ('333', '444', '5555')]

# The Wildcard Character

atRegex = re.compile(r".at")
at = atRegex.findall("cat the falt hat in")
print(at)  # result ['cat', 'hat']

# The sub() Method
namesRegex = re.compile(r"Agent \w+")
name = namesRegex.sub(
    "CENSORED", "Agent Ailce gave the secret documents to Agent Bob. "
)
print(name)

nameRegex = re.compile(r"Agent (\w)\w*")
Nmae = namesRegex.sub(r"\****", "Agent Ailce told Agent Bob")
print(Nmae)
