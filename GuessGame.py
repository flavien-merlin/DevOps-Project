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


def play_guess(difficulty):
    def welcome():
        print(f"Welcome to the Guess Game you will have to guess a number between 1 to {difficulty}")
        time.sleep(1)
        print(f"Get ready it's going to start: ")
        dots()

    difficulty = difficulty + 1
    welcome()

    def generate_number():  # generate a number between 1 to difficulty and save it to a secret number
        random_number = random.randint(1, difficulty)
        secret_number = random_number
        return secret_number

    def get_guess_from_user():  # get input from user between 1 to difficulty
        while True:
            user_input = input(f"\nGuess a number between 1 to {difficulty}: ")
            if not user_input.isdigit() or int(user_input) not in range(difficulty + 1):
                print("Please chose a valid number: ")
            else:
                break
        input_from_user = user_input
        lines()
        return input_from_user

    def compare_result():  # compare the result
        generated_number = generate_number()
        user_number = get_guess_from_user()

        if int(generated_number) == int(user_number):
            return True
        else:
            return False

    if compare_result():
        print("Congratulation, you won")
        add_score(difficulty)
    else:
        print("What a bummer, you lose")
