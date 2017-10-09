#Practice from PracticePython.org
"""
Character Input
input string type int

Exercise 1
 Create a program that asks the user to enter their name and their age. Print out the message addressed to them
 that tells them the year that they will turn 100 years old.

 Extras:
 1.- Add on to the previous program by asking the user for another number and printing out many copies of the
     previous message. (Hint: order of operations exists in Python)
 2.- Print out that many copies of the previous messge on separate lines. (Hint: the string "\n is the same as pressing
     the ENTER button)
"""

#Asking name
name = input("Give me your name: ")

#print("The name given was: " + name)

#Asking Age
age = input("Give me your age: ")
age = int(age) #What you get from input() is a string, so you can make your string into a number
#print("Your age was: " + str(age)) #It's necessary to convert number types to string type when printing

"""
Another way to get a number from user in a compact form is:
age = int(input("Give age: "))
"""
year = int(input("What year is it?: "))

cicle = int(input("How many times you want to repeat the message?: "))

#Now let's calculate the year when you'll be 100 years old
#year = year - age
#year = year + 100

#Another way to clculate it
year = year + (100 - age)

message1 = "Your name is: "+name+". Your actual age is: "+str(age)+". \n"
message = "Hi "+name+", you'll be 100 years old in year "+ str(year) + ". \n"
print(cicle * message)

"""
Solution coded by: KriztyanPM
Date: 10/08/2017 [08/10/2017 for Mexico]
Exercise from: http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
"""
