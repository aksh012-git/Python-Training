# Finding the sum of all digits of a number until the sum becomes a single digit.
# Examples. 10589=>5 , 121=>4, 99=>9, 10=>1

input_number = 1234567
sum_of_model_of_input = 0

while int(input_number/10) != 0:
    sum_of_model_of_input = 0
    while input_number != 0:
        sum_of_model_of_input += input_number%10
        input_number  = int(input_number/10)
    input_number = sum_of_model_of_input   

print(sum_of_model_of_input)

#----------------------------------------------------------------

if input_number % 9 == 0:
    print(9)
else:
    print(input_number%9)
    

    