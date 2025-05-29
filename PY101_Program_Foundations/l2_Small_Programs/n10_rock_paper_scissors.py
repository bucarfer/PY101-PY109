

'''In this assignment, we'll build a Rock Paper Scissors game. Rock Paper Scissors is a simple game played between two opponents.
Both opponents choose an item from rock, paper, or scissors. The winner is decided according to the following rules:

If player a chooses rock and player b chooses scissors, player a wins.
If player a chooses paper and player b chooses rock, player a wins.
If player a chooses scissors and player b chooses paper, player a wins.
If both players choose the same item, neither player wins. It's a tie.
Our version of the game lets the user play against the computer. The game flow should go like this:

The user makes a choice.
The computer makes a choice.
The winner is displayed.'''

# 0.2 Import random
import random

## Bonus question 2. Shortened Input Typing the full word "rock" or "lizard" is tiring. Update the program so the user can type "r" for "rock," "p" for "paper," and so on.
# Note that if you do bonus #1, you'll have two words that start with "s." How do you resolve that?

#Bonus 2. Define the abbreviations and their correspondence full name

CHOICES = {
    'r' : 'rock',
    'p' : 'paper',
    's' : 'scissors',
    'l' : 'lizard',
    'k' : 'spock',
}

# Bonus 3. Best of Five Keep score of the player's and computer's wins. When either the player or computer reaches three wins, the match is over, and the winning player becomes the grand winner.
# Don't add your incrementing logic to display_winner. Keep your functions simple; they should perform one logical task -- no more, no less.

# Bonus 3. best of 5 count variables(first to reach 3)
your_win_counts = 0
computer_win_counts = 0

# 0.0 Create a constant

VALID_CHOICES = list(CHOICES.keys())

# 1. Creating a prompt with bespoke message

def prompt(message):
    """prints prompt"""
    print(f"=> {message}")

# 1.2 Creating conditions winner
## Bonus question 1. adding more variations
# first approach was adding them to display_winner function but it was too long

def winner_combination(your_choice, computer_choice):
    winning_moves = {
        'rock' : ['scissors', 'lizard'],
        'paper' : ['rock', 'spock'],
        'scissors' : ['paper', 'lizard'],
        'lizard' : ['spock', 'paper'],
        'spock' : ['scissors', 'rock']
    }

    #Bonus 2. Convert to full words
    your_full_choice = CHOICES[your_choice]
    computer_full_choice = CHOICES [computer_choice]

    return computer_full_choice in winning_moves[your_full_choice]
    # True if it is included and False if it not included in winning_moves

def display_winner(your_choice, computer_choice):
    #Bonus 2. Convert to full words
    your_full_choice = CHOICES[your_choice]
    computer_full_choice = CHOICES[computer_choice]
    prompt(f'you chose {your_full_choice}, the computer chose {computer_full_choice}')

    if winner_combination(your_choice, computer_choice):
        prompt('You win!')
    elif winner_combination(computer_choice, your_choice):
        # inverted variables to make computer the winner (is not a mistake)
        prompt('Computer wins!!')
    else:
        prompt("It's a tie!")

# Bonus 3.

def best_of_five(your_choice, computer_choice):
    global your_win_counts
    global computer_win_counts

    if winner_combination(your_choice, computer_choice):
        your_win_counts += 1
        prompt(f"you won {your_win_counts}")
    elif winner_combination(computer_choice, your_choice):
        # inverted variables to make computer the winner (is not a mistake)
        computer_win_counts += 1
        prompt(f"computer won {computer_win_counts}")

# Display result of best of 5 and reset result
def display_best_of_five():
    global your_win_counts
    global computer_win_counts

    if your_win_counts == 3:
        prompt('You won 3 times, You are the best of 5 winner!!')
        your_win_counts = 0 # one equal is for assignment, two for comparison
        computer_win_counts = 0
        return True # indicating someone won
    elif computer_win_counts == 3:
        prompt('Computer won 3 times, Computer is the best of 5 winner!!')
        your_win_counts = 0
        computer_win_counts = 0
        return True # indicating someone won
    return False # False if no one has won the best of 5 yet

# Salutations:
prompt("Welcome to rock/paper/scissors/lizard/spock game")

