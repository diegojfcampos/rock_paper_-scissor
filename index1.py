import game_object as go

human_choice = "START"


while human_choice is not "EXIT":
    game = go.Game()
    game.board()
    human_choice = game.human_choice()
    if human_choice == "EXIT":
        break
    computer_choice = game.computer_choice()
    game.print_choices(human_choice, computer_choice)
    game.game_result(human_choice, computer_choice)
