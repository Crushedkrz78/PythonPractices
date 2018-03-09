# -*- coding:UTF-8 -*-
#NOTE: This code is using Python 2.7
import re

"""
Ejercicio 2:

Validar usuario y contraseña insertados por teclado.
La información se debe encontrar en dos tuplas:
    - Una Tupla para usuarios
    - Una Tupla para contraseñas
"""

#Tupla para usuarios
usr = ("root","Cris","Val","Diana")

#Tupla para contraseñas
psw = ("0000","Cris078","Val014","Diana006")

#Validacion de Usuario y Contraseña mediante posiciones
def Check():
    v_usr = raw_input("Usuario: ")
    v_psw = raw_input("Contraseña: ")
    pos = 0
    found = False
    while pos < len(usr) and not found:
        if(v_usr == usr[pos]):
            if(v_psw == psw[pos]):
                found = True
            else:
                pos = pos + 1
        else:
            pos = pos + 1
    if found:
        print("Acceso permitido: \nBienvenido")
    else:
        print("Usuario o contraseña no válidos, intente nuevamente")
        Check()

Check()