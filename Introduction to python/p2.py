# Write a Python program to add two positive integers without using the '+' operator

a = int(input('Enter a: '))
b = int(input('Enter b: '))

while b != 0:
        data = a & b
        a = a ^ b
        b = data << 1

print(a)


