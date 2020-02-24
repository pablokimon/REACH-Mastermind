# Requirements: Python 3 and an internet connection

'''
Mastermind is a command line game based on the boardgame of the same name.
This code was created as part of a seven day coding challenge in February 2020 by Paul Knowles
It does require an internet connection as it implements the random.org random integer generator to create the number combinations to be guessed.

'''

import requests
import json
from collections import defaultdict
import sys
from random import shuffle
from time import sleep
import os
import subprocess




def getRandomPattern(pattern_length,pattern_start,pattern_end):
    '''returns a list of a series of random numbers based on the parameters passed in.
    
    '''
    print('Please wait...generating random pattern...',end='')
    url = 'https://www.random.org/integers/' #integer generator
    params = {'num':pattern_length,'min':pattern_start,'max':pattern_end,'col':1,'base':10,'format':'plain','rnd':'new'} # api parameters
    response = requests.get(url,params) #save the contents of the get request to a variable, returns a plain text list of numbers with \n new line after each number
    pattern = [int(x) for x in response.text.strip('\n').split('\n')] #parse the response into a nice list: remove the last \n from the string, split on \n and use list comprehension to convert each string into an integer
    
    print("Random pattern generated, let's play!") 
    return pattern




def checkGuess(guess,pattern):
    '''
    Compares a guess by the user to the computer's pattern. 
    This function expects both guess and pattern to be lists of the same size.
    This similarity is checked when the guess is captured before it is passed here.
    We iterate through the guess from index 0.
    First we check for correct number and location and then correct number from remaining elements.
    '''
    
    correctLocation = 0 #counter for number of guesses that are in the correct number and location
    correctNumber = 0 #conter for the number of guesses that are only a correct number but NOT in the correct place
    pattern_copy = pattern.copy() # a copy of the pattern so the correct location numbers can be removed and compared to the other guess values
    guess_copy = guess.copy() # a copy of the guess so that the correct location numbers can be removed and the remaining compared to the pattern_
    
    for x in range(len(guess)): #loops over the length of the guess, uses x as an index of the list
        if guess[x] == pattern[x]: #check if the index of the guess is in the correct place and correct number then increment counter
            correctLocation += 1 
            pattern_copy.remove(guess[x]) #remove first instance of current correct guess number from pattern_copy so it doesn't get counted again
            guess_copy.remove(guess[x]) # remove first instance of current correct guess number from guess_copy so it doesn't get counted again
    
    for x in guess_copy: # to find number only matches, iterate through remaining values in guess_copy to check if they are included in remaing pattern_copy
        if x in pattern_copy: #if element of guess_copy is in pattern_copy,
            correctNumber += 1 # increment correct number
            pattern_copy.remove(x) # and remove from pattern_copy so it doesn't get counted again
    
    return correctNumber,correctLocation #return the counts of correct number only and correct number and location, respectively




def guessInRange(guess,pattern_range):
    '''iterates through the guess and checks if the elements are in the range of the pattern,
    as soon as an element is found outside the range, return false'''
    for g in guess:
        if g not in pattern_range:
            print("Sorry one of your guesses was outside the range")
            return False
        else:
            return True




def giveHint():
    '''to be completed, gives hint based on previous guesses'''
    print("Here's a hint, try something different.")
    pass





def getGuess(guess_number,pattern_length,pattern_start,pattern_end,pattern_range):
    '''
    This function captures the guess via keyboard input and verifies that the guess is the same length as the pattern
    and that the elements of the guess are integers that fall within the pattern range. 
    This function also provides for expanded functions like quit, hint, restart, etc.
    '''
    
    while True:
        try:
            guess = input('Guess # {}: Please enter {} numbers between {} and {} inclusive '.format(guess_number,pattern_length,pattern_start,pattern_end)) # captures guess displaying length, start and end of guess number range
            
            if guess.lower() == 'q' or guess.lower() == 'quit': # quits game
                sys.exit()
            
            if guess.lower() == 'r' or guess.lower() == 'reset' or guess.lower() == 'restart': # restarts game
                startGame()
                
            if guess.lower() == 'h' or guess.lower() == 'hint': # gives hint
                giveHint()
                continue
                
            guess =[int(g) for g in guess] #converts the guess into a list of integers
            
        except ValueError: #catches the error if the input is not integers and tries again
            print ('Oops you entered something other than numbers')
            continue 
        
        if len(guess) != pattern_length: #catches the error if the input doesn't match the length of the pattern and tries again
            print ("Oops your guess wasn't %d numbers long" %pattern_length)
            continue

        elif not guessInRange(guess,pattern_range): #checks if elements of guess are all within the pattern range. I tried to get this working in an if statement, but had to move it outside to a function
            continue
            
        else:
            return guess                                





