number = int(23)
flag = False
    
if number == 1:
    print('Unique value')
else:
    for i in range(2,int((number/2)+1)):
        if number % i == 0:
            flag = True
            break
        else:
            flag = False

    if flag:
        print(f'{number} is not prime')
    else:
        print(f'{number} is prime')
    
    