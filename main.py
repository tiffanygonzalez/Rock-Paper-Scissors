import random


def choose_rps():
    """
    Output: randomly returns rock, paper, or scissors
    """
    return random.choice(['rock', 'paper', 'scissors'])


def play_round(user_choice, computer_choice):
    """
    Input: user and computer's choices
    Output: the outcome of the round as a string
    """
    # Tie
    if user_choice == computer_choice:
        return "It's a tie!"

    # User wins
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return "You won!"
    
    # Computer wins
    return "The computer won!"


play = True

# Play the game
while play:
    # Get user choice
    while True:
        user_choice = input('Please enter your choice (rock, paper, or scissors): ').lower()
        print(f'You chose {user_choice}')

        if user_choice in ['rock', 'paper', 'scissors']:
            break
        else:
            print('Invalid choice. Please try again.\n')

    # Randomly assign computer choice
    computer_choice = choose_rps()
    print(f'The computer chose {computer_choice}')

    # Print outcome
    outcome = play_round(user_choice, computer_choice)
    print(outcome)
    print('\n---')

    # Play again or end game
    while True:
        play_again = input('\nWould you like to play again? (y/n): ').lower()
        if play_again == 'n':
            play = False
            print('\n')
            break
        if play_again == 'y':
            play = True
            print('\n')
            break
        else:
            print('Invalid choice. Please try again.\n')

# End game message
print('Thank you for playing!')