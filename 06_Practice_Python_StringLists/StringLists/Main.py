"""
Exercise 6
Ask the user for a string and print out whether this strings is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards).
"""
#Asking for a word for analize if it's Palindrome
print("---Analizador de Palindromes---")
ask = input("Ingresa una palabra: ")
word = []
drow = []
ind = len(ask) - 1
for letter in ask:
    word.append(letter)
    drow.insert(0,letter)

while ind >= 0:
    if word[ind] == drow[ind]:
        ind -= 1
        if ind == 0:
            print("La palabra es palíndromo")
    else:
        ind = -1
        print("La palabra no es palíndromo")

"""
Solution coded by: KriztyanPM
Date: 10/19/2017 [25/10/2017 for Mexico]
Exercise from: http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
"""