__author__ = 'gabriel'
import random

Comision = 0
Resultados = " "
dado1J1 = 0
dado2J1 = 0
dado3J1 = 0
PuntajeJ1 = 0
PuntajeTotalJ1 = 0
bandera1 = 0
apuestamen2000 = 0


dado1J2 = 0
dado2J2 = 0
dado3J2 = 0
PuntajeJ2 = 0
PuntajeTotalJ2 = 0
bandera2 = 0

stringdado1j1 = ""
stringdado2j1 = ""
stringdado3j1 = ""

stringdado1j2 = ""
stringdado2j2 = ""
stringdado3j2 = ""

apuestaJ1 = 0
apuestaJ2 = 0

stringDadoJ1 = ""
stringDadoJ2 = ""


nomJ1 = "Jugador 1"
nomJ2 = "Jugador 2"

def generarJugada1():
    global dado1J1
    global dado2J1
    global dado3J1

    dado1J1 = random.randint(1,6)
    dado2J1 = random.randint(1,6)
    dado3J1 = random.randint(1,6)

def generarJugada2() :
    global dado1J2
    global dado2J2
    global dado3J2

    dado1J2 = random.randint(1,6)
    dado2J2 = random.randint(1,6)
    dado3J2 = random.randint(1,6)

def calcularPuntosJ1():

    global dado1J1
    global dado2J1
    global dado3J1
    global PuntajeJ1
    global PuntajeTotalJ1
    global bandera1

    if dado1J1 == 1:
        PuntajeTotalJ1 = PuntajeTotalJ1 + 1
    if dado2J1 == 1:
        PuntajeTotalJ1 = PuntajeTotalJ1 + 1
    if dado3J1 == 1:
        PuntajeTotalJ1 = PuntajeTotalJ1 + 1

    if dado1J1 == 3:
        PuntajeTotalJ1 = PuntajeTotalJ1 + 2
    if dado2J1 == 3:
        PuntajeTotalJ1 = PuntajeTotalJ1 + 2
    if dado3J1 == 3:
        PuntajeTotalJ1 = PuntajeTotalJ1 + 2

    if dado1J1 == 5:
        PuntajeTotalJ1 = PuntajeTotalJ1 + 4
    if dado2J1 == 5:
        PuntajeTotalJ1 = PuntajeTotalJ1 + 4
    if dado3J1 == 5:
        PuntajeTotalJ1 = PuntajeTotalJ1 + 4


def calcularPuntosJ2() :

    global dado1J2
    global dado2J2
    global dado3J2
    global PuntajeJ2
    global PuntajeTotalJ2
    global bandera2


    if dado1J2 == 1:
        PuntajeTotalJ2 = PuntajeTotalJ2 + 1
    if dado2J2 == 1:
        PuntajeTotalJ2 = PuntajeTotalJ2 + 1
    if dado3J2 == 1:
        PuntajeTotalJ2 = PuntajeTotalJ2 + 1

    if dado1J2 == 3:
        PuntajeTotalJ2 = PuntajeTotalJ2 + 2
    if dado2J2 == 3:
        PuntajeTotalJ2 = PuntajeTotalJ2 + 2
    if dado3J2 == 3:
        PuntajeTotalJ2 = PuntajeTotalJ2 + 2

    if dado1J2 == 5:
        PuntajeTotalJ2 = PuntajeTotalJ2 + 4
    if dado2J2 == 5:
        PuntajeTotalJ2 = PuntajeTotalJ2 + 4
    if dado3J2 == 5:
        PuntajeTotalJ2 = PuntajeTotalJ2 + 4


