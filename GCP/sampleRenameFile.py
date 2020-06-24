#! #!/usr/bin/env python3

# PURPOSE: Example for how to change the name of photos in a folder

import os

folderName = input("Enter the folder name where the photos are located: ")
os.chdir(dirname)
folderList = os.listdir()

photoNumber = 1
for filename in folderList:
    if filename.endswith('.jpg'):
        newname = "PhotoLabel"+str(photoNumber)+".jpg"
        os.rename(filename,newname)
        photoNumber += 1
