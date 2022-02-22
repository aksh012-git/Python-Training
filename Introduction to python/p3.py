# Write a Python program to find common divisors between two numbers in a given pair

def gcdOfTwoNumber(a,b):
    if (a == b):
        return a
    
    if (a > b):
        return gcdOfTwoNumber(a-b, b)
    else:
        return gcdOfTwoNumber(a, b-a)
 
a = int(input("Enter a: "))
b = int(input("Enter b: "))
if(gcdOfTwoNumber(a, b)):
    print(gcdOfTwoNumber(a, b))
    
    
# ------------------------------------------------------------------------------------------------
import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(math.gcd(a,b))



# ------------------------------------------------------------------------------------------------

# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# a1 = a
# b1 = b
# x= 2
# y= 2
# x1 = []
# y1 = []

# while a>1:
#     if a%x == 0:
#         x1.append(x)
#         a = int(a/x)
#     else:
#         x = x + 1
        
# while b>1:
#     if b%y == 0:
#         y1.append(y)
#         b = int(b/y)
#     else:
#         y = y + 1
        
# print(x1,y1)


    
        
            
            
        