def stringDados():

    global stringDadoJ1
    global stringDadoJ2
    global stringdado1j1
    global stringdado2j1
    global stringdado3j1

    global stringdado1j2
    global stringdado2j2
    global stringdado3j2

    sDado6 = " ________" '\n'"|º      º|" '\n' "|º      º|" '\n' "|º      º|" '\n' " ¯¯¯¯¯¯¯¯"
    sDado5 = " ________" '\n'"|º      º|" '\n' "|    º   |" '\n' "|º      º|" '\n' " ¯¯¯¯¯¯¯¯"
    sDado4 = " ________" '\n'"|º      º|" '\n' "|        |" '\n' "|º      º|" '\n' " ¯¯¯¯¯¯¯¯"
    sDado3 = " ________" '\n'"|       º|" '\n' "|    º   |" '\n' "|º       |" '\n' " ¯¯¯¯¯¯¯¯"
    sDado2 = " ________" '\n'"|       º|" '\n' "|        |" '\n' "|º       |" '\n' " ¯¯¯¯¯¯¯¯"
    sDado1 = " ________" '\n'"|        |" '\n' "|    º   |" '\n' "|        |" '\n' " ¯¯¯¯¯¯¯¯"

    if dado1J1 == 1:
        stringdado1j1 = sDado1
    if dado1J1 == 2:
        stringdado1j1 = sDado2
    if dado1J1 == 3:
        stringdado1j1 = sDado3
    if dado1J1 == 4:
        stringdado1j1 = sDado4
    if dado1J1 == 5:
        stringdado1j1 = sDado5
    if dado1J1 == 6:
        stringdado1j1 = sDado6


    if dado2J1 == 1:
        stringdado2j1 = sDado1
    if dado2J1 == 2:
        stringdado2j1 = sDado2
    if dado2J1 == 3:
        stringdado2j1 = sDado3
    if dado2J1 == 4:
        stringdado2j1 = sDado4
    if dado2J1 == 5:
        stringdado2j1 = sDado5
    if dado2J1 == 6:
        stringdado2j1 = sDado6

    if dado3J1 == 1:
        stringdado3j1 = sDado1
    if dado3J1 == 2:
        stringdado3j1 = sDado2
    if dado3J1 == 3:
        stringdado3j1 = sDado3
    if dado3J1 == 4:
        stringdado3j1 = sDado4
    if dado3J1 == 5:
        stringdado3j1 = sDado5
    if dado3J1 == 6:
        stringdado3j1 = sDado6

    if dado1J2 == 1:
        stringdado1j2 = sDado1
    if dado1J2 == 2:
        stringdado1j2 = sDado2
    if dado1J2 == 3:
        stringdado1j2 = sDado3
    if dado1J2 == 4:
        stringdado1j2 = sDado4
    if dado1J2 == 5:
        stringdado1j2 = sDado5
    if dado1J2 == 6:
        stringdado1j2 = sDado6


    if dado2J2 == 1:
        stringdado2j2 = sDado1
    if dado2J2 == 2:
        stringdado2j2 = sDado2
    if dado2J2 == 3:
        stringdado2j2 = sDado3
    if dado2J2 == 4:
        stringdado2j2 = sDado4
    if dado2J2 == 5:
        stringdado2j2 = sDado5
    if dado2J2 == 6:
        stringdado2j2 = sDado6

    if dado3J2 == 1:
        stringdado3j2 = sDado1
    if dado3J2 == 2:
        stringdado3j2 = sDado2
    if dado3J2 == 3:
        stringdado3j2 = sDado3
    if dado3J2 == 4:
        stringdado3j2 = sDado4
    if dado3J2 == 5:
        stringdado3j2 = sDado5
    if dado3J2 == 6:
        stringdado3j2 = sDado6

    stringDadoJ1 = stringdado1j1 + '\n' + stringdado2j1 + '\n' + stringdado3j1
    stringDadoJ2 = stringdado1j2 + '\n' + stringdado2j2 + '\n' + stringdado3j2

def evaluarResultados():
    global Resultados

    if PuntajeTotalJ1 > PuntajeTotalJ2 :
        Resultados = '¡¡¡Felicidades ', nomJ1, 'Ganaste!!! :D'
    if PuntajeTotalJ1 < PuntajeTotalJ2 :
        Resultados = '¡¡¡Felicidades ', nomJ2, 'Ganaste!!! :D'

    if PuntajeTotalJ1 == PuntajeTotalJ2 :
        Resultados = nomJ1, " y ",nomJ2," han empatado :O "

def duplicar():
    global bandera1
    global PuntajeTotalJ1
    global  bandera2
    global PuntajeTotalJ2

    if bandera1 == 0 :

        if dado1J1 ==2 and dado2J1 == 2 and dado3J1 == 2:
            PuntajeTotalJ1 = PuntajeTotalJ1 * 2
            bandera1 = 1

        if dado1J1 ==4 and dado2J1 == 4 and dado3J1 == 4:
            PuntajeTotalJ1 = PuntajeTotalJ1 * 2
            bandera1 = 1

        if dado1J1 ==6 and dado2J1 == 6 and dado3J1 == 6:
            PuntajeTotalJ1 = PuntajeTotalJ1 * 2
            bandera1 = 1

    if bandera2 == 0 :

        if dado1J2 ==2 and dado2J2 == 2 and dado3J2 == 2:
            PuntajeTotalJ2 = PuntajeTotalJ2 * 2
            bandera2 = 1

        if dado1J2 ==4 and dado2J2 == 4 and dado3J2 == 4:
            PuntajeTotalJ2 = PuntajeTotalJ2 * 2
            bandera2 = 1

        if dado1J2 ==6 and dado2J2 == 6 and dado3J2 == 6:
            PuntajeTotalJ2 = PuntajeTotalJ2 * 2
            bandera2 = 1

