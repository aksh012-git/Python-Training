total_cards = 52
total_ace_in_one_deck = 4
total_tries = 0
decreased_ace_probability = []
average_rate_of_decrease = 0

while True:
    total_tries  = total_tries + 1     
             
    if not total_ace_in_one_deck: 
        print(f'In the "{total_tries}th" try probability goes to 0')
        print('Average rate of decrease: ',average_rate_of_decrease/3)
        break
    
    if total_ace_in_one_deck < 4:
        average_rate_of_decrease = ((total_ace_in_one_deck+1)/(total_cards+1))*100 - (total_ace_in_one_deck/total_cards)*100 + average_rate_of_decrease
        
    total_cards = total_cards - 1
    total_ace_in_one_deck = total_ace_in_one_deck - 1
    
