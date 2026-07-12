# Project: Deleting Unneeded files.

import os


def findLargeFiles(folder, maxSize=100):
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            path = os.path.join(foldername, filename)
            size = os.path.getsize(path)
            sizeMB = size / (1024 * 1024)
            if sizeMB > maxSize:
                print(f"{path} ->{sizeMB:.2f} MB")


findLargeFiles("/Users")
