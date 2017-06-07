import random,time

def muestraIntro():
    print("""Estas en un planeta lleno de Dragones. En frente tuyo
    hay dos cuevas. En una de ellas, el Dragon es bueno y compartira
    su tesoro contigo. El otro Dragon esta hambriento y te devorará
    en cuanto te vea.
    
    """)

def eligeCueva():
    cueva=""
    while cueva!="1" and cueva!="2":
        print("¿A qué cueva quieres ir? (1 o 2)")
        cueva = str(input("Elijo la cueva número...  "))
    return cueva

def mirarCueva(queCueva):
    print("Te aproximas a la cueva... ")
    time.sleep(2)
    print("Esta oscuro y misterioso... ")
    time.sleep(2)
    print("""¡Un gran Dragón aparece delante tuyo! Abre sus fauces y...
    
     """)
    time.sleep(2)
    cuevaSalvadora=random.randint(1,2)
    if queCueva==str(cuevaSalvadora):
        print("... ¡Te da su tesoro!")
    else:
        print("¡Te devora de un solo bocado!")

jugarOtraVez = "s"

while jugarOtraVez == "s" or jugarOtraVez == "S" or jugarOtraVez == "Si" or jugarOtraVez == "SI":
    muestraIntro()
    numeroCueva = eligeCueva()
    mirarCueva(numeroCueva)
    print("¿Quieres jugar otra vez? (S / N)" )
    jugarOtraVez = input()
