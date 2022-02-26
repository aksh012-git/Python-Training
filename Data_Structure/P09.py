# Count the subsequence “AG” in the given string.
# 			Ex. S = “BCAHGBNAJKGTYUALKWG”
# 			Output: 6


string = "BCAHGBNAJKGTYUALKWG"
find_str = "AG"   
array = [] 
count = 0          
            
for i in range(len(string)):
    if find_str[0]==string[i]:
        for item in string[i+1:]:
            if find_str[1] == item:
                count+=1
print(count) 


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
            
                
                   
                   
               
               
               
               