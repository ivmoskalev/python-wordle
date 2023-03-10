import random
import os
from pathlib import Path

WORDLIST = Path("wordle/words.txt")
WORDLEN = 5

def get_random_word(wordlist: os.PathLike, word_len: int) -> str:
    words = [
        word.upper()
        for word in wordlist.read_text(encoding="utf-8").strip().split("\n")
        if len(word) == word_len
            ]
    return random.choice(words)

def show_guess(guess: str, word: str) -> None:

    correct_letters = {
        letter for letter, correct in zip(guess, word) if letter == correct
    }
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print("Correct letters:", ", ".join(sorted(correct_letters)))
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))

def game_over(word: str) -> None:
    print(f"The word was {word}")

def main() -> None:

    word = get_random_word(WORDLIST, WORDLEN)

    for guess_num in range(1, 7):
        print(word) #Debug cheat. Remove in production
        guess = input(f"\nGuess {guess_num}: ").upper()

        if guess == word:
            print("Correct")
            break

        show_guess(guess, word)

    else:
        game_over(word)

if __name__ == "__main__":
    main()