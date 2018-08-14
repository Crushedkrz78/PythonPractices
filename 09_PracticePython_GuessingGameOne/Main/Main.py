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
guess_number = rnd.randint(1,9)
#print(guess_number)
usr_number = int(input("Choose a number between 1 and 9: "))
#print(" -Random Number: %s\n -User Number: %s" %(guess_number,usr_number))

#Comparing numbers Section-----
diff = guess_number - usr_number
#print("Absolute difference between numbers: %s" %diff)

if diff == 0:
    print ("---You nailed it!---")
elif diff < 0:
    print("---The number is too high---")
else:
    print("---The number is too low---")

