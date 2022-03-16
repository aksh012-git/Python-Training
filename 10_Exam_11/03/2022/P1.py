from itertools import count
import gdown
import zipfile
import os
import string
import random
import shutil

# ----------------------------------------------------------------------------------------------------------------------
# download From url

url = "https://drive.google.com/file/d/1Aeh4GIjLwyiuWGd6AGxM8Q3WgiffLfIu/view?usp=sharing"
output = "Exam.zip"
obj = gdown.download(url, output, quiet=False,fuzzy=True)


#----------------------------------------------------------------------------------------------------------------------
#unzip Exam.zip

pathOfUnzipFolder = '/home/wot-aksh/Desktop/Python_Training/10_Exam_AI_ML/'

with zipfile.ZipFile('/home/wot-aksh/Desktop/Python_Training/Exam.zip', 'r') as zip_ref:
    zip_ref.extractall(pathOfUnzipFolder)
    
    
#----------------------------------------------------------------------------------------------------------------------
# created output folder and add one file in which all text.txt file paths

try:
    pathOfOutputFolder = pathOfUnzipFolder + 'Output/'
    os.mkdir(pathOfOutputFolder)
except:
    pass
finally:
    pathOfTxtFile = pathOfOutputFolder + 'textFilePaths.txt'

    openpathOfTxtFile = open(pathOfTxtFile,"w+")

    root = pathOfUnzipFolder + 'Exam/'

    for root, dirs, files in os.walk(root):  
        for f in files:
            openpathOfTxtFile.write(os.path.join(root, f) + '\n')
            
    openpathOfTxtFile.close()


#----------------------------------------------------------------------------------------------------------------------
#generet random name and add into file and change name of files

readfile = open(pathOfTxtFile)

linesList = readfile.read().splitlines()

abcd_list = []
abcd_list[:] = string.ascii_uppercase

count_of_file = 0
for pathOfFile in linesList:
    openTxtFile = open(pathOfFile,'w')
    random_name_length = random.randint(3,7)
    random_name = ''
    for i in range(random_name_length):
        random_name = random_name + abcd_list[random.randint(0,25)]
    openTxtFile.write(random_name)
    openTxtFile.close()
    pathOfstring = pathOfFile.split('Exam')[2]
    os.rename(pathOfFile,pathOfFile.split('text.txt')[0]+ str(count_of_file)+pathOfstring.replace('/','_'))
    count_of_file += 1


#----------------------------------------------------------------------------------------------------------------------
#Add all file in Output/all_files/ folder
path = pathOfOutputFolder + 'allFiles/'
try:
    os.mkdir(path)
except:
    pass
finally:
    for pathInFile in linesList:
        
        source = pathInFile.split('text.txt')[0]
        destination = path

        allfiles = os.listdir(source)

        for item in allfiles:
            if '.txt' in item:
                shutil.move(source+item,destination+item)