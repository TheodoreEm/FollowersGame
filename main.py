# import logos
from art import logo, vs
import random
from game_data import data
from os import system, name


# function for clearing the terminal
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


correct_answer = True
score = 0
# Beginning logo
print(logo)
while correct_answer:
    if score != 0:
        print(f"You are right! current score: {score}")
    # Generating 2 random number with range of 0 to 49 because the length of the list is 50
    number_1 = random.randint(0, 49)
    number_2 = random.randint(0, 49)

    print("Compare A:", data[number_1]["name"], ", ", data[number_1]["description"], ", ", data[number_1]["country"])

    print(vs)
    print("Compare B:", data[number_2]["name"], ", ", data[number_2]["description"], ", ", data[number_2]["country"])

    # input the choice for the user to answer if he picks A or B
    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    # While loop making sure that the answer is a or b
    while user_answer != "a" and user_answer != "b":
        clear()
        user_answer = input("Wrong input, Who has more followers? Type 'A' or 'B': ").lower()

    # If the user picks A
    if user_answer == "a":
        if data[number_1]["follower_count"] > data[number_2]["follower_count"]:
            score += 1
            clear()
        else:
            correct_answer = False
            print(f"You are wrong! Your final score is {score}")

    # If the user picks B
    else:
        if data[number_1]["follower_count"] < data[number_2]["follower_count"]:
            score += 1
            clear()
        else:
            correct_answer = False
            print(f"You are wrong! Your final score is {score}")

