import random
from hangman_art import stages, logo
from hangman_words import word_list


def clear_console():
    print('\n' * 150)


print(logo)
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
# print(chosen_word)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    clear_console()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print(f"You lose. The correct word was {chosen_word}.")

    if "_" not in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])