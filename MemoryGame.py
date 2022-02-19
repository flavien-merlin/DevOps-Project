from Score import add_score
import random
import time
import sys


def lines():  # Separation lines
    print("-" * 55)


def dots():  # Print waiting dots
    for i in range(1, 6):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.3)


def play_memory(difficulty):
    def welcome():
        print(f"Welcome to the Memory Game: You will have to remember {difficulty} number.")
        time.sleep(1)
        print(f"Get ready it's going to start: ")
        dots()

    welcome()

    def generate_sequence():  # Generate a random number 1 to 101 with length of difficulty
        random_list = [random.randint(1, 101) for i in range(difficulty)]
        saved_list = random_list
        print(saved_list)
        time.sleep(0.7)
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        return saved_list

    def get_list_from_user():  # Prompt the user for a list of number
        while True:
            user_list = input(f"Enter {difficulty} number separated by space: ").split()
            try:
                user_list = [int(i) for i in user_list]
            except ValueError:
                print("Invalid value, try again")
                continue
            if not len(user_list) == difficulty:
                print(f"Please chose {difficulty} number separated by space: ")
            else:
                break
        lines()
        saved_user_list = user_list
        return saved_user_list

    def is_list_equal():  # will compare both of the list above and return True/False
        computer_list = generate_sequence()
        user_list = get_list_from_user()
        computer_list.sort()
        user_list.sort()
        if sorted(user_list) == sorted(computer_list):
            return True
        else:
            return False

    if is_list_equal():
        print("You won, good memory")
        add_score(difficulty)
    else:
        print("You lose, what a bummer: Try again!")
