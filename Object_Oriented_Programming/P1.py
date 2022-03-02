# Take the word and its meaning as input from the user.
# -> Create a class named flashcard, use the __init__() function to assign values for Word and Meaning.
# -> Now use the __str__() function to return a string that contains the word and meaning.
# -> Store the returned strings in a list named flash.
# -> Use a while loop to print all the stored flashcards.
# -> Add proper error handling
# 		-> Result image is attached in thread


class Flashcard():
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
        
    def __str__(self):
        return self.word + " " + self.meaning

    
print('Welcome To Flashcard Application')
flash = []
while True:
    try:
        add_oparation = int(input('\nEnter : 0, If you want to add flashcard \nEnter : 1, If you want to show existing flashcards \nEnter : 2, If you want to quit our application \n:'))
        if not add_oparation:
            word_input = input('Enter word:')
            meaning_input = input('Enter meaning of entered word:')
            word_list = str(Flashcard(word_input,meaning_input)).split(" ")
            flash.append(word_list)
        elif add_oparation == 1:
            i = 0
            if len(flash) != 0:
                while i < len(flash):
                    print(flash[i][0],'( {0} )'.format(flash[i][1]))
                    i+=1
            else:
                print('currently is no flashcards exist!!')
        elif add_oparation == 2:
            break
        else:
            print('Please Enter only 0,1 or 2')
    except Exception as e:
        print(type(e).__name__,':',e)
        print('Please Enter only 0,1 or 2')
    
    