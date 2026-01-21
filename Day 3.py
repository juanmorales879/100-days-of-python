import sys

print("Welcome to Treasure island")
print("YOUR MISSION IS TO  FIND THE TREASURE ")

def ask_to_play():
    return input("Play again? (y/n): ").lower()=="y"

play_again = True    

while play_again:
    first_choice = input("Type left or right: ")
    
    if (first_choice.upper() != "LEFT"):
        print("You've fallen into a hole. Game over")
        play_again = ask_to_play()
        continue
        
    second_choice = input("Swim or Wait: ")
    if (second_choice.upper() != "SWIM"):
        print("Attacked by trout. Game over")
        play_again = ask_to_play()
        continue
   
    third_choice = input("Which door: Yellow, Blue or Red? ")
    if (third_choice.upper() == "YELLOW"):
        print("You win")
        sys.exit(0)
    elif (third_choice.upper() == "BLUE"):
        print("Eaten by beasts. Game over")
        play_again = ask_to_play()
        continue
    elif (third_choice.upper() == "RED"):
        print("Burned by fire. Game over")
        play_again = ask_to_play()
        continue
    else:
        print("Game over.")
        play_again = ask_to_play()
    
    