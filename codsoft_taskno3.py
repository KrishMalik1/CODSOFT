import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'tie'
    if (player_choice == 'rock' and computer_choice == 'scissors') or \
       (player_choice == 'scissors' and computer_choice == 'paper') or \
       (player_choice == 'paper' and computer_choice == 'rock'):
        return 'player'
    return 'computer'

def display_result(user_choice, computer_choice, winner):
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'player':
        print("You win!")
    else:
        print("You lose!")

def play_game():
    player_score = 0
    computer_score = 0
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, please try again.")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        display_result(user_choice, computer_choice, winner)
        
        if winner == 'player':
            player_score += 1
        elif winner == 'computer':
            computer_score += 1
        
        print(f"Score - You: {player_score}, Computer: {computer_score}")
        
        if input("Play again? (yes/no): ").lower() == 'no':
            break
    
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
