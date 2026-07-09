# files and file path
import os

print(os.getcwd())
print(os.path.join("usr", "bin", "spam"))

myfiles = ["hh.txt", "tt.csv", "jj.docx"]
for filename in myfiles:
    print(os.path.join("C:\\User\\asweigart", filename))

f = open("hh.txt", "w")
f.write("hello\n")
f.close()
f = open("hh.txt", "a")
f.write("hi")
f.close()

print(os.path.abspath("."))
print(os.path.abspath(".//add"))
print(os.path.isabs(os.path.abspath(".")))

os.chdir("/Users")
print(os.getcwd())
print(os.listdir())

path = "/Users/name/Desktop/cale.exe"
print(os.path.basename(path))  # result cale.exe
print(os.path.dirname(path))  # result "/Users/name"

print(os.path.split(path))  # result ("/Users/name/Desktop", "cale.exe")

print(path.split(os.path.sep))  # result ['', 'Users', 'name', 'Desktop', 'cale.exe']

print(os.path.getsize("/Users"))

totalSize = 0
for filename in os.listdir("/Users"):
    totalSize = totalSize + os.path.getsize(os.path.join(("/Users")))
print(totalSize)

F = open("/Users/Desktop/ATMTBRSF/hh.txt")
R = F.read()
print(R)  # result hello

import shelve

shelfile = shelve.open("/Users/Desktop/mydata")
shelfile["cats"] = ["Zophie", "Pooka", "Simon"]
shelfile.close()

shelfile = shelve.open("/Users/Desktop/mydata")
print(shelfile["cats"])
shelfile.close()

shelfile = shelve.open("/Users/Desktop/mydata")
print(list(shelfile.keys()))
list(shelfile.values())
shelfile.close()

import pprint
cats = [{"name": "Zophie", "desc": "chubby"}, {"name": "Pooka", "desc": "fluffy"}]
pprint.pformat(cats)
fileObj = open("/Users/ATMTBRSF/Code/myCats.py", "w")
fileObj.write("cats = " + pprint.pformat(cats) + "\n" )
fileObj.close()

import myCats
print(myCats.cats)
