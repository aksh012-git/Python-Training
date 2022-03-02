#  Create class Cards with two list suits (Hearts, Diamonds, Clubs, Spades) and  values (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)
# -> Create a class deck. That contains a method to get a card set containing 52 elements.
# -> Create class shuffle. That contains two methods to shuffle given cards and remove/pick a single card.
# -> Create two objects of the above class as players. Each player pick/remove 5 cards from the shuffle cards. Total points of both players and display name of winner player.


import math,random


class Cards():
    def __init__(self,cards_type,cards_value):
         self.cards_type =cards_type
         self.cards_value = cards_value
        
class deck(Cards):
    def all_cards(self):
        list_of_all_cards = []
        for i in self.cards_value:
            for j in self.cards_type:
                list_of_all_cards.append([j,i])
        return list_of_all_cards

class Shuffle():
    count = 0
    def __init__(self,list_of_all_cards):
        self.list_of_all_cards = list_of_all_cards
        
    def shuffle_cards(self):
        for i in range(len(self.list_of_all_cards)-1,-1,-1):
            random_index = random.randint(0,i)
            x = self.list_of_all_cards[random_index]
            self.list_of_all_cards.remove(x)
            self.list_of_all_cards.append(x)
            
    def pick_card(self,number_of_card):
        previous_cards = Shuffle.count
        Shuffle.count = Shuffle.count + (number_of_card)
        return self.list_of_all_cards[previous_cards:Shuffle.count]
        
        
    
    
cards_type = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
cards_value = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
obj = Cards(cards_type,cards_value)
list_of_all_cards = deck.all_cards(obj)
# print(len(list_of_all_cards),list_of_all_cards,'\n\n')

mainObj = Shuffle(list_of_all_cards)

mainObj.shuffle_cards()

player_1 = mainObj.pick_card(5)
player_2 = mainObj.pick_card(5)

print(player_1)
print(player_2)

player_1_total_point = 0
player_2_total_point = 0
for i in range(len(player_1)):
    player_1_total_point += cards_type.index(player_1[i][0]) + cards_value.index(player_1[i][1])
    player_2_total_point += cards_type.index(player_2[i][0]) + cards_value.index(player_2[i][1])
    

if player_1_total_point > player_2_total_point:
    print('player-1 is win!!!\n','Point of player-1 {0}\n'.format(player_1_total_point),'Point of player-2 {0}\n'.format(player_2_total_point))
else:
    print('player-2 is win!!!\n','Point of player-1 {0}\n'.format(player_1_total_point),'Point of player-2 {0}\n'.format(player_2_total_point))
    