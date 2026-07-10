import shutil, os

# copying Files and Folders
os.chdir("/Users")
shutil.copy("/Users/bacon.txt", "/Users/bacon2.txt")

shutil.copy("/Users/bacon.txt", "/Users/bacon_backup")

# Moving And Renaming Files and Folders

shutil.move("/Users/bacon_backup", "/Users/bacon_backup2")

# Permanenly Deleting files and

folder = "/Users"

for filename in os.listdir(folder):
    full_path = os.path.join(folder, filename)
    print("found:", full_path)
    if filename.endswith(".rxt"):
        os.unlink(full_path)
        print("deleted:", full_path)

# safe deletes with the send2trash Module.

import send2trash

baconFile = open("/Users/bacon.txt", "a")
baconFile.write("bacon is not a vegetable.")

baconFile.close()
send2trash.send2trash("/Users/bacon.txt")

# Walking a Directory tree
import os

for foldername, subfolders, filenames in os.walk("/Users"):
    print("The current floder is :", foldername)

    for subfolder in subfolders:
        print("SUBFOLDER OF", foldername, ":", subfolder)

    for filename in filenames:
        print("FILE INSIDE", foldername, ":", filename)

    print("")

# Reading zip files

import zipfile, os

os.chdir("/Users")
exampleZip = zipfile.ZipFile("example.zip")
print(exampleZip.namelist())

spamInfo = exampleZip.getinfo("spam.txt")
print(spamInfo.file_size)
print(spamInfo.compress_size)

print(
    "compress file is %sx smaller!"
    % (round(spamInfo.file_size / spamInfo.compress_size, 2))
)  # old style

print(
    f"compress file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!"
)  # new style

# extracting from zip files

exampleZip = zipfile.ZipFile("example.zip")
print(exampleZip.extract("spam.txt"))
exampleZip.close()

# Greating and adding to ZIP files

Newzip = zipfile.ZipFile("new.zip", "w")
Newzip.write("spam.txt", compress_type=zipfile.ZIP_DEFLATED)
Newzip.close()
