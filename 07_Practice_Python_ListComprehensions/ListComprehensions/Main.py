"""
List Comprehension

Exercise 7

Let's say I give you a list saved in a variable:

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Write one line of Python that takes this list and makes a new list that has only the even
elements of this list in it.
"""
#Let's crete the mai list of the elements
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#One line condenses a loop for and an if sentence into a list
even = [evNum for evNum in a if evNum % 2 == 0]

#Then finally print the results
for result in even:
    print("Numeros Pares: "+str(result))
"""
Coded by: KriztyanPM
Date: 10/28/2017 [28/10/2017 in Mexico]
Exercise from: http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
"""