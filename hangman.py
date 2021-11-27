import random
from words import words
import string

def valid_word(words):
    word=random.choice(words) #randomly choose a word
    while '-' in word or ' 'in word:
        word=random.choice(words)
    return word.upper()

def hangman():
    word=valid_word(words)
    all_letters = set(word) #letters in the word
    alphabet= set(string.ascii_uppercase)
    used_letters = set() #letters user has used
    lives=6 #total lives user has
    while len(all_letters)>0 and lives>0:
        print('You have', lives, 'lives left and you have used these letters: ',' '.join(used_letters))  #show you the list of letters you have used
    #what the current word is
        word_list =[letter if letter in used_letters else '_'for letter in word]
        print('current word: ',' '.join(word_list))
        user_letter=input('Guess a letter: ').upper() #get user input
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in all_letters:
                all_letters.remove(user_letter)
            else:
                lives = lives-1 #take one live away
                print('letter is not in the word')

        elif user_letter in used_letters:
            print('You ve guessed this letter.Please try again')
        else:
            print('Invalid character. Please try again')
        #either they guess all the letters or they died
    if lives==0:
        print('you died. The word was', word)
    else:
        print("yay you guessed the word")
# stops here when all_letters ==0
valid_word(words)
hangman()
