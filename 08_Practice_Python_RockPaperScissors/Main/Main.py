"""
Exercise 8
Make a two-player Rock-Paper-Scissors game.
Compare multiple inputs, print out a message  of ocngratulations to the winner,
and ask if the players want to start a new game.

Remembering the rules:
 - Rock beats Scissors
 - Scissors beats Paper
 - Paper beats Rock
"""

"""
    For this program we can convert every playabe element to a code
    1 - Rock
    2 - Paper
    3 - Scissors
    
    Finally the program prints which hand is better and who won the game
"""
#Defining soma variables
player1 = 0
player2 = 0
status = -100
game = ["Piedra", "Papel", "Tijeras"]

#Starting game
while(status != 1):
    player1 = int(input("Jugador 1, Ingrese su mano: \n"
                    "1.- Piedra\n"
                    "2.- Papel\n"
                    "3.- Tijera\n"))
    player2 = int(input("Jugador 2, Ingrese su mano: \n"
                    "1.- Piedra\n"
                    "2.- Papel\n"
                    "3.- Tijera\n"))

    #print("Mano del jugador 1: " + game[player1 - 1])
    #print("Mano del jugador 2: " + game[player2 - 1])

    if player1 == 1 and player2 == 3:
        print("Gana el jugador 1")
        print(game[player1 - 1]+" > "+game[player2 - 1])
        break

    if player2 == 1 and player1 == 3:
        print("Gana el jugador 2")
        print(game[player2 - 1] + " > " + game[player1 - 1])
        break

    if player1 > player2:
        print("Gana el jugador 1")
        print(game[player1 - 1] + " > " + game[player2 - 1])
        break
    else:
        print("Gana el jugador 2")
        print(game[player2 - 1] + " > " + game[player1 - 1])
        break

#This version of the game is unoptimized and can be reduced to a smaller and faster code

"""
Coded by: KriztyanPM
Date: 01/05/2018 [05/01/2018 in Mexico]
Exercise from: http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
"""