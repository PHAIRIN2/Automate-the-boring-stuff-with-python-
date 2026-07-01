# else

print("Welcome to my world . What your name: ")
name = input()

if name == "":
    print("Hi")
else:
    print(f"Hi, {name}")

# elif

print("How old are you:")
age = int(input())
if age < 12:
    print("You are a Child")
elif age >= 200:
    print("Seriously!")
elif age > 20:
    print("You are an Adult")

# while, continue and break

while True:
    print("Who are you?")
    name2 = input()
    if name2 != "Joe":
        continue
    print("Hello, Joe. What is the password?)")
    password = input()
    if password == "iloveyou":
        break
print("Accsee granted.")

# TRUTHY and FALSEY

name3 = ""
while not name3:
    print("Enter your name:")
    name3 = input()
print("How many gusets will you have?")
number0fGuests = input()
if number0fGuests:
    print("Be sure to have enough room for all your guests")
print("DONE")

# range()

total = 0
for num in range(101):
    total = total + num
print(total)

# import random

import random

for i in range(5):
    print(random.randint(1, 10))

# import sys

import sys

while True:
    print("Type exit to exit.")
    response = input()
    if response == "exit":
        sys.exit()
    print("you typed" + response + ".")
