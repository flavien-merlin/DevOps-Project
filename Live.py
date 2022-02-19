import sys
import time
from GuessGame import play_guess
from MemoryGame import play_memory


def dots():  # Print waiting dots
    for i in range(1, 6):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.3)


def lines():  # Separation lines
    print("-" * 55)


def check_choice(a):  # check number in range
    while True:
        i = int(a) - 1
        if i not in range(2):
            a = input("invalid number try again: ")
            continue
        break
    return a


def check_difficulty(b):  # check number in range
    while True:
        i = int(b) - 1
        if i not in range(5):
            b = input("invalid number try again: ")
            continue
        break
    return b


def welcome():
    while True:
        name = str(input("Welcome, please enter your name: "))
        lines()
        if name.isdigit():
            print("Please enter a valid name.")
        else:
            break
    print(f"Hello {name}! Welcome to the World of Games (WoG).\nHere you can find many cool games to play.")
    dots()


def load_game():
    print(f"\nPlease choose a game to play: \n"
          f"1.Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
          f"2.Guess Game  - guess a number and see if you chose like the computer")
    lines()

    while True:
        choice = input("Chose which game you want to play between 1 and 2: ")
        if not choice.isdigit():
            print("Please enter a valid number: ")
        else:
            break

    user_choice = ["the Memory Game, get ready.", "the Guess Game, get ready.",
                   "Currency Roulette - try and guess the value of a random amount of USD in ILS, get ready."]

    choice = check_choice(choice)
    print("You chose to play ", user_choice[int(choice) - int(1)])
    lines()

    while True:
        difficulty = input("Please choose also the game difficulty from 1 to 5: ")
        if not difficulty.isdigit():
            print("Please enter a valid number: ")
        else:
            break

    level_of_difficulty = [
        "very easy, ok you are scared to loose but let's play.",
        "easy, ok let's play.", "normal, ok let's play.", "hard, now we are talking let's play.",
        "very hard, ok we got a challenger let's play"]

    difficulty = check_difficulty(difficulty)
    print("Level of difficulty is ", level_of_difficulty[int(difficulty) - int(1)])
    lines()

    def play_guess_game():
        play_guess(int(difficulty))

    def play_memory_game():
        play_memory(int(difficulty))

    if choice == "1":
        play_memory_game()
    elif choice == "2":
        play_guess_game()
