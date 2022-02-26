from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


def set_difficulty():

    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    while level != "easy" and level != "hard":
        print(f"You have chosen an incorrect difficulty: '{level}'. Please try again.")
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS


def game():
    print(logo)

    # Generate a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    # print(f"THE RANDOM NUMBER: {answer}")

    turns_left = set_difficulty()

    # Make player guess the number while they have turns left and not guessed right, and
    # end the game if the guess is correct or turns left is 0
    guess = 0
    while guess != answer:
        print(f"You have {turns_left} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        # After each guess, check if it's correct, after wrong guess reduce turns left
        turns_left = check_answer(guess, answer, turns_left)
        if turns_left == 0:
            print("You've run out of guesses, you lose.")
            print(f"The correct number would have been: {answer}")
            return
        elif guess != answer:
            print("Guess again.")


game()
