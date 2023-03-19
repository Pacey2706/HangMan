# HangMan
Hang man is a terminal based game that allows the user to guess a randomly gegenerated word.
## How To Play
To play the user is firsted asked to input their name followed by a question if they would like to see the instructions for the game.
Once the game has begun the user is presented with a choose a letter input area.
The user is then required to guess the letters to the word one at a time until either they have run out of guesses or correctly guessed the word
## Features
### existing features 
* at the beginging of the game the user is asked to for their name. 
their name is then used through out the game for a more personal experince.
* after each failed guess a image is displayed in the terminal showing the user each stage of the hangman process.

### future features 
In the future I would like this game to incorporate a highscore chart linked to a database that would update after each game.
I would also like to add a difficulty setting where the player can choose how hard they would like the game to be 
## technology 
Python
## bugs and errors 
While deveolping the game I encountered a bug for the users letter choice. if the user added spaces or more than one letter the program would crash. to fix this I added .strip() and .lower()
## testing
the program has been ran through the pep8ci checker 
15 x W291 errors relating to the hangman visuals
3 x W605 errors relating to the hangman visuals 
## credits 
youtube- Kite
How to build HANGMAN with Python in 10 MINUTES
ascii art- 
https://ascii.co.uk/art/hangman