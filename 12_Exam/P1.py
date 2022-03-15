num = 99
x = 0
while int(num/10) != 0:
    x = 0
    while num != 0:
        x += num%10
        num  = int(num/10)
    num = x   

print(x)