play_again = True
while play_again:
    # 2. ask user to choose

    prompt("choose one letter: 'r' (rock),'p' (paper),'s' scissors, 'l' lizard,'k' for spock") # introduce constant
    your_choice = input().lower()

    while your_choice not in VALID_CHOICES:
        prompt(f'not a valid choice, choose: {", ".join(VALID_CHOICES)}')
        your_choice = input()

    # 3. make computer choose

    computer_choice = random.choice(VALID_CHOICES)

    # 4. print output

    display_winner(your_choice, computer_choice)

    # Bonus 3. Best of Five
    best_of_five(your_choice, computer_choice)
    display_best_of_five()

    # 6. Ask user to play again
    valid_answer = False
    while not valid_answer:
        prompt("Do you want to play again? The Real Winner is the best of 5 y/n")
        answer = input().lower()

        if answer.startswith('y'):
            valid_answer = True
            play_again = True
        elif answer.startswith('n'):
            valid_answer = True
            play_again = False
        else:
            prompt("That's not a valid answer")


##Bonus questions

# 1. Notice how the display_winner function calls the prompt function. What happens if you move the display_winner function definition above the prompt function definition? Does it still work?

# No it´s stop working, we need to call the function with the variables, once the variables have been defined.

# 2. How would you use the display_winner function differently if it returned a string, as opposed to outputting the string directly?

# I would print the function -> print(display_winner(choice, computer_choice))

# 3. We used a while loop with an always-true condition and a break statement to decide whether to replay the game. Can you rewrite the loop so that we don't need to use the break statement to stop the loop?

# if answer.startwith('y') or answer.startwith('n')
# if answer[0] != 'n'

# To rewrite the loop without using a break statement, you can modify the condition of the while loop to check a variable that determines whether to continue playing. Here's how you can solve this:

## Initialize a variable to control the game loop
# play_again = True

## Use the variable in the while condition instead of True
# while play_again:
#     prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
#     choice = input()

#     while choice not in VALID_CHOICES:
#         prompt("That's not a valid choice")
#         choice = input()

#     computer_choice = random.choice(VALID_CHOICES)
#     display_winner(choice, computer_choice)

#     valid_answer = False
#     while not valid_answer:
#         prompt("Do you want to play again (y/n)?")
#         answer = input().lower()

#         if answer.startswith('n') or answer.startswith('y'):
#             valid_answer = True
#         else:
#             prompt("That's not a valid choice")

#     # Set play_again based on the user's answer
#     play_again = answer.startswith('y')

#### Bonus 1.
# Lizard Spock This game is a variation on the Rock Paper Scissors game that adds two more options - Lizard and Spock. The full explanation and rules are here. There's also a hilarious Big Bang Theory video about it here.

# The goal of this bonus is to add Lizard and Spock to your game.

# My original approach below was adding more options to the display_winner but unfortunately is too long, we need to create a dictionary instead with a

# def display_winner(player, computer):
#     prompt(f'you chose {player}, the computer chose {computer}')

#     if ((player == 'rock' and computer == 'scissors') or
#         (player == 'paper' and computer == 'rock') or
#         (player == 'scissors' and computer == 'paper') or
#         (player == 'rock' and computer == 'lizard') or
#         (player == 'lizard' and computer == 'spock') or
#         (player == 'spock' and computer == 'scissors') or
#         (player == 'scissors' and computer == 'lizard') or
#         (player == 'lizard' and computer == 'paper') or
#         (player == 'paper' and computer == 'spock') or
#         (player == 'spock' and computer == 'rock')):
#         prompt('You win!!')
#     elif ((computer == 'rock' and player == 'scissors') or
#           (computer == 'paper' and player == 'rock') or
#           (computer == 'scissors' and player == 'paper') or
#           (computer == 'rock' and player == 'lizard') or
#           (computer == 'lizard' and player == 'spock') or
#           (computer == 'spock' and player == 'scissors') or
#           (computer == 'scissors' and player == 'lizard') or
#           (computer == 'lizard' and player == 'paper') or
#           (computer == 'paper' and player == 'spock') or
#           (computer == 'spock' and player == 'rock')):
#         prompt('Computer wins!!')
#     else:
#         prompt("It's a tie!")
