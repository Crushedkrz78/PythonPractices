#This is the first Python code I make
"""
So I am using te very basic concepts for my understandig of this interesting language
So, Let's just starts and let's see how we progress through time while we are programming.
"""

#Basic Python concepts
print("-------------------------------------------------")
print("---------------Dynamic Typing Examples-----------")
"""
Dynamic Typing
Tipado dinámico
"""
print("-------------------------------------------------")
x = 8 #Assign X value
y = x #Assing Y value

print("X value: "+ str(x)) #X value at this point
print("Y value: "+ str(y)) #Y value at this point

x= 4 #Changing X value

print("X value: "+ str(x)) #X value at this point
print("Y value: "+ str(y)) #Y value at this point

print("-------------------------------------------------")
list_1 = [9, 8, 7] #Assing multiple values
list_2 = list_1    #Assing multiple values

print(list_1)      #List_1 values at this point
print(list_2)      #List_2 values at this point

list_1[2] = 5   #Changing on value from list_1

print(list_1)      #List_1 values at this point
print(list_2)      #List_2 values at this point

#Note that the changed value affects both lists
print("-------------------------------------------------")
#Showing data types
print("X is: "+str(type(x)))
print("List_1 is: "+str(type(list_1)))

print("-------------------------------------------------")
"""
Numbers
"""
print("-------------Numbers Exmples---------------------")
print("-------------------------------------------------")
Int_Number = 8
Negative_Number = -78
Real_Number = 4.5
Complex_Number = 3.5 + 4j
Real_sci_Number = 0.5e-4
print("Int Number: "+str(Int_Number))
print("Negative Number: "+str(Negative_Number))
print("Real Number: "+str(Real_Number))
print("Complex Number: "+str(Complex_Number))
print("Scientific Notation Number: "+str(Real_sci_Number))
print("-------------------------------------------------")