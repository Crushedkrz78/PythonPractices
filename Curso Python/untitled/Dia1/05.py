"""Creacion de Listas y Tuplas"""

#Una lista es dinamica (List)

a = []  #Esto es una lista
a = list() #Una poco convencional y no recomendada de hacer una lista
a = [1,2,3,4] #Una lista, ya con valores
a = [1, "Hola", (1,2), True, -1.4] #Una lista con valores de diferentes tipos


#Una tupla es estatica (Array)

a = ()      #Creacion de una tupla
a = tuple() #Creacion de una tupla
a = (1, "Hola", (1,2), True, -1.4) #Puede contener elementos diferentes
a = (1,)    #Tupla con un unico elemento

#Acceso a los datos
print(a[0])

#Agregar datos al final de una lista
a = [1,2,3,4]
print(a)

a.append(5)
print(a)

#Agregar datos en un lugar especifico de la lista
a.insert(1,1.5)
print(a)

#Eliminar un valor de una lista
a.remove(1.5)
print(a)

#Eliminar un elemento en una posicion especifica
del a[0]
print(a)

#Eliminar todos los elementos de una lista
del a[:]
print(a)