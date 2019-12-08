Team Members: 

Ryan Hsiao
B#: B

Shirley Wong
B#: B00662672

How to run the program:
Click run. Play.

What is it?
The program is the hangman game.

What does it do?
When the player clicks play, a random word from a selection of words will be chosen.
The goal of the game is for players to guess that word before the man is hung.
If the player gueses it before the full man is pictured, the player wins.
If not, the player loses.

How does it work?
First a word is randomly selected by the program from the WORDS tuple.
Two functions were created: one to play the game and one to update the dashes that hold the word.

The Play() function begins by printing the names of the coders as well as introducing the game.
The variable "dashes" makes the dashes that hold the hidden word.
"Guesses" is the amount of times users can guess before the full man is drawn on the terminal.
"Wrong" contains the index the display the hanged man.
The while loop makes sure that while the player still has gueses left, that the game continues.
The loop starts by printing dashes and then taking user input and converting it to lowercase 
to make the program not case sensitive.
If the user guesses something wrong, the wrong variable will update by 1 and print the next body part.
The first set of if statements take into consideration possible player errors such as the input of
two letters instead of one and wrong guesses. It also lets player know if they did guess a letter correctly.
The final if statements are to make sure that once the game hits zero guesses, the player knows whether
he or she won or not.

The update_dashes() function serves to update the dashes dispalyed with any correct gueseses made by the player.
The loop searches for the player's guess in the word and returns the guess to replace the dash.
If player's guess is incorrect, it returns the dashes.

References: