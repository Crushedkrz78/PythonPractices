# -*- coding: UTF-8 -*-

"""
    This script is intended to practice file management with Python 2.7
"""

#Creating file object
file_object = open("TestFile.txt", "w")

#Wrhiting into the f¿new file
file_object.write(raw_input("Enter text to write into new file: "))

#Closing file
file_object.close()

#Reading file created previously
readF = open("TestFile.txt", "r")
print readF.read()
readF.close()