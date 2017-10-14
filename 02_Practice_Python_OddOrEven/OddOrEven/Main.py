"""
Odd or Even
input if types equality comparison numbers mod

Exercise 2
Ask the user for a number. Depending on whether the number is even or odd, print out an appropiate message to the
user.
Hint: How does an even/odd number react differently when divided by 2?

Extras:
1.- If the number is a multiple of 4, print out a different message.
2.- Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
    If check divides evenly into num, tell that to the user. If not, print a different appropiate message.
"""
print("---Par o Impar---")

#Ask numbers
num = int(input("Ingresa un número: "))

#Verify number
result = num % 2

#Show results
if result == 1:
    print("El número "+str(num)+" es impar.")
elif result == 0:
    print("El número "+str(num)+" es par.")

#Verify Extra 1
result = num % 4

#Show results Extra 1
if result == 0:
    print("El número "+str(num)+" es divisible entre 4.")
else:
    print("El número "+str(num)+" no es divisible entre 4.")

#Verify Extra 2
#Ask numbers for Extra 2
print("---------------------")
num = int(input("Ingrese un número divisor: "))
check = int(input("Ingrese un número dividendo: "))

#Calculate and validate numbers
result = check % num

print(result)
#Show results
if result == 0:
    print("El dividendo es completamente divisible entre el divisor.")
else:
    print("El dividendo no es divisible entre el divisor.")