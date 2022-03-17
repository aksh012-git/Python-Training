# from logging import root
# import pandas as pd
# import os

# df = pd.read_csv('/home/wot-aksh/Desktop/Python_Training/13_annotation/lable_3.csv')
# df = pd.DataFrame(df)
# listOfNamesInCsv = df.iloc[:,0].tolist()
# # print(list)


# root = '/home/wot-aksh/Desktop/Python_Training/13_annotation/lable_3'

# dirList = os.listdir(root)

# print(len(listOfNamesInCsv),len(dirList))

# for i in dirList:
#     if i not in listOfNamesInCsv:
#         print(i)


# importing pandas
# import pandas as pd

# # merging two csv files
# df = pd.concat(map(pd.read_csv, ['13_annotation/lable_1.csv', '13_annotation/lable_2.csv','13_annotation/lable_3.csv']))
# print(df)

# df.to_csv('13_annotation/finalFile.csv',index=False)

import shutil
import os


# Function to create new folder if not exists
def make_new_folder(folder_name, parent_folder):
	
	# Path
	path = os.path.join(parent_folder, folder_name)
	
	# Create the folder
	# 'new_folder' in
	# parent_folder
	try:
		# mode of the folder
		mode = 0o777

		# Create folder
		os.mkdir(path, mode)
	except OSError as error:
		print(error)

# current folder path
current_folder = os.getcwd()

# list of folders to be merged
list_dir = ['/home/wot-aksh/Desktop/Python_Training/13_annotation/lable_1', '/home/wot-aksh/Desktop/Python_Training/13_annotation/lable_2', '/home/wot-aksh/Desktop/Python_Training/13_annotation/lable_3']

# enumerate on list_dir to get the
# content of all the folders ans store
# it in a dictionary
content_list = {}
for index, val in enumerate(list_dir):
	path = os.path.join(current_folder, val)
	content_list[ list_dir[index] ] = os.listdir(path)

# folder in which all the content will
# be merged
merge_folder = "merge_folder"

# merge_folder path - current_folder
# + merge_folder
merge_folder_path = os.path.join(current_folder, merge_folder)

# create merge_folder if not exists
make_new_folder(merge_folder, current_folder)

# loop through the list of folders
for sub_dir in content_list:

	# loop through the contents of the
	# list of folders
	for contents in content_list[sub_dir]:

		# make the path of the content to move
		path_to_content = sub_dir + "/" + contents

		# make the path with the current folder
		dir_to_move = os.path.join(current_folder, path_to_content )

		# move the file
		shutil.move(dir_to_move, merge_folder_path)
