# Two way to append value in array

array = []
for i in range(5):
       array[len(array):] = [i]
print(array)

array = []
for i in range(5):
       array.append(i)
print(array)

# Ex - 
array = [1,2,3,4]
array[1:3] = [3,10]
print(array)

# -------------------------------------------------------------------------------
# Three way to extend array

array = [1,2,3]
array1 = [4,5,6,7]
array.extend(array1)
print(array)

array = [1,2,3]
array1 = [4,5,6,7]
array = array + array1
print(array)

array = [1,2,3]
array1 = [4,5,6,7]
array[len(array):] = array1
print(array)

# ---------------------------------------------------------------------------------
# Insert at index 
array = [1,2,3,4,6,7]
array.insert(4,5)
print(array)
   
array = [1,2,3,4,6,7]
array.insert(len(array),8)
print(array)

array = [1,2,3,4,4,4,6,7]
array[4:6] = [5]
print(array)

array = [1,2,7,8]
array1 = [3,4,5,6]
q = 0
for i in range(2,6):
   array.insert(i,array1[q])
   q=q+1
   
print(array)

# ---------------------------------------------------------------------------------
# Remove given value in list 

array = [1,2,3,4,6,7]
array.remove(3)
print(array)

# ---------------------------------------------------------------------------------
# Remove item at index
array = [1,2,3,4,6,7]
x = array.pop(2)
print(array,x)

#last index
array = [1,2,3,4,6,7]
array.pop()
print(array)

# ---------------------------------------------------------------------------------
# Clear list many way

array = [1,2,3,4,6,7]
array.clear()
print(array)

array = [1,2,3,4,6,7]
del array[3:]
print(array)

array = [1,2,3,4,6,7]
del array[:]
print(array)

# ---------------------------------------------------------------------------------
#array.index(value,starting_index,ending_index)

array = [1,4,4,2,3,4,6,7,4,4,4]
a = array.index(4,5,len(array))
print(array,a)

# --------------------------------------------------------------------------------
#count given value in list

array = [1,4,4,2,3,4,6,7,4,4,4]
a = array.count(4)
print(a)

# --------------------------------------------------------------------------------

array = [1,4,4,2,3,4,6,7,4,4,4]
a = array.sort(reverse=True)
print(a,array)

# --------------------------------------------------------------------------------
#just reverse list
array = [1,4,4,2,3,4,6,7,4,4,4]
array.reverse()
print(array)

#--------------------------------------------------------------------------------

li1 = [1, 2, 3, 4]

li2 = li1.copy()
print ("The original elements before shallow copying")
print(li1)

li2[2] = 5

print ("The original elements after shallow copying")
print(li1)


li1 = [1, 2, [2,3], 4]

li2 = li1.copy()
print ("The original elements before shallow copying")
print(li1)

li2[2][1] = 5

print ("The original elements after shallow copying")
print(li1)

#--------------------------------------------------------------------------------
# Using Lists as Stacks

a = [1,2,3]
a.append(5)
a.append(6)
print(a)
a.pop()
a.pop()
print(a)

#--------------------------------------------------------------------------------
# Using Lists as Queues

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           
queue.append("Graham")
print(queue)        
queue.popleft()               
queue.popleft()               
print(queue)     


from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.appendleft("Terry")           
queue.appendleft("Graham")
print(queue)        
queue.pop()               
queue.pop()               
print(queue)    

#--------------------------------------------------------------------------------
#  List Comprehensions

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)          

squares = list(map(lambda x: x**2, range(10)))
print(squares)
     
squares = [i**2 for i in range(10)]
print(squares)


myList = []
for i in [1,2,3]:
       for j in [3,1,4]:
              if i != j:
                     myList.append((i,j))
print(myList)
                  

myList = [(i,j)  for i in [1,2,3] for j in [3,1,4] if i!=j]
print(myList)


#--------------------------------------------------------------------------------
# Nested List Comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

final = [[row[i] for row in matrix] for i in range(4)]
print(final)

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

#--------------------------------------------------------------------------------
# tuple
t = 1212,1331,3,131,'sdfsdfs';
print(t)

u = t,1212,1212,1212;
print(u)


print(u[0])
print(u[0][0])

u[1] = 232
print(u)

a = 'aksh Maradiya'
print(len(a),a)

a  = 'aksh maradiya',
print(len(a),a)
print(a[0])

# paking
t = 23,23,2,
x, y, z = t
print(x,y,z)

#unpaking
t = 23,23,2,'aaa'
x, y, z, m = t
print(x,y,z,m)

#--------------------------------------------------------------------------------
#set

basket = {'apple', 'orange','apple', 'pear', 'orange', 'banana'}
print(basket)

x = set('akshaksh')
print(x)
y = set('maradiyaMaradiya')
print(y)

print(x|y)
print(x&y)

#--------------------------------------------------------------------------------
#dictionary

tel = {'jack': 4098, 'sape': 4139, 'aksh':2323}
array = list(tel)
print(tel,array)

array = sorted(tel)
print(tel,array)

print(dict([('sape',4139)], guido=4127, jack=4098))

#--------------------------------------------------------------------------------
#When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

#--------------------------------------------------------------------------------

for i in reversed(range(1, 10)):
    print(i)

#--------------------------------------------------------------------------------
from collections import Counter

myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
print(myList)

myList = Counter(myList)
print(myList)

print(myList.items())
print(myList.keys())
print(myList.values())

#--------------------------------------------------------------------------------