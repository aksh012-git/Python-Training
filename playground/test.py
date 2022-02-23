# from collections import Counter

# myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# print(myList)

# myList = Counter(myList)
# print(myList)

# print(myList.items())
# print(myList.keys())
# print(myList.values())


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

x = int(input())
y = int(input())
z = int(input())
n = int(input())
final = []

# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i+j+k == n:
#                 continue
#             final.append([i,j,k])


final = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
print(final)