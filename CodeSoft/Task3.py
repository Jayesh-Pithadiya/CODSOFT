import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the character sets
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Main program
try:
    # Prompt the user to enter the desired password length
    length = int(input("Enter the desired password length: "))

    if length < 4:
        print("Password length should be at least 4 characters for complexity.")
    else:
        # Generate and display the password
        password = generate_password(length)
        print("Generated password:", password)

except ValueError:
    print("Please enter a valid number for the length.")
