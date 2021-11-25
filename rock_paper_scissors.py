import random

# def computer_choice():
#     user=input('rock(r), paper(p), scissors(s), shoot: ').lower()
#     computer=random.choice(['r','p','s'])
#     if user==r and computer==p:
#         print("you lost!")
#     elif user=='r' and computer=='s':
#         print("you won!")
#     elif user=='p' and computer=='s':
#         print("you lost!")
#     elif user=='p' and computer=='r':
#         print("you won!")
#     elif user=='s' and computer=='r':
#         print("you lost!")
#     elif user=='s'and computer=='p':
#         print("you won!")
#     else:
#         print("it's a tie")

def computer_choice():
    user=input('rock(r), paper(p), scissors(s), shoot:').lower()
    computer=random.choice(['r','p','s'])
    if user==computer:
        print("it\'s a tie")
    if user_win(user, computer):
        print('you won!')
  
    return 'you lost!'

def user_win(user, computer):
    if (user=='r' and computer=='s')or(user=='p' and computer=='r')or(user=='p' and computer=='r'):
        return True

computer_choice()
