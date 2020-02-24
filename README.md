# REACH Project: Mastermind

This is a command line implementation of the board game Mastermind written by Paul Knowles in Python as a coding exercise for the LinkedIn REACH program.

## Table of Contents:

1. [Game Overview](README.md#game-overview)
2. [Game Rules](README.md#game-rules)
3. [Code Explanation](READme.md#code-explanation)
4. [Challanges](README.md#challenges)
5. [Next Steps](README.md#next-steps)
6. [Takeaways](README.md#takeaways)

# Game Overview

To run this game on your local machine, clone this repo and simply run the mastermind.py file from the command line.

You will need Python 3.5, the requests package and an internet connection.


# Game Rules

At the start of the game the computer will randomly select a pattern of four different numbers from a total of 8 different numbers.
The player will then have 10 chances to correctly guess the pattern.

After each guess attempt, the computer will provide feedback whether the player:
    •had guessed a number correctly, and/or
    •had guessed a number and location correctly.

The computer will not tell you which numbers you guessed correctly, you must use a combination of skill, luck and deductive reasoning to win!

Example game play:
If the pattern was [4,5,6,7]
and you guessed    [7,5,1,2]

The computer will tell you:
Correct Location and Number: 1, Correct Number Only: 1

Which means:
you got one number and location right (5)
you got one number right (7) but in the wrong location

# Code Explanation

The entire game is contained inside the mastermind.py file, except for the libraries imported and the API call.

The file starts with importing the neccessary dependancies from the python libraries.

The functions:
  * getRandomPattern performs a call to the www.random.org/integers API to obtain random integers for the pattern to be guessed.

  * checkGuess compares the guess to the pattern and returns the count of correct numbers only and correct numbers in the correct location.
  
  * guessInRange checks if the guess contains numbers in the range of numbers which the random pattern is drawn from.
  
  * giveHint is unfinished and would be used to generate a hint for the user if they are stuck.
  
  * getGuess takes input from the user and verifies it meets the requirements of the game (integer, in range and correct length)
  
  * setParameters is unfinished and would be used to change the parameters of the game (patter size, pattern range, number of guesses, etc)
  
  * shuffleWord is a simple little function purely decorative to shuffle the letters of a word in place then display the unshuffled word after a set number of shuffles.
  
  * clear is an operting system agnostic function I found on stackoverflow which is used to clear the output screen.
  
  * startGame is the driver which contains the default game parameter values and puts it all together
  
  
# Challanges

I've played to board game a few times recently and was actually considering how to implement this game in Python while playing it.

The first challenges were making sure to get good input from the user that satisfied a guess that could be compared to the pattern.

The second challenge was successfully comparing the guess to the pattern. Initially I was over valuing matches and had to modify my approach. First I thought if I checked for number and location then number only that would catch all cases. But that approach didn't account for a location and number match later in the pattern and gave a false positive for a number only match that was earlier in the pattern. Ultimately I made a copy of the pattern and guess, removed the number and location matches then compared the remaining values to determine number only matches.

The third challenge was unpacking the dictionary of guess results and displaying them in an effective way for the player to use them to make better guesses.

Overall I really enjoyed creating this on a timeline and look forward to adding more to it.

# Next Steps
