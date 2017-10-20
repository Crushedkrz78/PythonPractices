"""
List Overlap

Exercise 5
Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.

Extras
1.- Randomly generate two lists to test this.
2.- Write this in one line of Python (Don't worry if you can't figure this out at this point
    (We'll get to it soon).
"""
#First part of the program
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print("Elementos de la lista a: ")
for element in a:
    print(element)
print("Elementos de la lista b: ")
for element in b:
    print(element)

#Now validating common elements
print("Elementos en común para las listas a y b")
for element in a:
    if element in b:
        print(element)
#For now this program is not completed, I'll work on it later

"""
Solution coded by: KriztyanPM
Date: 10/19/2017 [19/10/2017 for Mexico]
Exercise from: http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
"""