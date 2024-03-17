# Importing necessary modules
from art import logo, vs
from game_data import data
import random

# Function to get follower count from data based on index
def get_follower(random_idx):
    return data[random_idx]['follower_count']

# Function to print name, description, and country of a person from data
def print_data(random_idx):
    d = data[random_idx]
    print(f"{d['name']}, who is {d['description']}, from {d['country']}")

# Printing the game logo
print(logo)

# Function to display options and their data
def recursive(r1, r2):
    print("\nOption A\n")
    print_data(r1)
    print(vs)
    print("\nOption B\n")
    print_data(r2)

# Generating random indices for two options
r1 = random.randint(0, len(data) - 1)
r2 = random.randint(0, len(data) - 1)
recursive(r1, r2)

# Initializing score and prompting user for input
score = 0
user_choice = input("\nEnter your choice 'a' or 'b': ").lower()

# Flag to determine game end
end_game = False
score = 0

# Game loop
while not end_game:
    # Checking user's choice and comparing follower counts
    if user_choice == "a" and get_follower(r1) > get_follower(r2):
        new_random_number = r1
        recursive(new_random_number, random.randint(0, len(data) - 1))
        score += 1
    elif user_choice == "b" and get_follower(r1) < get_follower(r2):
        new_random_number = r2
        recursive(random.randint(0, len(data) - 1), new_random_number)
        score += 1
    else:
        # If user's choice is invalid or follower count comparison fails, end the game
        end_game = True
        print("\nInvalid choice or follower count. Game Over.")
    # Displaying current score
    print(f"\nYour score is {score}")
    if not end_game:
        # If the game hasn't ended, prompt user for another choice
        user_choice = input("\nEnter your choice 'a' or 'b': ").lower()
