import gdown
import zipfile
import csv
import pandas as pd

url = "https://drive.google.com/file/d/1kuwj_EJ2aUeYxtQkYxUhbb52D0_SFGcE/view"
output = "filesstep1.zip"
obj = gdown.download(url, output, quiet=False,fuzzy=True)


pathOfUnzipFolder = '/home/wot-aksh/Desktop/Python_Training/exam_14_04_2022/Unzipfilesstep1'

with zipfile.ZipFile('/home/wot-aksh/Desktop/Python_Training/filesstep1.zip', 'r') as zip_ref:
    zip_ref.extractall(pathOfUnzipFolder)
      
      
ml_user_file = pd.read_csv(pathOfUnzipFolder + '/ML-1-1Use-1-210720201428.csv')

list_of_FFTs_column = []


for column_name in ml_user_file.columns:
    if 'FFT' in column_name:
        list_of_FFTs_column.append(column_name)
        
ml_user_file  = ml_user_file[list_of_FFTs_column]


with open('/home/wot-aksh/Desktop/Python_Training/exam_14_04_2022/output_file.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(list_of_FFTs_column)
    no_of_row_in_ml_user_file = ml_user_file.shape[0]
    starting_row = 0
    while (starting_row +  4) <= no_of_row_in_ml_user_file:
        writer.writerow((ml_user_file.iloc[starting_row:(starting_row+4),:]).sum())
        starting_row = starting_row +  1
        
    
    

