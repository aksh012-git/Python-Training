# Convert any lower case string to upper case without in-built python functions.
# 			Ex. A = “abcdef ghi”
# 			Output: “ABCDEF GHI

lowerCaseString = 'abcdef ghiz'
upperCaseString=''
for item in lowerCaseString:
    if  ord(item)-32 in range(65,91):
        upperCaseString = upperCaseString+chr(ord(item)-32)
    else: 
        upperCaseString = upperCaseString+item
           
print(upperCaseString)