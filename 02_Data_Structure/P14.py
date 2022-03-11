# Add 1 to given list elements. Do not use string conversion.
# 	Sample = [1, 2, 3]
#         Output = [1, 2, 4]

num_list = [8,9,9,9]
lenth = len(num_list) -1
mult = 10**(lenth)
pure_value = 0

for item in num_list:
    pure_value += (item * mult)
    lenth -= 1
    mult = 10**(lenth)    
    
pure_value = pure_value+1
final_list = []

while pure_value > 0:
    final_list.insert(0,pure_value%10)
    pure_value = int(pure_value / 10)

print(final_list)