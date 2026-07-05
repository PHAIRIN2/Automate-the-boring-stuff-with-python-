# The dictionnary data type

myCat = {"size": "fat", "color": "white", "disposition": "loud"}
print(myCat["size"])  # result is fat

# Birthdays database
birthdays = {"bob": "Apr 1", "alice": "Dec 5", "pop": "Jul 22"}

while True:
    print("Enter a name: (blank to quit)")
    name = input()
    if name == "":
        break
    if name in birthdays:
        print(birthdays[name], "is the birthday of", name)
    else:
        print("I do not have birthday information for", name)
        print("What is their birthday?")
        bday = input()
        birthdays[name] = bday
        print("birthdays database update.")

# The keys(), values() and items() Methods

spam = {"name": "bob", "age": 43}
for v in list(spam.keys()):
    print(v)

for m in spam.values():
    print(m)

for j in spam.items():
    print(j)

for k, v in spam.items():
    print("keys:", k, "Values:", str(v))

# The get() Method

picnicItems = {"eggs": 2, "cups": 3}
print(
    "I'm bringing", str(picnicItems.get("cups", 2)), "cups"
)  # result is I'm briging 3 cups
print(
    "I'm bringgin", str(picnicItems.get("water", 9)), "bottles"
)  # result is I'm briging 9 bottles

# The setdefault() Method

myDog = {"name": "tt", "size": "tiny"}
myDog.setdefault("color", "black")
print(myDog)  # {'name': 'tt', 'size': 'tiny', 'color': 'black'}

# Pretty printing
import pprint

message = "hello hi"
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
