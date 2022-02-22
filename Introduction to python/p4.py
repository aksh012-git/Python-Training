# Write a Python program to filter(even and odd) a list of integers using Lambda.
#  Original list of integers:
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  Even numbers from the said list:
#  [2, 4, 6, 8, 10]
#  Odd numbers from the said list:
#  [1, 3, 5, 7, 9]

listPy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
odd = []

for a in listPy:
    x = lambda q : q % 2
    if x(a):
        odd.append(a)
    else:
        even.append(a)
        
print(even,odd)