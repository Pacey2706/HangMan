"""Imports random"""
import random


def choose_word():
    """
    Chooses a word from random from the list
    """
    words = ["blah", "boop", "numpty", "pacey", "arghhh"]  # find word liabary
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
    for l in word:
        if l in guesses:
            hidden_word += l
        else:
            hidden_word += "*"
    return hidden_word


def main():
    """
    runs main mechanics for hangman game
    """
    word = choose_word()
    guesses = set()
    num_guesses = 6  # add difficulty section
    while num_guesses > 0:
        print(f"guesses: {num_guesses}")
        print(display_word(word, guesses))
        guess = player_guess()
        if guess in guesses:
            print("letter already guessed please try again")
        elif guess in word:
            guesses.add(guess)
            if set(word) == guesses:
                print(f"you win the word was: {word}")
                return
        else:
            print("incorrect")
            num_guesses -= 1
        # add ascii art thingy for each stage of code
    print(f"sorry you lose the word was  {word}")

main()



# def start_game():
#     user = input("Please enter your name: ")
#     print("Welcome to HangMan would you like to play?")
#     answer = input("y = yes n = no:")
#     while answer == "y" or "n":
#         if answer == "y":
#          main()
#         elif answer == "n":
#           print(f"Goodbye {user}")
#           quit()
#       else:
#          print("Please either choose (y or n)")

# start_game() make this a while loop at the start of the program that calls the main function afterwards


def hangman_art(num_guesses):
    """
    Prints hang man art that corresponds to users guesses that are left
    art used from 'https://ascii.co.uk/art/hangman'
    """
    if num_guesses == 6:
        print("""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / /
     |
    _|___""")
    elif num_guesses == 5:
        print("""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___""")
    elif num_guesses == 4:
        print("""
      _______
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
    _|___""")
    elif num_guesses == 3:
        print("""
      _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___""")
    elif num_guesses == 2:
        print("""
      _______
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___""")
    elif num_guesses == 1:
        print("""
      
     |      
     |      
     |      
     |       
     |      
     |
    _|___""")
