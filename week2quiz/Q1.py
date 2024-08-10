"""
Write a program to move a file in directory 'source' and copy it to 'destination'. Handle necessary exceptions:
1. if file does not exists in source, print "no file found in source".
2. if same file already exists in target, print "file with same name already exists"
shutil.move(source_path, destination_path)
"""

import shutil
import os

try:
    print(os.getcwd())
    os.mkdir("source")
    f = open("source/f1.txt", "x")
    f.close

    print(os.getcwd())
    os.mkdir("destination")
    #shutil.move("source/f1.txt","destination/f1.txt")
    shutil.copy("source/f1.txt","destination/f1.txt")
    

except FileNotFoundError:
    print("no file found in source")

except FileExistsError:
    print("file with same name already exists")