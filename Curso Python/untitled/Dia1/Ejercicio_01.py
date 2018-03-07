# -*- coding:UTF-8 -*-
#NOTE: This code is using Python 2.7

"""
Ejercicio 1:

Almacenar los datos de una persona
    - Nombre
    - Apellidos
        - Paterno
        - Materno
    - Edad
    - Peso
    - Altura
    - CURP

Validar su CURP, y de ser válido, calcular su IMC (Índice de Masa Corporal
y mostrar la información de la persona
"""

#Definición de variables a utilizar

Nombre = ""         #Sólo un nombre
ApellidoP = ""      #Apellido Paterno
ApellidoM = ""      #Apellido Materno
Edad = 0            #Edad del usuario
Peso = 0.0          #Peso en Kilogramos
Estatura = 0.0        #Estatura en Metros
CURP = ""           #Clave Única de Registro Poblacional

#Solicitud de los datos del Usuario
#Nombre = raw_input("Ingrese su nombre (Solo el primer nombre): ")
#ApellidoP = raw_input("Ingrese su apellido Paterno: ")
#ApellidoM = raw_input("Ingrese su apellido Materno")
#Edad = int(raw_input("Ingrese su edad: "))
Peso = float(raw_input("Ingrese su peso (Kg): "))
Estatura = float(raw_input("Ingrese su estatura (m): "))
#print("Para validar sus datos, ingrese su CURP: ")
#CURP = raw_input("CURP: ")

#Cálculo del Índice de Masa Corporal
"""
El índice de masa corporal (IMC) se calcula mediante la fórmula:
IMC = Peso/(Estatura^2)
"""
def CalcIMC(p_Peso, p_Est):
    IMC = p_Peso/(p_Est*p_Est)
    print("Su IMC es de: "+str(IMC)+".")
    if IMC < 18:
        print("Su peso es bajo")
    else:
        if IMC >= 18 and IMC < 25:
            print("Su peso es normal")
        else:
            print("Su peso es elevado")
#Fin de la función para calcular IMC

CalcIMC(Peso,Estatura)