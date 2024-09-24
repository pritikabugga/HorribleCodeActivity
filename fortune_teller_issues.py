import random

# This program violates best coding practices: KISS, DRY, and Single Responsibility.

def fortune_teller():
    # Getting user's name and showing fortune all in one function
    name = input("What is your name? ")

    # Repeatedly displaying fortunes within the same function
    fortunes = [
        "You will discover something new today.",
        "Focus inward and you will see outward changes.",
        "You will overcome challenges holding you back.",
        "A mistake you make will turn out for the better.",
        "Your search will yield the results you desire."
    ]

    # Randomly selecting a fortune
    fortune = random.choice(fortunes)

    # Mixing input/output logic with fortune selection
    if name:
        print(f"{name}, your fortune is: {fortune}")
    else:
        print("Your fortune is: ", fortune)

if __name__ == "__main__":
    fortune_teller()
