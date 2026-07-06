# ROCK, PAPAER AND SCISSOR GAME!

print("==== ROCK, PAPER AND SCISSOR =====")

import random as r

a = input("Want to play? (Y/N) : ")

if a.lower() == "y":

    moves = ["Rock" , "Paper" , "Scissor"]

    choice = int(input("""
    Select Your Choice
    1. Rock
    2. Paper
    3. Scissor
                        
    Enter Your Choice : """))
    
    if 1 <= choice <= 3:

        user = moves[choice-1]
        computer = r.choice(moves)

        print("----------------------")
        print(f"You       : {user}")
        print(f"Computer  : {computer}")
        print("------------------------")

        if user == computer:
            print("🤝 Match Draw!")
        elif user == "Rock" and computer == "Scissor":
            print("🎉 You Win!")
        elif user == "Paper" and computer == "Rock":
            print("🎉 You Win!")
        elif user == "Scissor" and computer == "Paper":
            print("🎉 You Win!")
        else:
            print("💻 Computer Win!")
    
    else:
        print("Invalid Choice")

else:
    print("Game Aborted!")




