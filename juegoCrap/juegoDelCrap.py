__author__ = 'Avendaño '


import random

def juego_punto():
    def lanzamientos() :
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        dado3 = random.randint(1,6)

        if dado1 == 1:
            print(" ________" '\n'"|        |" '\n' "|    º   |" '\n' "|        |" '\n' " ¯¯¯¯¯¯¯¯")
        elif dado1 == 2:
            print(" ________" '\n'"|       º|" '\n' "|        |" '\n' "|º       |" '\n' " ¯¯¯¯¯¯¯¯")
        elif dado1 == 3:
            print(" ________" '\n'"|       º|" '\n' "|    º   |" '\n' "|º       |" '\n' " ¯¯¯¯¯¯¯¯")
        elif dado1 == 4:
            print(" ________" '\n'"|º      º|" '\n' "|        |" '\n' "|º      º|" '\n' " ¯¯¯¯¯¯¯¯")
        elif dado1 == 5:
            print(" ________" '\n'"|º      º|" '\n' "|    º   |" '\n' "|º      º|" '\n' " ¯¯¯¯¯¯¯¯")
        elif dado1 == 6:
            print(" ________" '\n'"|º      º|" '\n' "|º      º|" '\n' "|º      º|" '\n' " ¯¯¯¯¯¯¯¯")

        if dado2 == 1:
            print(" ________" '\n'"|        |" '\n' "|    º   |" '\n' "|        |" '\n' " ¯¯¯¯¯¯¯¯")
        elif dado2 == 2:
            print(" ________" '\n'"|       º|" '\n' "|        |" '\n' "|º       |" '\n' " ¯¯¯¯¯¯¯¯")
        elif dado2 == 3:
            print(" ________" '\n'"|       º|" '\n' "|    º   |" '\n' "|º       |" '\n' " ¯¯¯¯¯¯¯¯")
        elif dado2 == 4:
            print(" ________" '\n'"|º      º|" '\n' "|        |" '\n' "|º      º|" '\n' " ¯¯¯¯¯¯¯¯")
        elif dado2 == 5:
            print(" ________" '\n'"|º      º|" '\n' "|    º   |" '\n' "|º      º|" '\n' " ¯¯¯¯¯¯¯¯")
        elif dado2 == 6:
            print(" ________" '\n'"|º      º|" '\n' "|º      º|" '\n' "|º      º|" '\n' " ¯¯¯¯¯¯¯¯")

        if dado3 == 1:
            print(" ________" '\n'"|        |" '\n' "|    º   |" '\n' "|        |" '\n' " ¯¯¯¯¯¯¯¯")
        elif dado3 == 2:
            print(" ________" '\n'"|       º|" '\n' "|        |" '\n' "|º       |" '\n' " ¯¯¯¯¯¯¯¯")
        elif dado3 == 3:
            print(" ________" '\n'"|       º|" '\n' "|    º   |" '\n' "|º       |" '\n' " ¯¯¯¯¯¯¯¯")
        elif dado3 == 4:
            print(" ________" '\n'"|º      º|" '\n' "|        |" '\n' "|º      º|" '\n' " ¯¯¯¯¯¯¯¯")
        elif dado3 == 5:
            print(" ________" '\n'"|º      º|" '\n' "|    º   |" '\n' "|º      º|" '\n' " ¯¯¯¯¯¯¯¯")
        elif dado3 == 6:
            print(" ________" '\n'"|º      º|" '\n' "|º      º|" '\n' "|º      º|" '\n' " ¯¯¯¯¯¯¯¯")


        return dado1,dado2,dado3

    def leer_lanzamiento(a,b,c):
        punt = 0
        if a == 1:
            punt += 1
        elif a == 3:
            punt += 2
        elif a == 5:
            punt += 4
        if b == 1:
            punt += 1
        elif b == 3:
            punt += 2
        elif b == 5:
            punt += 4
        if c == 1:
            punt += 1
        elif c == 3:
            punt += 2
        elif c == 5:
            punt += 4
        return punt

    def bonus(a,b,c):
        bonus = 1
        if (a == 2 and b == 2 and c == 2) or (a == 4 and b == 4 and c == 4) or (a == 6 and b == 6 and c == 6):
            bonus = 2
        return bonus

    def ganador(a,b,c,d,j,k):
        if a > b:

            print("*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$")
            print('El ganador es : ',j)
            print(j, ' ha ganado un monto de',c,'pesos, el casino le corresponde una comision de',d,'pesos')
            print("*$*$*$*$*$*-FIN-*$*$*$*$*$*$*$*$")
        elif a < b:

            print("*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$")
            print('El ganador es',k)
            print(k,'ha ganado un monto de',c,'pesos, el casino le corresponde una comision de',d,'pesos')
            print("*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$*$")
            print("*$*$*$*$*$*-FIN-*$*$*$*$*$*$*$*$")
        else:
            print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
            print('No hay ganador... Es un empate')
            print('Cada jugador se llevara su apuesta y el casino no obtendra comision')
            print("*$*$*$*$*$*-FIN-*$*$*$*$*$*$*$*$")

    def monto_comision():
        montoj1 = int(input('Ingresar apuesta del jugador 1►'))
        montoj2 = int(input('Ingresar apuesta del jugador 2►'))
        montototal = montoj1+montoj2
        if montototal < 2000:
            comision = montototal*15/100
            montoganado = montototal -comision
        else:
            comision = montototal*15/100
            montoganado = montototal -comision
        return montoganado,comision

    def j1():

        puntj1 = 0
        multiplicador = 1
        print('\nTurno de JUGADOR 1')
        print('Usted dispondra de 4 lanzamientos...')
        for i in range(0,4):
            input('Presione enter para lanzar...')
            d1,d2,d3 = lanzamientos()
            puntj1 += leer_lanzamiento(d1,d2,d3)
            multiplicador = bonus(d1,d2,d3)
            print('Puntaje actual:',puntj1)
        puntj1 *= multiplicador
        print('Puntaje total:',puntj1)
        return puntj1

    def j2():
        puntj2 = 0
        multiplicador = 1
        print('\nTurno de JUGADOR 2')
        print('Usted dispondra de 4 lanzamientos...')
        for i in range(0,4):
            input('Presione enter para lanzar...')
            d1,d2,d3 = lanzamientos()
            puntj2 += leer_lanzamiento(d1,d2,d3)
            multiplicador = bonus(d1,d2,d3)
            print('Puntaje actual:',puntj2)
        puntj2 *= multiplicador
        print('Puntaje total:',puntj2,'\n')
        return puntj2

    def jugadoresstring():
        juga1 = input("Ingrese el nombre del jugador 1 ►")
        juga2 = input("Ingrese el nombre del jugador 2 ►")

        return juga1,juga2

    def play():
        print('••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••')
        print('•••••••••••••••Bienvenido al juego del punto••••••••••••••••')
        print('••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••')
        print('••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••')
        print('••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••')
        print('\n ░░░▒▒▒▓▓▓▓░░░▒▒▒▓▓▓▓░░░▒▒▒')

        juga1, juga2 = jugadoresstring()
        print('\n ░░░▒▒▒▓▓▓▓░░░▒▒▒▓▓▓▓░░░▒▒▒')
        monto,comision = monto_comision()
        pj1 = j1()
        pj2 = j2()
        print('\n ░░░▒▒▒▓▓▓▓░░░▒▒▒▓▓▓▓░░░▒▒▒')
        ganador(pj1,pj2,monto,comision,juga1,juga2)

    play()

