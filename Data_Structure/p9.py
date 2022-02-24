# Count the subsequence “AG” in the given string.
# 			Ex. S = “BCAHGBNAJKGTYUALKWG”
# 			Output: 6



string = "AKSHMARADIYAakshMARADIYAAKSHAKSH"
find_str = "AKSH"
print(string.count(find_str))


#------------------------------------------------------------------------------------------- 

string = "AKSHMARADIYAakshMARADIYAAKSHAKSH"
find_str = "AKSH"
flag = False
count = 0

for index,item in enumerate(string):
       if find_str[0] == item:
           x = index
           for itm in find_str:
               if x<len(string) and itm == string[x]:
                   flag = True
                   x += 1
               else:
                   flag = False
                   break
           if flag:
                count += 1
                
print(count)
            
                
                   
                   
               
               
               
               