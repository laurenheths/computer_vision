import random

game_options = ["rock", "paper", "scissors"]

def game():

    def get_computer_choice(game_options):
        computer_option = random.choice(game_options)
        return computer_option
    
    def get_user_choice():
        user_option = input("choose rock, paper or scissors: ")
        return user_option
    
    def get_winner(computer_option, user_option):
        if computer_option == 'rock' and user_option == 'scissors' or computer_option == "scissors" and user_option == 'paper' or computer_option == 'paper' and user_option == 'rock': 
            print('You Lose')
        elif user_option == 'rock' and computer_option == 'scissors' or user_option == "scissors" and computer_option == 'paper' or user_option == 'paper' and computer_option == 'rock': 
            print('You win')
        elif user_option == computer_option: 
            print('it is a tie')
        elif user_option not in game_options or computer_option not in game_options:
            print('invalid input')
            
    user_option = get_user_choice()
    computer_option = get_computer_choice(game_options)
    print(f"The computer chose : {computer_option}")
    get_winner(computer_option, user_option)


game()