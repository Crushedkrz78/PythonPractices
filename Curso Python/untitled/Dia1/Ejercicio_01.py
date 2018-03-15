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
#CURP = ""           #Clave Única de Registro Poblacional

#Solicitud de los datos del Usuario
"""
Nombre = raw_input("Ingrese su nombre (Solo el primer nombre): ")
ApellidoP = raw_input("Ingrese su apellido Paterno: ")
ApellidoM = raw_input("Ingrese su apellido Materno: ")
Edad = int(raw_input("Ingrese su edad: "))
Peso = float(raw_input("Ingrese su peso (Kg): "))
Estatura = float(raw_input("Ingrese su estatura (m): "))
"""
print("Para validar sus datos, ingrese su DNI: ")
DNI = raw_input("DNI: ")

def valDNI(p_DNI):
    letrasDNI = ("T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E")
    #Determinar si el DNI es de ciudadano Español o Residente Extranjero
    tempNIF = p_DNI[1:len(p_DNI)]
    NIE = ["X", "Y", "Z"]
    if p_DNI[0] == "X":
        p_DNI = str(0)+tempNIF
    elif p_DNI[0] == "Y":
        p_DNI = str(1) + tempNIF
    elif p_DNI[0] == "Z":
        p_DNI = str(2) + tempNIF
    #Si no hay letra X, Y o Z al inicio, el DNI pertenece a ciudadano Español
    numDNI = int(p_DNI[0:len(p_DNI)-1])
    letraDNI = p_DNI[8]
    calcLetraDNI = numDNI % 23
    if letraDNI == letrasDNI[calcLetraDNI]:
        print("La DNI fue ingresada y validada correctamente")
    else:
        print("La DNI ingresada contiene un error, intente nuevamente")

valDNI(DNI)


#Cálculo del Índice de Masa Corporal
"""
El índice de masa corporal (IMC) se calcula mediante la fórmula:
IMC = Peso/(Estatura^2)
"""
def CalcIMC(p_Peso, p_Est):
    IMC = p_Peso/(p_Est*p_Est)
    print("Tiene un IMC de: "+str(IMC)+".")
    print("Por lo tanto:")
    if IMC < 18:
        print("--Su peso es bajo")
    else:
        if IMC >= 18 and IMC < 25:
            print("--Su peso es normal")
        else:
            print("--Su peso es elevado")
#Fin de la función para calcular IMC
"""
#Mostrar datos ingresados del usuario
print("------------------------------------------------")
print("El usuario "+Nombre+" "+ApellidoP+" "+ApellidoM)
print("de "+str(Edad)+" años.")
print("Peso: "+str(Peso)+" Kg")
print("Estatura: "+str(Estatura)+" mts")
CalcIMC(Peso,Estatura)
print("------------------------------------------------")
"""