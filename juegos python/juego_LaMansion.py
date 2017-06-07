# -*- coding: utf-8 -*-

import time

# Listas utiles para el juego

verbos = ["ir","coger","abrir","atacar","hablar","beber","comer","saltar","subir","bajar","inventario","examinar"]
objetos = ["llave","espada","copa","vaso","galletas","bombones"]
direcciones = ["norte","sur","este","oeste"]

# Mapa de salidas de cada habitacion, id=3 numeros --> piso,fila,columna

salidas = {}
salidas[(1,1,1)] = ["este"]
salidas[(1,1,2)] = ["oeste","sur"]
salidas[(1,1,3)] = ["sur"]
salidas[(1,2,1)] = ["este"]
salidas[(1,2,2)] = ["oeste","norte","este"]
salidas[(1,2,3)] = ["oeste","norte"]
salidas[(2,1,1)] = ["sur"]
salidas[(2,1,2)] = ["este"]
salidas[(2,1,3)] = ["oeste","norte","sur"]
salidas[(2,2,1)] = ["norte","este"]
salidas[(2,2,2)] = ["este","oeste"]
salidas[(2,2,3)] = ["oeste","norte"]


# Función para describir las salas

def describir(p,f,c):
    # p = piso
    # f = fila
    # c = columna
    sala = (p,f,c)
    print("-----------------------------------------------------------------------------------")
    if sala == (1,1,1):
        print("""La cama está oscura. Hay una cama sin hacer.
        No huele especialmente bien.""")

    elif sala == (1,1,2):
        print("El Hall de la casa es más bien sombrio...")
        if trollVivo:
            print("Se oye crujir algo a lo lejos.")
    elif sala == (1,1,3):
        print("""Una pequeña ventana deja vislumbrar un viejo baul junto a la pared.
        Una cucaracha corre a tus pies.""")
    elif sala == (1,2,1):
        print("Ves una mesa. Sobre ella, algunas galletas y restos liquidos")
    elif sala == (1,2,2):
        print("Una escalera llena de polvo conduce hacia arriba")
        if trollVivo:
            print("En algún lugar, se oyen pasos que se arrastran")
    elif sala == (1,2,3):
        print("En el suelo hay una copa. Las paredes estan desconchadas")
    elif sala == (2,1,1):
        print("En una esquina hay un vaso con líquido en su interior.")
        if trollVivo:
            print("Un sonido potente produce un eco que no alcanzas a entender")
    elif sala == (2,1,2):
        if trollVivo:
            print("""Un troll horrible te observa amenazante y se dirige hacia ti
            Detrás de él puedes observar un cofre""")
        else:
            print("El cadaver de un troll descansa en el suelo junto a un cofre")
    elif sala == (2,1,3):
        print("La habitación esta desierta... ")
        if trollVivo:
            print(" ... pero notas la presencia de algo vivo no lejos de aquí.")
    elif sala == (2,2,1):
        print("Un enorme pozo se abre delante de ti. No parece tener fin")
    elif sala == (2,2,2):
        print("""Estas en el piso superior. No hay casi luz y casi te dan ganas
        de volver a bajar por la escalera y escapar""")
    elif sala == (2,2,3):
        print("""Hay unos bombones en una estantería. Una gotera en algún lugar
        produce un sonido rítmico y desconcertante""")

    print("_____________________________________________________________________________")
    print("Te puedes mover en estas direcciones: ")
    for s in salidas[sala]:
        print(s,)
    print("_____________________________________________________________________________")

# Función introducción al juego

def intro():
    print("""Ante ti está LA MANSION. Te han encargado recuperar una hermosa joya,
    una piedra preciosa de incalculable valor. Sabes que esta custodiada y
    que si no tienes valor e inteligencia no saldrás con vida de ella.
    
    """)
    time.sleep(1)
    print("Respiras hondo, te maldices por no venir armado, y entras... ")
    time.sleep(1)
    print(" ")
    input("Pulsa <intro> para empezar el juego.")

