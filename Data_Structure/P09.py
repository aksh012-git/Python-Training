# Count the subsequence “AG” in the given string.
# 			Ex. S = “BCAHGBNAJKGTYUALKWG”
# 			Output: 6


string = "BCAHGBNAJKGTYUALKWG"
find_str = "AG"   
count_0f_a = 0
count = 0          
            
for i in string:
    if i == 'A':
        count_0f_a += 1
    if i == 'G':
        count = count + count_0f_a
        
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
            
                
                   
                   
               
               
               
               