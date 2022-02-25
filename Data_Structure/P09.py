# Count the subsequence “AG” in the given string.
# 			Ex. S = “BCAHGBNAJKGTYUALKWG”
# 			Output: 6


string = "BCAHGBNAJKGTYUALKWG"
find_str = "AG"
count = 0
for item in string:
    if find_str[0] == item:
       count+=1
    elif find_str[1] == item:
        count+=1
print(count)
       

#------------------------------------------------------------------------------------------- 

string = "BCAHGBNAJKGTYUALKWG"
find_str = "AG"
count = 0
for item in find_str:
    for itm in string:
        if itm == item:
            count += 1
# print(count)



#-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
 
#for count substring

string = "AKSHMARADIYAakshMARADIYAAKSHAKSH"
find_str = "AKSH"
# print(string.count(find_str))


#------------------------------------------------------------------------------------------- 

string = "AAKSHMARADIYAakshMARADIYAAKSHAKSH"
find_str = "AKSH"
flag = False
count = 0

for index,item in enumerate(string):
       if find_str[0] == item:
           x = index
           flag = True
           for itm in find_str:
               if x<len(string) and itm == string[x]:
                   x += 1
               else:
                   flag = False
                   break
           if flag:
                count += 1
                
# print(count)
            
                
                   
                   
               
               
               
               