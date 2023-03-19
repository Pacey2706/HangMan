import random   # Imports random


def player_instructions():
    """
    opens the file 'player-instructions' when called
    """
    with open("player-instructions.txt") as p_i:
        instructions = p_i.read()
        print(instructions)


def choose_word():
    """
    Chooses a word at random from the list
    """
    words = ["hello", "scooter", "hobbits", "wizard", "elephant",
             "picnic", "apple", "yellow", "slide", "naughty", "towers"]
    return random.choice(words)


def player_guess():
    """
    returns players guess and checks validity
    """
    player_choice = input("choose a letter: ").strip().lower()
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
    for let in word:
        if let in guesses:
            hidden_word += let
        else:
            hidden_word += "*"
    return hidden_word


def hangman_art(num_guesses):
    """
    Prints hang man art that corresponds to users guesses that are left
    art used from 'https://ascii.co.uk/art/hangman'
    """
    if num_guesses == 0:
        print("""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / /
     |
    _|___""")
    elif num_guesses == 1:
        print("""
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |    
     |
    _|___""")
    elif num_guesses == 2:
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
    elif num_guesses == 4:
        print("""
      _______
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___""")
    elif num_guesses == 5:
        print("""
      
     |      
     |      
     |      
     |       
     |      
     |
    _|___""")


def main(user):
    """
    runs main mechanics for hangman game
    """
    word = choose_word()
    guesses = set()
    num_guesses = 6  # add difficulty section
    print(f"Lets begin {user}, your word has {len(word)} characters \n")
    while num_guesses > 0:
        print(f"guesses: {num_guesses}")
        print(display_word(word, guesses))
        guess = player_guess()
        if guess in guesses:
            print(f"Sorry {user} letter already guessed please try again")
        elif guess in word:
            guesses.add(guess)
            if set(word) == guesses:
                print(f"Congratulations {user}, the word was: {word}")
                return
        else:
            print("incorrect")
            num_guesses -= 1
            hangman_art(num_guesses)
    print(f"Sorry {user} better luck next time, the word was  {word}")


user = input("Please enter your name: ")
print("Welcome to HangMan would you like to play?")
answer = input("y = yes n = no: ").strip().lower()
while answer == "y" or "n":
    if answer == "y":
        print("Do you need instuctions for the game?")
        int_an = input("y = yes, anything else = no: ").strip().lower()
        if int_an == "y":
            player_instructions()
        main(user)
        break
    elif answer == "n":
        print(f"Goodbye {user}")
        quit()
    elif answer != "y" or "n":
        print("Invalid response please choose either y or n")
        sec_answer = input("y = yes n = no: ").strip().lower()
        if sec_answer == "y":
            print("Do you need instuctions for the game?")
            int_an = input("y = yes, anything else = no: ").strip().lower()
            if int_an == "y":
                player_instructions()
            main(user)
            break
        elif answer == "n":
            print(f"Goodbye {user}")
            quit()
        else:
            print(f"Sorry {user}, response invalid. Please reload the program")
            quit()
