import os
class StorageCreater:
    @staticmethod
    def createNewFolders(self, storage):
        if(not os.path.exists(storage)):
            os.mkdir(storage)
        if(not os.path.exists(os.mkdir(os.path.join(self.storage, "Pictures")))):
            os.mkdir(os.path.join(self.storage, "Pictures"))
        if(not os.path.exists(os.mkdir(os.path.join(self.storage, "Videos")))):    
            os.mkdir(os.path.join(self.storage, "Videos"))
        if(not os.path.exists(os.mkdir(os.path.join(self.storage, "Documents")))):
            os.mkdir(os.path.join(self.storage, "Documents"))
        if(not os.path.exists(os.path.join(self.storage, "Others"))):
            os.mkdir(os.path.join(self.storage, "Others"))

class DownloadsFolder:
    @staticmethod
    def Downloads(directory):
        for file in os.listdir(directory):
            if(file.split(",")[1] == ("png" or "jpg" or "bmp" or "gif")):
                