# Función para comer / beber

def comerBeber(v,c):
    # v es el verbo: comer/beber
    # c es lo que se quiere comer/beber

    # Declarar los globales
    global inventario, juegoAcabado, haComido, haBebido

    # Comprobar que tiene lo que quiere comer/beber
    if c not in inventario:
        print("No tienes " + c)
        return

    # Comer
    if v == "comer":
        #...galletas
        if c == "galletas":
            print("Comes las galletas y te sientes bien")
            haComido=True
            # Eliminar del inventario
            inventario.remove(c)
            return

        elif c == "bombones":
            print("¡Horror! Un dolor insoportable te invade... ")
            time.sleep(1)
            print("... y mueres retorciendote como una serpiente.")
            # Activar fin de juego
            juegoAcabado = True
            return

        else:
            print("No puedo comer " + c)
            return

    else:
        if c == "vaso":
            print("Bebes del vaso... agua cristalina. ¡Que bien!")
            haBebido = True
            inventario.remove(c)
            return
        elif c == "copa":
            print("Sientes un mareo momentaneo... ")
            time.sleep(1)
            print("... y mueres fulminantemente")
            juegoAcabado=True
            return
        else:
            print("No puedo beber " + c)
            return

# Función procesar acciones

def procesar(instrucciones):
    # Globales = variables modificables
    global piso, fila, columna, juegoAcabado, inventario, yaDescrito, sinLLave
    global pozoAlSur, bAbierto, tieneEspada, trollActivo, trollVivo
    if instrucciones=="":
        return
    if instrucciones=="ayuda":
        print("Debes usar verbos en infinitivo y, si lo necesitas, un nombre.")
        print("Acciones disponibles:")
        print("_____________________")
        for i in verbos:
            print(i,)
            return
        print("_____________________")
        #separar accion en palabras
        palabras = instrucciones.split()
        verbo = palabras[0]
        if verbo not in verbos:
            print("Perdona, no te entiendo")
            return
        if verbo == "ir":
            if len(palabras)!=2 or palabras[1] not in direcciones:
                print("Perdona, no entiendo a donde quieres ir")
                return
            donde = palabras[1]
            if donde not in salidas[(piso,fila,columna)]:
                print("No puedo ir hacia el " + donde)
                return
            elif donde == "norte":
                if fila == 1:
                    print("¡La puerta era una trampa!")
                    time.sleep(1)
                    print("Al otro lado hay un precipicio y te despeñas por él...")
                    juegoAcabado=True
                    return
                elif (fila,columna) == (2,1) and not pozoAlSur:
                    print("Avanzas sin cuidado y te adelantas sobre el pozo...")
                    time.sleep(1)
                    print("¡Caes a la profundidad y la oscuridad del submundo!")
                    juegoAcabado = True
                    return
                fila -= 1
            elif donde == "sur":
                fila +=1
            elif donde == "este":
                if (fila,columna)==(2,1) and pozoAlSur:
                    print("¡Te has olvidado del pozo!")
                    time.sleep(1)
                    print("¡La sima del pozo te traga sin clemencia... ")
                    juegoAcabado = True
                    return
                columna += 1
            else:
                columna -= 1

            print("Vas hacia el " + donde)
            yaDescrito = False
            return
        if verbo == "saltar":
            if len(palabras) != 2:
                print("No entiendo que tengo que saltar.")
                return
            elQue = palabras[1]

            if elQue != "pozo":
                print("Qué tontería...")
                return
            else:
                if (piso,fila,columna) != (2,2,1):
                    print("No hay ningun pozo que saltar")
                else:
                    print("Saltas el pozo con agilidad...")
                    time.sleep(1)
                    print("... y lo dejas a tus espaldas.")
                    pozoAlSur = not pozoAlSur
            return
        if verbo == "subir":
            if (piso,fila,columna) == (1,2,2):
                print("Subes por la escalera")
                piso += 1
                yaDescrito = False
            else:
                print("No puedo subir")
            return
        if verbo == "bajar":
            if (piso,fila,columna) == (2,2,2):
                print("Bajas por la escalera")
                piso -= 1
                yaDescrito = False

            elif (piso,fila,columna) == (2,2,1):
                print("Desciendes por el pozo...")
                time.sleep(0.5)
                print("Unos ojos brillantes te observan desde el fondo")
                print("¡Algo te agarra y te devora!")
                juegoAcabado = True
            else:
                print("No puedo bajar")
            return
        if verbo == "comer" or verbo == "beber":
            if len(palabras) == 1:
                print("Perdona... ¿el qué?")
                return
            else:
                comerBeber(verbo,palabras[1])
                return

        if verbo == "coger":
            if len(palabras) == 1:
                print("Perdona... ¿coger qué?")
                return
            else:
                objeto = palabras[1]
                if objeto in mapa[(piso,fila,columna)]:
                    inventario.append(objeto)
                    mapa[(piso,fila,columna)].remove(objeto)
                    print("Lleva contigo: " + objeto)
                elif (piso,fila,columna) == (1,2,1) and objeto == "llave" and sinLLave:
                    inventario.append(objeto)
                    sinLLave = False
                    print("Llevas contigo: " + objeto)
                elif (piso,fila,columna) == (1,1,3) and objeto == "espada" and bAbierto:
                    if tieneEspada:
                        print("Ya tienes la espada")
                    else:
                        inventario.append(objeto)
                        tieneEspada=True
                        print("Llevas contigo: " + objeto)
                else:
                    print("No puedo hacer eso")
                return

        if verbo == "abrir":
            if len(palabras) == 1:
                print("Perdona... ¿abrir qué?")
                return
            else:
                objeto = palabras[1]
                if (piso,fila,columna) == (1,1,3) and objeto == "baul":
                    if bAbierto:
                        print("El baul ya esta abierto")
                    else:
                        bAbierto=True
                        print("Has abierto el baul")
                elif (piso,fila,columna) == (2,1,2) and objeto == "cofre":
                    if sinLLave:
                        print("¡No puedes abrir el cofre sin una llave!")
                    else:
                        print("Abres el cofre, lentamente...")
                        time.sleep(1)
                        ganar()
                        juegoAcabado=True
                else:
                    print("No puedo hacer eso")
                return

        if verbo == "examinar":
            if len(palabras) == 1:
                print("Perdona, ¿examinar qué?")
                return
            else:
                objeto = palabras[1]
                if objeto == "mesa" and (piso,fila,columna) == (1,2,1) :
                    print("La mesa parece solida")
                    time.sleep(0.5)
                    print("Miras por debajo... ")
                    time.sleep(0.5)
                    if sinLLave:
                        print("... y ves una llave!")
                    else:
                        print("No hay nada")
                elif objeto == "baul" and (piso,fila,columna) == (1,1,3):
                    if bAbierto:
                        print("Miras dentro del baúl...")
                        time.sleep(0.5)
                        if tieneEspada:
                            print("Esta vacio")
                        else:
                            print("¡Hay una espada!")
                    else:
                        print("El baul parece cerrado...")
                elif objeto == "cofre" and (piso,fila,columna) == (2,1,2):
                    print("Es un cofre de madera regia")
                    time.sleep(0.5)
                    print("Y con una cerradura muy resistente")
                else:
                    print("Para lo que te va a servir")
                return

        if verbo == "inventario":
            if inventario == []:
                print("No llevas nada")
                return
            print("Llevas contigo: ")
            for i in inventario:
                print(i)
            print()
            return
        if verbo == "atacar":
            if len(palabras)==1 or palabras[1]=="troll":
                if not trollVivo:
                    print("Pero... ¡si ya esta muerto!")
                if (piso,fila,columna) == (2,1,2):
                    trollActivo = True
                    if tieneEspada:
                        print("El troll acerca su fétido rostro al tuyo...")
                        time.sleep(1)
                        if haComido:
                            print("¡Y lo decapitas de manera fulminante con tu espada!")
                        else:
                            print("mientras te sientes débil por no haber comido...")
                            time.sleep(0.5)
                            print("y te desmayas mientras el troll te desmiembra")
                            juegoAcabado = True
                            trollActivo = False
                    else:
                        print("Insensato... ¡Deberias haber huido mientras podias")
                else:
                    print("Creo que no estás en el lugar correcto para hacer eso")
            else:
                print("Supongo que estas de broma, ¿no?")
            return

