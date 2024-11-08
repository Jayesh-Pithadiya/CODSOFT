import random

# Choices for the game
choices = ["rock", "paper", "scissors"]

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Main program
user_score = 0
computer_score = 0

print("Welcome to Rock-Paper-Scissors Game!")
print("Instructions: Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to end the game.\n")

while True:
    # Prompt the user for input
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    # Option to quit the game
    if user_choice == "quit":
        print("\nThanks for playing!")
        break

    # Validate user choice
    if user_choice not in choices:
        print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
        continue

    # Generate a random choice for the computer
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    result = determine_winner(user_choice, computer_choice)

    if result == "user":
        print("You win this round!")
        user_score += 1
    elif result == "computer":
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("It's a tie!")

    # Display the current score
    print(f"Score - You: {user_score} | Computer: {computer_score}\n")

    # Ask if the user wants to play another round
    play_again = input("Do you want to play another round? (yes/no): ").lower()
    if play_again != "yes":
        print("\nThanks for playing!")
        break

# Final score display
print(f"\nFinal Score - You: {user_score} | Computer: {computer_score}")
if user_score > computer_score:
    print("Congratulations! You won the game!")
elif computer_score > user_score:
    print("Computer wins the game. Better luck next time!")
else:
    print("It's a tie game!")
