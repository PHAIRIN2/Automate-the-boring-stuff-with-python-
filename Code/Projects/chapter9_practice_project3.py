# Project: Filling In The Gaps.
import re, os

folder = "/Users/SpamTest"
prefix = "spam"

pattern = re.compile(r"^(%s)(\d+)(\.txt)$" % prefix)
files = []

print("Files in folder:")
for filename in os.listdir(folder):
    print("->", filename)
    mo = pattern.match(filename)
    if mo:
        print("  Matched! group2=", mo.group(2))
        files.append((int(mo.group(2)), filename))
print("Matched files:", files)
files.sort()
print("Sorted:", files)
for i, (num, filename) in enumerate(files):
    expectedNum = i + 1
    if num != expectedNum:
        newName = prefix + str(expectedNum).zfill(3) + ".txt"
        oldPath = os.path.join(folder, filename)
        newPath = os.path.join(folder, newName)
        print(f"Renaming {filename} -> {newName}")
        os.rename(oldPath, newPath)

print("Done!")
