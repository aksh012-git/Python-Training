#Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

def chekNumberIsSameOrNot(sequenceOfNumber):
    if len(sequenceOfNumber) != len(set(sequenceOfNumber)):
        return False
    else:
        return True
    
sequenceOfNumber = list(map(int,input().split(" ")))
print(chekNumberIsSameOrNot(sequenceOfNumber))
        