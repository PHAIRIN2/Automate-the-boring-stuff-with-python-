# project: allMyCats

Catname = []
while True:
    print("Enter the name of cat:" + str(len(Catname) + 1), ("or Enter noting to stop"))
    name = input()
    if name == "":
        break
    Catname = Catname + [name]


print("The cat names are:")
for name in Catname:
    print("  ", name)

for i in str(len(Catname)):
    print("All cats have:" + str(i))

# index
supplies = ["pen", "dog", "apple", "eggs"]
for i in range(len(supplies)):
    print("index:", str(i), "in supplies is :", supplies[i])

# Magic 8 bell with a list
import random

messages = [
    "It is certain",
    "It is decidedly so",
    "Yes definitely",
    "Reply hazy try again",
    "Ask again later",
    "Concentrate and ask again",
    "My reply is no",
    "Outlook not so good",
    "Very doubtful",
]
print(messages[random.randint(0, len(messages) - 1)])
print(len(messages))

# del, append() and delete()

bacon = [1, 2, 3, 4, 5]

del bacon[1]  # result [1, 3, 4, 5]

bacon.append(10)  # result [1, 3, 4, 5, 10]

bacon.remove(5)  # result [1, 3, 4, 10]

# list() and tuple()

print(tuple([1, 2, 3, 5]))  # result (1, 2, 3, 5)

list((1, 2, 3, 5))  # result [1, 2, 3, 5]

print(list("hello"))  # result ["h", "e", "l", "l", "o"]

# copy() function
import copy

spam = [1, 3, [1, 2]]
cheese = copy.copy(spam)
cheese[0] = 99
print(spam)  # result [1, 3 [1, 2]]

cheese[2][0] = 99
print(spam)  # result [1, 3, [99, 2]]

# deepcopy() function
import copy

spam = [1, 3, [1, 2]]
cheese = copy.deepcopy(spam)
cheese[0] = 99
print(spam)  # result [1, 3 [1, 2]]

cheese[2][0] = 99
print(spam)  # result [1, 3, [1, 2]]
