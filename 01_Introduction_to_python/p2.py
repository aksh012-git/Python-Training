# Write a Python program to add two positive integers without using the '+' operator

inputNumber1 = int(input('Enter a: '))
inputNumber2 = int(input('Enter b: '))

while inputNumber2 != 0:
        data = inputNumber1 & inputNumber2
        inputNumber1 = inputNumber1 ^ inputNumber2
        inputNumber2 = data << 1

print(inputNumber1)


