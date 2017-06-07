import random

def adivinanza():
    intentos = 0
    print("Hola, ¿cómo te llamas? :)")
    nombre = str(input())

    numero = random.randint(1,20)
    print("Bueno, " + nombre + ", estoy pensando un número del 1 al 20 ¡Adivinalo!")

    while intentos<6:
        print("Creo que es el...")
        posible = int(input())

        intentos += 1

        if posible < numero:
            print("Mi número es más grande")

        if posible > numero:
            print("Mi número es más pequeño")

        if posible == numero:
            break

    if posible == numero:
        intentos = str(intentos)
        print("¡Enhorabuena " + nombre + "! ¡Has adivinado el número en " + intentos + " intentos!")

    if posible !=numero:
        numero = str(numero)
        print("¡Nooooo, ya no te quedan intentos! El número era el " + numero + ".")



print(adivinanza())