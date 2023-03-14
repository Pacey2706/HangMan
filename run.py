# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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


def display_word():
    """
    returns word
    """


def main():
    """
    runs main mechanics for hangman game
    """