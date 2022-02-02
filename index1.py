import game_object as go


human_choice = ""
game_object = go.Game()

test1 = input("\n==========================\n Make your choice (1 to 4):  ")
print(test1)

while human_choice is not "EXIT":
    game_object.board()

    human_choice = game_object.human_choice()
   
    computer_choice = game_object.computer_choice()

    game_object.print_choices(human_choice, computer_choice)
    game_object.game_result(human_choice, computer_choice)