def juego_craps():
    def apuestas():
        apass = int(input('Apuesta PASS►'))
        anopass = int(input('Auesta NO PASS►'))
        afield = int(input('Apuesta FIELD►'))
        ndobles = 1
        while not(ndobles == 4 or ndobles == 6 or ndobles == 8 or ndobles == 10):
            ndobles = int(input('Apuesta DOBLES, ingrese un numero(4,6,8,10)►'))
            if not(ndobles == 4 or ndobles == 6 or ndobles == 8 or ndobles == 10):
                print('Numero no valido... por favor ingrese un numero valido...')
        adobles = int(input('Apuesta DOBLES►'))
        if ndobles == 4 or ndobles == 10:
            adobles *= 7
        else:
            adobles *= 9
        return apass,anopass,afield,ndobles,adobles

    def lanzamiento2d():
        stringdadoc1 = "nada"
        stringdadoc2 = "nada"
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)




        if d1 == 1:
            stringdadoc1 = " ________" '\n'"|        |" '\n' "|    º   |" '\n' "|        |" '\n' " ¯¯¯¯¯¯¯¯"
        elif d1 == 2:
            stringdadoc1 = " ________" '\n'"|       º|" '\n' "|        |" '\n' "|º       |" '\n' " ¯¯¯¯¯¯¯¯"
        elif d1 == 3:
            stringdadoc1 = " ________" '\n'"|       º|" '\n' "|    º   |" '\n' "|º       |" '\n' " ¯¯¯¯¯¯¯¯"
        elif d1 == 4:
            stringdadoc1 = " ________" '\n'"|º      º|" '\n' "|        |" '\n' "|º      º|" '\n' " ¯¯¯¯¯¯¯¯"
        elif d1 == 5:
            stringdadoc1 = " ________" '\n'"|º      º|" '\n' "|    º   |" '\n' "|º      º|" '\n' " ¯¯¯¯¯¯¯¯"
        elif d1 == 6:
            stringdadoc1 = " ________" '\n'"|º      º|" '\n' "|º      º|" '\n' "|º      º|" '\n' " ¯¯¯¯¯¯¯¯"

        if d2 == 1:
            stringdadoc2 = " ________" '\n'"|        |" '\n' "|    º   |" '\n' "|        |" '\n' " ¯¯¯¯¯¯¯¯"
        elif d2 == 2:
            stringdadoc2 = " ________" '\n'"|       º|" '\n' "|        |" '\n' "|º       |" '\n' " ¯¯¯¯¯¯¯¯"
        elif d2 == 3:
            stringdadoc2 = " ________" '\n'"|       º|" '\n' "|    º   |" '\n' "|º       |" '\n' " ¯¯¯¯¯¯¯¯"
        elif d2 == 4:
            stringdadoc2 = " ________" '\n'"|º      º|" '\n' "|        |" '\n' "|º      º|" '\n' " ¯¯¯¯¯¯¯¯"
        elif d2 == 5:
            stringdadoc2 = " ________" '\n'"|º      º|" '\n' "|    º   |" '\n' "|º      º|" '\n' " ¯¯¯¯¯¯¯¯"
        elif d2 == 6:
            stringdadoc2 = " ________" '\n'"|º      º|" '\n' "|º      º|" '\n' "|º      º|" '\n' " ¯¯¯¯¯¯¯¯"

        print(stringdadoc1)
        print(stringdadoc2)
        return d1,d2

    def ganancias(a,b,c,d,e,f):
        montog = 0
        if a == 7 or a == 11:
            print('GANASTE!!!!!!!')
            print('Ganaste la apuesta PASS, que es un monto de',b,'$')
            montog += b
        elif a == 2 or a == 3 or a == 12:
            print('Usted ha perdido...')
            print('ganaste la apuesta NO PASS, que es un monto de',c,'$')
            montog += c
        else:
            punto = a
            print('Segunda etapa, buscando el ['+str(punto)+']')
            puntn = 0
            while punto != puntn:
                input('Presione enter para un nuevo lanzamiento...')
                d1,d2 = lanzamiento2d()
                puntn = d1+d2
                if puntn == punto:
                    print('Ganaste!!...')
                    print('Ganaste la apuesta PASS, equivalente a un monto de',b,'$')
                    montog += b
                    break
                elif puntn == 7:
                    print('Perdiste !!')
                    print('Ganaste la apuesta NO PASS, equivalente a un monto',c,'$')
                    montog += c
                    break
                else:
                    if puntn == 2 or puntn == 12:
                        print('Ha ganado la apuesta FIELD:',d*2)
                        montog += d*2
                    elif puntn == 3 or puntn == 4 or puntn == 9 or puntn == 10 or puntn == 11:
                        print('Ha ganado la apuesta FIELD',d)
                        montog += d
                    if puntn == e:
                        print('Usted ha ganado la apuesta DOBLES:',f)
                        montog += f
        print('Ha ganado un total de',montog,'$')

    def play():
        print('『』『』『』『』『』『』『』『』『』『』『』『』『』『』『』『』『』『』『』')
        print('『』『』Bienvenido al juego del  ʗ Ɍ д Ᵽ ₴ 『』『』『』『』『』『』『』')
        print('『』『』『』『』『』『』『』『』『』『』『』『』『』『』『』『』『』『』『』')
        apass, anopass, afield, ndobles, adobles = apuestas()
        input('Presione enter para su primer lanzamiento...')
        d1,d2 = lanzamiento2d()
        puntos = d1+d2
        ganancias(puntos, apass, anopass,afield,ndobles,adobles)

    play()

def menu():
    opc = 1
    while opc != 3:
        print('░░░▒▒▒▓▓▓▓░░░▒▒▒▓▓▓▓░░░▒▒▒')
        print('ϟϟϟϟϟϟϟϟϟϟϟϟϟBienvenido al Menúϟϟϟϟϟϟϟϟϟϟϟϟϟ')
        print('░░░▒▒▒▓▓▓▓░░░▒▒▒▓▓▓▓░░░▒▒▒')
        print('\n[1] ingresar al Juego del [P U Ν T ʘ]')
        print('[2] jugar al  ʗ Ɍ д Ᵽ ₴ ---→Nuevo!!☺')
        print('[3]  ←-EXIT ')
        print('\n ░░░▒▒▒▓▓▓▓░░░▒▒▒▓▓▓▓░░░▒▒▒')
        opc = int(input('Seleccione una opcion ► '))


        if opc == 1:
            juego_punto()
        elif opc == 2:
            juego_craps()
        elif opc == 3:
            print('Gracias por utilizar este programa...')
        else:
            print('Por favor introduzca una opcion correcta...')

menu()
