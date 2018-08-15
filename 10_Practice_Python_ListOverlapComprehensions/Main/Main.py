"""
Exercise 10
Take two lists, for example:
    a = [1,1,2,3,5,8,13,21,34,55,89]
    b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.
Write this using at least one list comprehension.

Extra:
 - Randomly generate two lists to test this

Notes:
    This exercise was solved using Python 3.6.5
"""
import random
#Variables to be used (Pre-Defined lists)
#a = [1,1,2,3,5,8,13,21,34,55,89]
a = [1,1,1,1]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]

#Full randomly generated lists
range_v = range(1,100)
c = random.sample(range_v,random.randint(1,10))
d = random.sample(range_v,random.randint(1,10))
#print(c)
#print(d)
final_list = []
final_list = [y for y in a if y in b and y in final_list]
print(final_list)

"""
Coded by: KriztyanPM
Date: 08/14/2018 [14/08/2018 in Mexico]
Exercise from: http://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
"""