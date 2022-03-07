# Convert any lower case string to upper case without in-built python functions.
# 			Ex. A = “abcdef ghi”
# 			Output: “ABCDEF GHI

a = 'abcdef ghiz'
b=''
for item in a:
    if  ord(item)-32 in range(65,91):
        b = b+chr(ord(item)-32)
    else: 
        b = b+item
           
print(b)