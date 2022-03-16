# Write a Python program to filter(even and odd) a list of integers using Lambda.
#  Original list of integers:
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  Even numbers from the said list:
#  [2, 4, 6, 8, 10]
#  Odd numbers from the said list:
#  [1, 3, 5, 7, 9]

inputList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
outputOfEvenList = []
outputOfOddList = []

for listItem in inputList:
    moduloValue = lambda number : number % 2
    if moduloValue(listItem):
        outputOfOddList.append(listItem)
    else:
        outputOfEvenList.append(listItem)
        
print(outputOfEvenList,outputOfOddList)