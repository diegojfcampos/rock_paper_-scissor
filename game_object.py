import random

class Game():
    def __init__(self):
        pass

    def board(self):
        print("\n============\nGAME CHOICE\n============\n");
        print("1 - Rock");
        print("2 - Paper");
        print("3 - Scissor");
        print("4 - Exit");

    def human_choice(self):
        human_choice = int(input("\n==========================\n Make your choice (1 to 4):  ")) 
        if human_choice == 1:
            return "ROCK"
        if human_choice == 2:
            return "PAPER"
        if human_choice == 3:
            return "SCISSOR"
        if human_choice == 4:
            return "EXIT"

    def computer_choice(self):
        option = ["ROCK", "PAPER", "SCISSOR"]
        computer_choice = random.choice(option)  
        print(computer_choice)
        return computer_choice


    def print_choices(self, human_choice, computer_choice):
        print(f"\nYou: {human_choice}")
        print(f"Computer: {computer_choice}\n")


    def game_result(self, human_choice, computer_choice):
        if human_choice == "ROCK":      
            if computer_choice == "PAPER":
                print("COMPUTER WIN")
            elif computer_choice == "SCISSOR":
                print("YOU WIN")
            else:
                print("DRAWN")

        if human_choice == "PAPER":      
            if computer_choice == "SCISSOR":
                print("COMPUTER WIN")
            elif computer_choice == "ROCK":
                print("YOU WIN")
            else:
                print("DRAWN")

        if human_choice == "SCISSOR":      
            if computer_choice == "ROCK":
                print("COMPUTER WIN")
            elif computer_choice == "PAPER":
                print("YOU WIN")
            else:
                print("DRAWN")

    