def comisionCasino():
    global Comision
    global apuestamen2000


    if apuestaJ2 + apuestaJ1 < 2000:
        Comision = ((apuestaJ1 + apuestaJ2) / 100 ) * 115
        apuestamen2000 = 1

    if apuestaJ1 + apuestaJ2 >= 2000:
        Comision = ( ( apuestaJ1 + apuestaJ2 ) / 100 ) * 25



print("                 Juego del Púnto ")
nomJ1 = input("Ingrese nombre jugador 1 :")
nomJ2 = input("Ingrese nombre jugador 2 :")
print("$$$$$$$$$$$$$$$$$$$$$---------------$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$| 0           0 |$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$|               |$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$|       *       |$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$|               |$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$| 0           0 |$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$---------------$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("Bienvenidos al Juego del Púnto ",nomJ1, " y ",nomJ2)
print(nomJ1," Ingrese su apuesta a continuacion ")
apuestaJ1 = int(input("ingrese aquí >> :"))

print(nomJ2," Ingrese su apuesta a continuacion ")
apuestaJ2 = int(input("ingrese aquí >> :"))

print("$$$$$$$$$$$$$$$$$$$$$---------------$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$| 0           0 |$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$|               |$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$|       *       |$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$|               |$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$| 0           0 |$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("$$$$$$$$$$$$$$$$$$$$$---------------$$$$$$$$$$$$$$$$$$$$$$$$$$$")

print("$$$$$$$$$$$$$$_Primera Ronda_$$$$$$$$$$$$$", '\n')

print("Túrno de ",nomJ1)
input( "Presione Enter para lanzar")
generarJugada1()
duplicar()
calcularPuntosJ1()
stringDados()
print(stringDadoJ1, '\n',"Puntaje Total De ",nomJ1,": ", PuntajeTotalJ1)
print('\n')

print("Túrno de ", nomJ2)
input("Presione Enter para lanzar")
generarJugada2()
duplicar()
calcularPuntosJ2()
stringDados()
print(stringDadoJ2, '\n', "Puntaje Total De ", nomJ2, ": ", PuntajeTotalJ2)

print("$$$$$$$$$$$$$$_Segunda Ronda_$$$$$$$$$$$$$", '\n')


print("Túrno de ",nomJ1)
input( "Presione Enter para lanzar")
generarJugada1()
duplicar()
calcularPuntosJ1()
stringDados()
print(stringDadoJ1, '\n',"Puntaje Total De ",nomJ1,": ", PuntajeTotalJ1)
print('\n')

print("Túrno de ", nomJ2)
input("Presione Enter para lanzar")
generarJugada2()
duplicar()
calcularPuntosJ2()
stringDados()
print(stringDadoJ2, '\n', "Puntaje Total De ", nomJ2, ": ", PuntajeTotalJ2)

print("$$$$$$$$$$$$$$_Tercera Ronda_$$$$$$$$$$$$$", '\n')

print("Túrno de ",nomJ1)
input( "Presione Enter para lanzar")
generarJugada1()
duplicar()
calcularPuntosJ1()
stringDados()
print(stringDadoJ1, '\n',"Puntaje Total De ",nomJ1,": ", PuntajeTotalJ1)
print('\n')

print("Túrno de ", nomJ2)
input("Presione Enter para lanzar")
generarJugada2()
duplicar()
calcularPuntosJ2()
stringDados()
print(stringDadoJ2, '\n', "Puntaje Total De ", nomJ2, ": ", PuntajeTotalJ2)


print("$$$$$$$$$$$$$$_Cuarta y Última Ronda_$$$$$$$$$$$$$", '\n')

print("Túrno de ",nomJ1)
input( "Presione Enter para lanzar")
generarJugada1()
duplicar()
calcularPuntosJ1()
stringDados()
print(stringDadoJ1, '\n',"Puntaje Total De ",nomJ1,": ", PuntajeTotalJ1)
print('\n')

print("Túrno de ", nomJ2)
input("Presione Enter para lanzar")
generarJugada2()
duplicar()
calcularPuntosJ2()
stringDados()
print(stringDadoJ2, '\n', "Puntaje Total De ", nomJ2, ": ", PuntajeTotalJ2)


input("|||||| Presione enter para Mostrar Resultados Finales |||||||")
evaluarResultados()
print("Resultados de la partida : ",Resultados)
comisionCasino()
if apuestamen2000 == 0:
    print("La comisión será del 25% del monto total")
if apuestamen2000 == 1:
    print("La comisión será del 15% del monto total")

print("La comisión del Casino es de : ", Comision, "$")
montoGanado = (apuestaJ1 + apuestaJ2) - Comision
print("Usted a ganado : ", montoGanado)







