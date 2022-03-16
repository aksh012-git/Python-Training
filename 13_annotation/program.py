# import splitfolders
# splitfolders.ratio('/home/wot-aksh/Desktop/Python_Training/13_annotation/images',output='/home/wot-aksh/Desktop/Python_Training/13_annotation/output',ratio=(0.33,0.33,0.34))

import csv
import os

import re
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

root = '/home/wot-aksh/Desktop/Python_Training/13_annotation/output/aksh/TNR_LPR_cropped_images'

dirlist = sorted_alphanumeric(os.listdir(root))
# print(dirlist)
    

with open('lable_part_1.csv', 'w') as obj:
     for filename in dirlist:
         write = csv.writer(obj)
         write.writerow([filename])