def setParameters(pattern_length, pattern_start, pattern_end, max_guess):
    '''This function is used to set the game parameters to values other than the default values
    it is not complete and could use a nice function to capture good values for these parameters to avoid repeated code
    '''
    
    print ('Press the corresponding number to change a parameter or press enter to return to the game:')
    print ('1. Pattern Length', pattern_length)
    
    print ('''
    Press the corresponding number to change a parameter or press enter to return to the game:
    1. Pattern Length: {}
    2. Pattern Range Start: {}
    3. Pattern Range End: {}
    4. Maximium Number of Guesses: {}
    0. Return to Game
    '''.format(pattern_length, pattern_start, pattern_end, max_guess))
    
    while True:
        try:
            parameter_number = int(input('Which parameter would you like to change?'))
    
            if parameter_number == 1:
                pass
            if parameter_number == 2:
                pass
            if parameter_number == 3:
                pass
            if parameter_number == 4:
                pass
            if parameter_number == 0:
                pass
        except ValueError:
            print ('Oops please enter a number from the menu above.')
            continue





def shuffleWord(word='mastermind',shuffles=10): 
    '''This function shuffles the letter in the word mastermind in place and then displays the word'''

    word_upper = [m.upper() for m in word] #make the word uppercase
    word_shuffled = word_upper.copy() # make a copy to be shuffled
    for x in range(shuffles): # setup a loop for shuffling the word, arbitrarily the length of the word + 1 LOL
        shuffle(word_shuffled) # shuffle a copy of the word
        print('\r',''.join(word_shuffled),end='') #print the shuffled word on the same line over itself
        sleep(0.5) # wait half a second 
 
    print('\r','*'*len(word),end='') # print a line of astericks for emphasis before...
    sleep(0.5) # wait a half second...
    print ('\r',''.join(word_upper),end='') # display the original unshuffled word
    #sleep(2) #wait two seconds
    #print ('\r',' '*len(word))





def clear():
    '''a niftly little function to clear the terminal screen which requires os and subprocess.
    Always standing on the shoulders of giants, original source: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console'''
    if os.name in ('nt','dos'):
        subprocess.call("cls")
    elif os.name in ('linux','osx','posix'):
        subprocess.call("clear")
    else:
        print("\n") * 120



        
def startGame():
    
    pattern_length = 4
    pattern_start = 1
    pattern_end = 8
    pattern_range = [r for r in range(pattern_start,pattern_end+1)]
    guess_number = 0
    max_guess = 10
    result_dict = defaultdict(dict)
    win = False
    
    clear()
    shuffleWord() #
    
    print('''
    
Game rules:

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

Got it?


Press \'s' now to change game settings
Press \'r' to reset the game
Press \'q' at anytime to quit 

Press enter to play!
    ''')

    _ = input()
    if _.lower()=='s': #change game settings
        setParameters(pattern_length, pattern_start, pattern_end, max_guess)
    
    if _.lower() == 'q' or _.lower() == 'quit': # quits game
        sys.exit()    
    
    clear() # clears the terminal window

    pattern = getRandomPattern(pattern_length,pattern_start,pattern_end) #generates pattern using random.org/integers api
    
    while guess_number < max_guess: # continue game play while player still has guesses
        print ('You only have {} guesses remaining!'.format(max_guess-guess_number))
        guess_number += 1 #increment guesses

        guess = getGuess(guess_number,pattern_length,pattern_start,pattern_end,pattern_range) #capture valid guess
        correctNumber, correctLocation = checkGuess(guess,pattern) #check guess against pattern

        #shuffleWord(word='checking',shuffles=2)
        
        if correctLocation == 4: #stop game play if correct guess
            win = True
            break
        else:
            print ('Try again...')
            #shuffleWord(word='Wrong!',shuffles=3) # if guess not correct, shame them lightly and continue     
            
        result_dict[guess_number]={'Guess':guess,'Correct Number':correctNumber, 'Correct Location':correctLocation} # add guess and results to dict
        for keys,values in result_dict.items(): #iterate through dict of guess results
            print('Guess #',keys,values['Guess'],'Correct Number Only:',values['Correct Number'],'Correct Number and Location:',values['Correct Location']) # print each guess and results for review
  
    if win: 
        shuffleWord(word='Congratulations!',shuffles=5) #shuffle congrats
        print ('You guessed the pattern in {} guesses! the pattern was {}'.format(guess_number,pattern))
    else:
        print ('Too Bad you lost, the pattern was ',pattern)
    
    print('')
    again = input('Would you like to play again(y/n)?')
    if again.lower() == 'y':
        startGame()
    else:
        sys.exit()





if __name__ == "__main__":
    startGame()
