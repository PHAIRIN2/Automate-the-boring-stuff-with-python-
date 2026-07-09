# Project: Mad Libs

import re

filename = input("Enter the filename to open:")

with open(filename) as f:
    content = f.read()

wordRegex = re.compile(r"ADJECTIVE|NOUN|ADVERB|VERB")


def replaceWord(matchobj):
    word = matchobj.group()
    userInput = input(f"Enter {'an' if word[0] in "AEIOU" else "a"} {word.lower()}:\n")
    return userInput


newContent = wordRegex.sub(replaceWord, content)

print("\nResult:")
print(newContent)

newFileName = filename.replace(".txt", "_madlibs.txt")
with open(newFileName, "w") as f:
    f.write(newContent)

print(f"\nSaved to {newFileName}")
