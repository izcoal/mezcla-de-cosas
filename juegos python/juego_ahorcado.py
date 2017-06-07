import random

DIBUJOS = ["""

+---------+
|         |
|         |
          |
          |
          |
          |
          |
============

""",

"""

+---------+
|         |
|         |
O         |
          |
          |
          |
          |
============

""",

"""

+---------+
|         |
|         |
O         |
|         |
|         |
|         |
          |
          |
============

""",

"""

+---------+
|         |
|         |
O         |
|\        |
| \       |
|         |
          |
          |
============

""",

"""

  +----------+
  |          |
  |          |
  O          |
 /|\         |
/ | \        |
  |          | 
             |
             |
================

""",

"""

  +----------+
  |          |
  |          |
  O          |
 /|\         |
/ | \        |
  |          | 
 /           |
/            |
================

""",


"""

  +----------+
  |          |
  |          |
  O          |
 /|\         |
/ | \        |
  |          | 
 / \         |
/   \        |
================

"""]



def palabraAleatoria(listaPalabras):
    cual = random.randint(0,len(listaPalabras)-1)
    ps = input("¿Quieres una pista? (s/n) ")
    if ps in ["s", "S", "si", "Si", "SI", "sI"]:
        print("Pista: Tiene " + str(len(listaPalabras[cual])) + " letras")
    return listaPalabras[cual]


def mostrarAhorcado(DIBUJOS,letrasMalas,letrasBuenas,palabraSecreta):
    print(DIBUJOS[len(letrasMalas)])
    print()
    errores = "Errores: "
    for letra in letrasMalas:
        L = letra + " "
        errores += L
    print(errores)

    huecos = "_" * len(palabraSecreta)

    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] in letrasBuenas:
                huecos = huecos[:i] + palabraSecreta[i]+huecos[i+1:]
    #for letra in huecos:
    #    print(letra)
    print(huecos)

def intento(yaIntentado):

    while True:
        candidata = input("Intenta con una letra...   ")
        candidata = candidata.lower()

        if len(candidata) != 1:
            print("Por favor, introduce solo una letra")
        elif candidata in yaIntentado:
            print("Ya has intentado esa letra. Elige otra")
        elif candidata not in "abcdefghijklmnñopqrstuvwxyz":
            print("Por favor, introduce una LETRA")
        else:
            return candidata


def adivinarPalabra(palabraSecreta):
    prg=str(input("¿Ya sabes que palabra es? (s/n) "))
    if prg in ["s","S","si","Si","SI","sI"]:
        adivinanza=""
        while len(adivinanza)!=len(palabraSecreta):
            try:
                adivinanza = str(input("¿Qué palabra crees que es? "))
            except ValueError:
                "La palabra no tiene esa longitud"

        if adivinanza.lower()!=palabraSecreta:
            print("Lo siento, no es esa palabra. Seguimos jugando")

        return adivinanza.lower()==palabraSecreta
    else:
        print("¡No pasa nada! Seguimos jugando")


def jugarOtraVez():
    return input("¿Quieres jugar otra vez? (s/n) ").lower().startswith("s")

def Juego():
    palabras = "hormiga lomo elefante hipopotamo sarten pierna psicologia neurociencia gaussianidad estadistica hola ola".split()
    print("A H O R C A D O")
    letrasFalladas = ""
    letrasAcertadas = ""
    palabraSecreta = palabraAleatoria(palabras)
    juegoTerminado = False



    while True:
        mostrarAhorcado(DIBUJOS,letrasFalladas,letrasAcertadas,palabraSecreta)


        eleccion = input("¿Quieres elegir una letra o adivinar la palabra? (letra/palabra) ")
        if eleccion.lower() in ["p","pal","pala","palab","palabr","palabra"]:
            adivinada = adivinarPalabra(palabraSecreta)
            if adivinada:
                print("¡Si! ¡La palabra secreta es " + palabraSecreta + "! ¡Has ganado!")
                juegoTerminado = True
        #else:
            #print("Oh, noooooo! ¡No es esa palabra!")
        elif eleccion.lower() in ["l","le","let","letr","letra"]:
            pruebaLetra = intento(letrasAcertadas + letrasFalladas)

        if pruebaLetra in palabraSecreta:
            letrasAcertadas = letrasAcertadas + pruebaLetra

            encontradasTodas = False
            lbool = 0
            for i in range(len(palabraSecreta)):
                lbool += palabraSecreta[i] in letrasAcertadas

                if lbool == len(palabraSecreta):
                    encontradasTodas = True

                #if palabraSecreta[i] not in letrasAcertadas:
                #    encontradasTodas = False
                #    break

                if encontradasTodas:
                    print("¡Si! ¡La palabra secreta es " + palabraSecreta + "! ¡Has ganado!")
                    juegoTerminado = True

        else:
            letrasFalladas = letrasFalladas + pruebaLetra
            if len(letrasFalladas) == len(DIBUJOS)-1:
                mostrarAhorcado(DIBUJOS, letrasFalladas, letrasAcertadas, palabraSecreta)
                print("¡Demasiado intentos! ¡Despues de " + str(len(letrasFalladas)) + \
                    " intentos fallidos y " + str(len(letrasAcertadas)) + \
                    " intentos correctos, la palabra era '" + palabraSecreta +"'")
                juegoTerminado=True

        if juegoTerminado:
            if jugarOtraVez():
                letrasAcertadas=""
                letrasFalladas=""
                juegoTerminado=False
                palabraSecreta=palabraAleatoria(palabras)
            else:
                break


Juego()
#print(adivinarPalabra("potorro"))

"""
Esto es un comentario
"""
