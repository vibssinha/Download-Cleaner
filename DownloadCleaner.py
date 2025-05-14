from Files import StorageCreater
import os
downloads = "C:\\Users\\Vibs Kumar\\Downloads"
files = []

for i in os.listdir(downloads):
    files.append(i)

storage = StorageCreater(os.path.join("C:","Users","Vibs Kumar","Storage"))

    

#else:
  #  if not os.path.exists('C:\\Users\\Vibs Kumar\\Storage\\Pictures'):
  #      os.mkdir('C:\\Users\\Vibs Kumar\\Storage\\Pictures')
   # if not os.path.exists('C:\\Users\\Vibs Kumar\\Storage\\Videos'):
  #      os.mkdir('C:\\Users\\Vibs Kumar\\Storage\\Videos')
   # if not os.path.exists('C:\\Users\\Vibs Kumar\\Storage\\Documents'):
    #    os.mkdir("C:\\Users\\Vibs Kumar\\Storage\\Documents")
   # if not os.path.exists('C:\\Users\\Vibs Kumar\\Storage\\Others'):
    #    os.mkdir("C:\\Users\\Vibs Kumar\\Storage\\Others")

for file in files:
    if file.split(".")[1] == "pdf" or file.split(".")[1] == "docx":

   # if file.split(".")[1] == "mp3":

  #  if file.split(".")[1] == "jpeg":

   # else:
        
