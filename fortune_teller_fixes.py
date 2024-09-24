import random

# This program follows the best coding principles: KISS, DRY, and Single Responsibility.

# Function to get the user's name
def get_user_name():
    return input("What is your name? ")

# Function to select a random fortune
def get_fortune():
    fortunes = [
        "You will discover something new today.",
        "Focus inward and you will see outward changes.",
        "You will overcome challenges holding you back.",
        "A mistake you make will turn out for the better.",
        "Your search will yield the results you desire."
    ]
    return random.choice(fortunes)

# Function to display the fortune
def display_fortune(user_name, fortune):
    print(f"{user_name}, your fortune is: {fortune}")

# Main function that handles the flow of the program
def main():
    user_name = get_user_name()
    fortune = get_fortune()
    display_fortune(user_name, fortune)

if __name__ == "__main__":
    main()
