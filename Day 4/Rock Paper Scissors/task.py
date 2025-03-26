rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

you = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))

comp = random.randint(0,2)

def choice_print(n):
    if n == 0:
        print(rock)
    elif n == 1:
        print(paper)
    elif n == 2:
        print(scissors)

choice_print(comp)
print('Computer chose:')
choice_print(you)

if you == comp:
    print("It's a draw")
elif (you == 2 and comp == 1) or (you == 1 and comp == 0) or (you == 0 and comp == 2):
    print("You win")
elif (you == 1 and comp == 2) or (you == 0 and comp == 1) or (you == 2 and comp == 0):
    print("You Lose")