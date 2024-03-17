from art import logo, vs
from game_data import data
import random
import os

def get_follower(random_idx):
    return data[random_idx]['follower_count']

def print_data(random_idx):
    d = data[random_idx]
    print(f"{d['name']}, who is {d['description']}, from {d['country']}")
print(logo)
def recursive(r1, r2):
    print("\nOption A\n")
    print_data(r1)
    print(vs)
    print("\nOption B\n")
    print_data(r2)

r1 = random.randint(0, len(data) - 1)
r2 = random.randint(0, len(data) - 1)
recursive(r1, r2)
score = 0
user_choice = input("\nEnter your choice 'a' or 'b': ").lower()
end_game = False
score = 0

while not end_game:
    if user_choice == "a" and get_follower(r1) > get_follower(r2):
        new_random_number = r1
        os.system('clear')
        recursive(new_random_number, random.randint(0, len(data) - 1))
        score += 1
        
    elif user_choice == "b" and get_follower(r1) < get_follower(r2):
        new_random_number = r2
        recursive(random.randint(0, len(data) - 1), new_random_number)
        score += 1
        os.system('clear')
    else:
        end_game = True
        print("\nInvalid choice or follower count. Game Over.")
    print(f"\nYour score is {score}")
    if not end_game:
        user_choice = input("\nEnter your choice 'a' or 'b': ").lower()