def ganar():
    print("***********************************************")
    print("** ¡El resplandor de las joyas te deslumbra! **")
    print("********** ENHORABUENA, CONSEGUISTE ***********")
    print("************** LA PIEDRA PRECIOSA *************")
    print("***********************************************")

def Jugar():
    while True:
        piso = 1
        fila = 1
        columna = 2

        bAbierto = False
        sinLLave = True
        tieneEspada = False
        haComido = False
        haBebido = False
        pozoAlSur = False
        espadaEnMano = False
        inventario = []
        mapa = {}
        mapa[(1,1,1)]=[]
        mapa[(1,1,2)]=[]
        mapa[(1,1,3)]=[]
        mapa[(1,2,1)]=["galletas"]
        mapa[(1,2,2)]=[]
        mapa[(1,2,3)]=["copa"]
        mapa[(2,1,1)]=["vaso"]
        mapa[(2,1,2)]=[]
        mapa[(2,1,3)]=[]
        mapa[(2,2,1)]=[]
        mapa[(2,2,2)]=[]
        mapa[(2,2,3)]=["bombones"]

        juegoAcabado = False
        yaDescrito = False
        tiempo = 0
        trollVivo = True
        esperaTroll = 0
        trollActivo = False

        intro()
        while True:
            if not yaDescrito:
                describir(piso,fila,columna)
                yaDescrito = True
            orden = input("¿Qué quieres hacer?").lower()
            tiempo += 1
            if (piso,fila,columna) == (2,1,2):
                esperaTroll += 1
            procesar(orden)
            if tiempo>25 and not haBebido and not juegoAcabado:
                print("Estas sediento, no puedes más, deberias haber bebido...")
                time.sleep(1)
                print("Te desmayas...")
                time.sleep(1)
                if trollVivo:
                    print("... Y un trol aprovecha la situación para comerte")
                    print("G A M E     O V E R ")
                else:
                    print("... Y te consumes poco a poco en el suelo, deshidratado")
                    print("G A M E     O V E R ")
                juegoAcabado = True
            if (esperaTroll>2 or trollActivo) and trollVivo:
                print("El troll te ataca...")
                time.sleep(1)
                if tieneEspada:
                    trollActivo = True
                    if not espadaEnMano:
                        print("... y desenvainas la espada y ¡te dispones a lucha!")
                        espadaEnMano = True
                else:
                    print("Desarmado no tienes ninguna posibilidad")
                    time.sleep(0.5)
                    print("Te despedaza y se come tus entrañas con avidez")
                    juegoAcabado = True

            if esperaTroll>3 and trollVivo:
                if not haComido:
                    print("Debil por falta de comida, no ofreces resistencia al troll... ¡Tu eres la comida!")
                    juegoAcabado = True
            if esperaTroll>5 and trollVivo:
                print("Finalmente el troll te hunde el pecho y mueres brutalmente...")
                juegoAcabado = True
            if juegoAcabado:
                break
        print("_____________________________________________________________________")
        continuar = input("¿Quieres volver a jugar? (s/n)").lower().startswith("s")
        if not continuar:
            break
        print("_____________________________________________________________________")
        print()




Jugar()