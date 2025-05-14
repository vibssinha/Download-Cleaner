import os
class StorageCreater:
    def __init__(self, storage):
        if(not os.path.exists(storage)):
            os.mkdir(storage)
        else:
            if not os.path.exists('C:\\Users\\Vibs Kumar\\Storage\\Pictures'):
                os.mkdir('C:\\Users\\Vibs Kumar\\Storage\\Pictures')
            if not os.path.exists('C:\\Users\\Vibs Kumar\\Storage\\Videos'):
                os.mkdir('C:\\Users\\Vibs Kumar\\Storage\\Videos')
            if not os.path.exists('C:\\Users\\Vibs Kumar\\Storage\\Documents'):
                    os.mkdir("C:\\Users\\Vibs Kumar\\Storage\\Documents")
            if not os.path.exists('C:\\Users\\Vibs Kumar\\Storage\\Others'):
                os.mkdir("C:\\Users\\Vibs Kumar\\Storage\\Others")
        self.storage = storage

    def createNewFolders(self):
        if(not os.path.exists(os.mkdir(os.path.join(self.storage, "Pictures")))):
            os.mkdir(os.path.join(self.storage, "Pictures"))
        if(not os.path.exists(os.mkdir(os.path.join(self.storage, "Videos")))):    
            os.mkdir(os.path.join(self.storage, "Videos"))
        if(not os.path.exists(os.mkdir(os.path.join(self.storage, "Documents")))):
            os.mkdir(os.path.join(self.storage, "Documents"))
        if(not os.path.exists(os.path.join(self.storage, "Others"))):
            os.mkdir(os.path.join(self.storage, "Others"))
