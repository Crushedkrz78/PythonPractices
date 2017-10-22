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

print("-----Elementos de la lista a: ")
for element in a:
    print(str(element) + " ", end='')
print("\n-----Elementos de la lista b: ")
for element in b:
    print(str(element) + " ", end='')

#Now validating common elements
c = []
print("\n-----Elementos en común para las listas a y b")
for element in a:
    if element in b and element not in c:
        c.append(element) #If element does not exists in C, then it's added

#The next line prints another list that not storages repeated elements
for element in c:
    print(str(element) + " ", end='')

#Extra 1: Randomly generted lists
"""
In this case, I'll ask user to define the size of both lists, that way, the code will fill both lists and perform
the code that finds common elements in both lists, also it is necessary to print what's on both lists.
"""
print("\n------------------------------------------------------")
import random
print("Elementos en común con listas llenadas aleatoriamente")
sizeA = int(input("¿De qué tamaño será la lista A?: "))
sizeB = int(input("¿De qué tamaño será la lista B?: "))

#Elements on both lists would have random numbers between 1 and 2000, so the range is arbitrary
a = random.sample(range(1,2000), sizeA)
b = random.sample(range(1,2000), sizeB)
c = []

#Now showing what's storaged on both lists
print("-----Elementos de la lista a: ")
for element in a:
    print(str(element) + " ", end='')
print("\n-----Elementos de la lista b: ")
for element in b:
    print(str(element) + " ", end='')

#Now validating common elements
print("\n-----Elementos en común para las listas a y b")
for element in a:
    if element in b and element not in c:
        c.append(element) #If element does not exists in C, then it's added

#The next line prints another list that not storages repeated elements
for element in c:
    print(str(element) + " ", end='')
"""
Solution coded by: KriztyanPM
Date: 10/19/2017 [19/10/2017 for Mexico]
Exercise from: http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
Main topic finished on: 10/22/2017 [22/10/2017 in Mexico]
"""