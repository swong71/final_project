import random

WORDS = ("whale", "python", "teacher", "apple", "scissors", "boomerang", "alpaca", "coding")
word = random.choice(WORDS)
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

def play():
    print("\nWelcome to Hangman! \nCoded by Ryan and Shirley.\n")
    print("Below is the word with letters represented by an underline.\n")

    dashes = "_ " * len(word) + "\n"
    guesses_left = 8
    wrong = 0

    while guesses_left > 0 and "_" in dashes:
        print(dashes)
        print(str(guesses_left) + " guesses left")
        print(HANGMAN[wrong])
        guess = input("Guess: ")
        guess = guess.lower()

        if len(guess) != 1:
            print("Guess should only have one character.")
        elif guess in word:
            print("That letter is in the word!")
            dashes = update_dashes(word, dashes, guess) 
        else:
            print("That letter is NOT in the word.")
            guesses_left -= 1
            wrong += 1    
    
    if guesses_left == 0:
        print("You lost. The word was: " + str(word) + "\n")  
    else:
        print("You WIN! The word was: " + str(word))

def update_dashes(word, dashes, guess):
    result = ""
    for i in range(len(word)):
        if word[i] == guess:
            result += guess + ' '
        else:
            result += dashes[i*2] + ' '
    return result + '\n'

play() 