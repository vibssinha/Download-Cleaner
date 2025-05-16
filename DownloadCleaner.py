from Files import FileEditor
import os
import shutil

user_folder = input("Enter the name of your folder who's downloads you want to clear out? ")
cleaner = FileEditor(os.path.join("C:", "Users", user_folder, "Downloads"))
cleaner.createNewFolders()
cleaner.move()