import random
from art import logo


def clear_console():
    print("\n" * 50)


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "   >>> DRAW <<<"
    elif computer_score == 0:
        return "   >>> YOU LOSE, COMPUTER HAS BLACKJACK <<<"
    elif user_score == 0:
        return "   >>> YOU WIN, YOU HAVE BLACKJACK <<<"
    elif user_score > 21:
        return "   >>> YOU LOSE, YOU WENT OVER 21 <<<"
    elif computer_score > 21:
        return "   >>> YOU WIN, COMPUTER WENT OVER 21 <<<"
    elif user_score > computer_score:
        return "   >>> YOU WIN <<<"
    else:
        return "   >>> YOU LOSE <<<"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: [{computer_cards[0]}]")

        if user_score == 0 or computer_score == 0 or user_score > 21 or user_score == 21:
            is_game_over = True
        else:
            user_should_deal = input("\nType 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\n   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}\n")
    print(compare(user_score, computer_score))


while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear_console()
    play_game()
