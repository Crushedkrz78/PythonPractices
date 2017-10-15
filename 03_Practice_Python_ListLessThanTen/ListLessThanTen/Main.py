"""
List Less Than Ten
list numbers elements if conditional

Exercise 3
Take a list, say for example this one:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all elements of the list that are less than 5.

Extras:
1.- Instead of printing the elements one by one, make a new list that has all the elements less than 5 fromm this list
    in it and print out this new list.
2.- Write this one line of Python.
3.- Ask the user for a number and return a list that contains only elements from the original list "a" that are smaller
    than that number given by the user.
"""

#Example list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#Printing all "a" elements
print("Elementos de la lista a: ")
for element in a:
    print(str(element)+" ", end='')
print("")

#Printing elements less than 5 from "a" list
print("Elementos menores a 5 de la lista a: ")
for element in a:
    if element < 5:
        print(str(element) + " ", end='')

#
"""
Solution coded by: KriztyanPM
Date: 10/14/2017 [14/10/2017 for Mexico]
Exercise from: http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
"""