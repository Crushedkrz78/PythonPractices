"""
Divisors

Exercise 4
Create a program that asks for a number and then prints out a list of all the divisors of that number.
(If you don't know what a divisor is, it is a number that divides evenly into another number.
    For example, 13 is divisor of 26 because 26/13 has no remainder).
"""
print("Ejercicio 4---------------------------------------------------------------")
usr = int(input("Ingresa un número: "))
div = range(2, usr)

print("Los números que son divisores de "+str(usr)+" son:")
for element in div:
    if (usr % element) == 0:
        print(element)

"""
Solution coded by: KriztyanPM
Date: 10/15/2017 [15/10/2017 for Mexico]
Exercise from: http://www.practicepython.org/exercise/2014/02/26/04-divisors.html
"""