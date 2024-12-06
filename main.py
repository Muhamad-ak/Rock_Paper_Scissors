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

game_gallery = [rock, paper, scissors]
player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_input = random.randint(0, 2)

if player_input >=0 and player_input <=2:
    print(game_gallery[player_input])

print("Computer chose:")
print(game_gallery[computer_input])

if player_input >=3 and player_input<0:
    print("You typed an invalid number. You lose!")
elif player_input == 0 and computer_input ==2:
    print("You win!")
elif computer_input == 0 and player_input ==2:
    print("You lose!")
elif computer_input > player_input:
    print("You lose!")
elif player_input > computer_input:
    print("You win!")
elif computer_input == player_input:
    print("It's a drwa!")


