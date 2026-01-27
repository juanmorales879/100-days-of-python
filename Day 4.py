# Rock , paper or scissors 

import random,sys

ascii_art = [
"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
,
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
,
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]

ai_choice = random.randint(0,2)
user_choice = int(input("What do you choose: 0 for Rock, 1 for Paper or 2 for Scissors? "))
if user_choice < 0 or user_choice > 2:
    print("Invalid response! Out of range!")
    sys.exit(0)
    
print(f"You chose: {ascii_art[user_choice]} ")
print(f"Your opponent chose: {ascii_art[ai_choice]} ")

if user_choice == ai_choice:
    print("It's a tie!")
elif user_choice == 0 and ai_choice == 2:
    print("User wins")
elif user_choice == 1 and ai_choice == 0:
    print("User wins")
elif user_choice == 2 and ai_choice == 1:
    print("User wins")
else:
    print("Opponent wins!")
    
