"""
Exercise 9
Generate random number between 1 and 9 (Incluiding 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low,
too high, or exactly right
(Hint: Remember to use the user input lessons from the very first exercise)

Extras:
 - Keep the game going until the user types "exit"
 - Keep track of how many guesses the user has taken, and when the game ends,
   print this out.

Notes:
    This exercise was solved using Python 3.6.5
"""
#Import Resources Section-----
import random as rnd

#Initialize Variables Section-----
cycle_flag = True
score_counter = 0
fail_attempt_counter = 0

#Cycle that keeps game running
while(cycle_flag):
    guess_number = rnd.randint(1,9)
    #print(guess_number)

    usr_input = input("Choose a number between 1 and 9 or write \"exit\" to end game: \n")
    #print(" -Random Number: %s\n -User Number: %s" %(guess_number,usr_number))
    if usr_input == "exit":
        cycle_flag = False
        print("User Score: %s \nFailed attempts: %s" %(score_counter, fail_attempt_counter))
    elif usr_input.isnumeric():
        usr_number = int(usr_input)

        #Comparing numbers Section-----
        diff = guess_number - usr_number
        #print("Absolute difference between numbers: %s" %diff)

        if diff == 0:
            print ("---You nailed it!---")
            score_counter += 1
        elif diff < 0:
            print("---The number is too high---")
            fail_attempt_counter += 1
        else:
            print("---The number is too low---")
            fail_attempt_counter += 1
    else:
        print("Please, insert a number bigger that 0 or insert \"exit\" to continue\n")

"""
Coded by: KriztyanPM
Date: 08/14/2018 [14/08/2018 in Mexico]
Exercise from: http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
"""