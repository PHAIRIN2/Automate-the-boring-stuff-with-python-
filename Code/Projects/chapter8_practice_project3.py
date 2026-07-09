# Regex Search
import re, os

folderPath = input("Enter the older path to search:")
pattern = input ("Enter the regular expression:")

regex = re.compile(pattern)

for filename in os.listdir(folderPath):
    if filename.endwith(".txt"):
        filePath = os.path.join(folderPath, filename)
        with open(filePath) as f:
            for lineNum , line in enumerate(f, start=1):
                if regex.search(line):
                    print(f"{filename} (line {lineNum}): {line.strip()}")