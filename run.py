"""Imports random"""
import random


def choose_word():
    """
    Chooses a word from random from the list
    """
    words = ["blah", "boop", "numpty", "pacey", "arghhh"]
    return random.choice(words)


def player_guess():
    """
    returns players guess and checks validity
    """
    player_choice = input("choose a letter: ")
    if len(player_choice) > 1:
        print("Invalid guess please try again")
        return player_guess()
    else:
        return player_choice


def display_word(word, guesses):
    """
    Displays hidden words unguessed letters with "*"
    """
    hidden_word = ""
    for x in word:
        if x in guesses:
            hidden_word += x
        else:
            hidden_word += "*"
    return hidden_word


def main():
    """
    runs main mechanics for hangman game
    """
    word = choose_word()
    guesses = []
    num_guesses = 4  #add difficulty section
    print(f"guesses:{num_guesses}")
    print(display_word(word, guesses))

main()

