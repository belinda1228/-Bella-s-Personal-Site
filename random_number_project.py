import random

#def guess(x):
#    random_number= random.randint(1,x)
#    guess = 0
#    while guess != random_number:
#        guess = int(input(f"guess a number between 1 and {x}: "))
#        if guess < random_number:
#            print("your guess is too low")
#        elif guess > random_number:
#            print("your guess is too high")
#    print('you got it right!')
#    print(guess)

def computer_guess(x):
    low=1
    high=x
    feedback=' '
    while feedback != 'c':
        if low!=high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback=input(f"is {guess} too high(h) or too low(l) or correct/c? ").lower()
        if feedback== "h":
                high=guess-1
        elif feedback== "l":
                low=guess+1

    print('computer guessed right')

computer_guess(100)

#guess(5)
    