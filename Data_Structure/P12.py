# Create a simulation program for Hot Potato Game.
# You can develop with your ideas. Just take care of the following things:
# - At least one person must remove from each round.
# - Display name in the console that which user has a hot potato.
# - Each user holds a potato for random seconds between 0.1 to 3.0
# - Each round starts after 3 seconds of the previous elimination.
# - Each round stops at random seconds between 5 to 20.
# - Display the name of the winner.

# Python code to demonstrate
# working of sleep()

import time
import random

player_list = ['HIREN SIR','HIRAL MA\'AM','NEEL SIR','RUTVIK SIR','PARAM SIR','SHUVAM SIR','DHRUVIN SIR']
removed_player = ''
for round1 in range(len(player_list)-1):
        total_of_player_seconds = 0
        round_second = random.randint(5,7)
        count = 0
        print('\n')
        print('Now,start round no.',round1+1)
        print('------------------------------------')

        while total_of_player_seconds <= round_second:
            each_player_seconds = round(random.uniform(0.1,0.4),1)
            total_of_player_seconds += each_player_seconds
            removed_player = player_list[count]
            print('Now,{0} have hot potato'.format(removed_player))
            count+=1
            if count == len(player_list):
                count = 0   
            time.sleep(each_player_seconds)

        player_list.remove(removed_player)
        print('------------------------------------')
        print('{0} is out of the game 😪'.format(removed_player))
        print('Available_player :', player_list)
        time.sleep(3)

print('\n')
print('-------------------------------------')
print('||  {0} is winner 🥳  ||'.format(player_list[0]))
print('-------------------------------------','\n')


#--------------------------------------------------------------------------------------------------------------

# count = 0
# removed_player = ''

# # for round in range(len(player_list)):
# total_of_player_seconds = 0
# round_second = random.randint(5,20)

# while total_of_player_seconds <= round_second:
#     each_player_seconds = round(random.uniform(0.1,3.0),1)
#     total_of_player_seconds += each_player_seconds
#     removed_player = player_list[count]
#     print(removed_player,total_of_player_seconds,round_second)
#     count+=1
#     if count == len(player_list):
#         count = 0   
#     time.sleep(each_player_seconds)

# player_list.remove(removed_player)
# print('Available_player :', player_list)
# print('-------------------------------------------')

# count = 0
# removed_player = ''

# # for round in range(len(player_list)):
# total_of_player_seconds = 0
# round_second = random.randint(5,20)

# while total_of_player_seconds <= round_second:
#     each_player_seconds = round(random.uniform(0.1,3.0),1)
#     total_of_player_seconds += each_player_seconds
#     removed_player = player_list[count]
#     print(removed_player,total_of_player_seconds,round_second)
#     count+=1
#     if count == len(player_list):
#         count = 0   
#     time.sleep(each_player_seconds)

# player_list.remove(removed_player)
# print('Available_player :', player_list)
# print('-------------------------------------------')

        
    
    
        
        
    
    


