from email.policy import strict
import string


stirng = '/home/wot-aksh/Desktop/Python_Training/Exam/Folder/text.txt'
strrr = '/home/wot-aksh/Desktop/Python_Training/Exam/Folder/text.txt'.split('text.txt')[0]+'text1.txt'
dstr = strrr.replace("/", "_")

print(dstr)

