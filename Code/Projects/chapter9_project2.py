# Project: Backing Up a Folder into a ZIP File
import zipfile, os


def backuptoZip(folder):
    folder = os.path.abspath(folder)
    print("Folder:", folder)
    print("Exists:", os.path.exists(folder))

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zipFilename):
            break
        number = number + 1

        print("Creating", zipFilename)
        backupZip = zipfile.ZipFile(zipFilename, "w")

        for foldername, subfolders, filename in os.walk(folder):
            print("Adding file in %s..." % (foldername))
            backupZip.write(foldername)
            for filename in filename:
                newBase = os.path.basename(folder) + "_"
                if filename.startswith(newBase) and filename.endswith(".zip"):
                    continue
                backupZip.write(os.path.join(foldername, filename))

        backupZip.close()
        print("Done!")


backuptoZip("/Users/banana/Desktop/Test")
