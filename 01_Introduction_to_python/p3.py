# Write a Python program to find common divisors between two numbers in a given pair

def gcdOfTwoNumber(inputNumber1,inputNumber2):
    if (inputNumber1 == inputNumber2):
        return inputNumber1
    
    if (inputNumber1 > inputNumber2):
        return gcdOfTwoNumber(inputNumber1-inputNumber2, inputNumber2)
    else:
        return gcdOfTwoNumber(inputNumber1, inputNumber2-inputNumber1)
 
inputNumber1 = int(input("Enter inputNumber1: "))
inputNumber2 = int(input("Enter inputNumber2: "))
if(gcdOfTwoNumber(inputNumber1, inputNumber2)):
    print(gcdOfTwoNumber(inputNumber1, inputNumber2))
    
    
# ------------------------------------------------------------------------------------------------
import math
inputNumber1 = int(input("Enter inputNumber1: "))
inputNumber2 = int(input("Enter inputNumber2: "))
print(math.gcd(inputNumber1,inputNumber2))

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


    
        
            
            
        