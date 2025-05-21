from Files import FileEditor
import os
import shutil

try:
    drive = input("Enter the drive whose download folder you want to clean? ")
    user_folder = input("Enter the name of your folder who's downloads you want to clear out? ")
    cleaner = FileEditor(os.path.join(drive + "\\", "Users", user_folder))
    cleaner.createNewFolders()
    cleaner.move()
except Exception as e:
    print("This file does not exist")