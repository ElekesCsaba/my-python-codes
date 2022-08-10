import random

MIN_NUMBER = 1
MAX_NUMBER = 10


def main():
    max_tries = 3

    # print intro
    intro(max_tries)

    # get random number
    magic_number = generate_random_number()

    # play game
    player_number = game_loop(max_tries, magic_number)

    # end game
    end_game(magic_number, player_number)

    # play again
    play_again()


def intro(max_tries):
    print("=" * 50, "MAGIC NUMBER", "=" * 50)
    print(f"Find out my number between {MIN_NUMBER} and {MAX_NUMBER}.")
    print(f"You have {max_tries} tries.")


def generate_random_number() -> int:
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def get_player_number() -> int:
    guess = input("Your guess: ")

    while not check_player_number(guess):
        print(f"Your input {guess} is not a number between {MIN_NUMBER} and {MAX_NUMBER}! Try again!")
        guess = input("Your guess: ")

    return int(guess)


def check_player_number(guess: str) -> bool:
    return check_input_is_number(guess) and check_number_between_range(guess)


def check_input_is_number(guess: str) -> bool:
    return guess.isnumeric()


def check_number_between_range(guess: str) -> bool:
    return int(guess) in list(range(MIN_NUMBER, MAX_NUMBER + 1))


def compare_numbers(magic_number, player_number):
    return magic_number == player_number


def end_game(magic_number, player_number):
    if magic_number == player_number:
        print(f"You won. Magic number was: {magic_number}.")
    else:
        print(f"Game over. Magic number was: {magic_number}.")


def play_again():
    result = input("Play again? (y/n) ")
    if result == "y":
        main()
    else:
        print("Good bye.")
        exit()


def game_loop(max_tries, magic_number):
    player_number = get_player_number()

    while not compare_numbers(magic_number, player_number):
        max_tries -= 1

        if max_tries == 0:
            print("Sorry. No more tries.")
            break

        print(f"Wrong answer. Nr of trie(s) left: {max_tries}.")
        player_number = get_player_number()

    return player_number


# entry point
main()
