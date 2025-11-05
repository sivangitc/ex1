import random
from typing import Tuple

SIZE_BOARD = 10


def is_close(real: Tuple[int, int], guess: Tuple[int, int]) -> bool:
    return abs(real[0] - guess[0]) <= 1 and abs(real[1] - guess[1]) <= 1


def is_interesting(real: Tuple[int, int], guess: Tuple[int, int]) -> bool:
    return real[0] == guess[0] or real[1] == guess[1]


def main() -> None:
    num_guesses = 0
    real = (random.randint(1, SIZE_BOARD), random.randint(1, SIZE_BOARD))
    guess = (0, 0)
    while real != guess:
        num_guesses += 1
        row_guess = int(input("Enter row: "))
        col_guess = int(input("Enter col: "))
        guess = (row_guess, col_guess)
        if real == guess:
            break
        if is_close(real, guess):
            print("CLOSE!")
            continue
        if is_interesting(real, guess):
            print("INTERESTING...")
            continue
        print("keep thinking :(")

    print(f"!HIT! you got it in {num_guesses} guesses well done!")


if __name__ == "__main__":
    main()
