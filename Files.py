import os
import shutil

class FileEditor:
    def __init__(self, storage):
        self.storage = storage

    def createNewFolders(self):
        if(not os.path.exists(self.storage)):
            os.mkdir(self.storage)
        if(not os.path.exists(os.path.join(self.storage, "Pictures"))):
            os.mkdir(os.path.join(self.storage, "Pictures"))
        if(not os.path.exists(os.path.join(self.storage, "Videos"))):    
            os.mkdir(os.path.join(self.storage, "Videos"))
        if(not os.path.exists(os.path.join(self.storage, "Documents"))):
            os.mkdir(os.path.join(self.storage, "Documents"))
        if(not os.path.exists(os.path.join(self.storage, "Others"))):
            os.mkdir(os.path.join(self.storage, "Others"))
    
    def move(self):
        for file in os.listdir(os.path.join(self.storage, "Downloads")):
            if(file.split(".")[1] in ("png", "jpg", "bmp", "gif", "avif")):
                shutil.move(os.path.join(self.storage, "Downloads", file), os.path.join(self.storage, "Pictures")) #Make sure you add the actual file otherwise you're moving the directory
            elif(file.split(".")[1] in ("mp4", "mov", "webm", "mpg", "ogg", "avi", "mov", "flv")):
                shutil.move(os.path.join(self.storage, "Downloads", file), os.path.join(self.storage, "Videos"))  #Make sure you add the actual file otherwise you're moving the directory
            elif(file.split(".")[1] in ("pdf", "docx", "docm", "doc", "odt", "ppt")):
                shutil.move(os.path.join(self.storage, "Downloads", file), os.path.join(self.storage, "Documents")) #Make sure you add the actual file otherwise you're moving the directory
            else:
                shutil.move(os.path.join(self.storage, "Downloads", file), os.path.join(self.storage, "Others")) #Make sure you add the actual file otherwise you're moving the directory
