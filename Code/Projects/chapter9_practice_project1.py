# Project: Selective Copy.
import os, shutil


def selecticecopy(folder, extension, destFolder):
    os.makedirs(destFolder, exist_ok=True)
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith(extension):
                src = os.path.join(foldername)
                shutil.copy(src, destFolder)
                print(f"copied: {filename}")


selecticecopy("/Users", ".pdf", "/Users/PDFs")
