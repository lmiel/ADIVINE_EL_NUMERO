import random 
numero = random.randint(0, 100) 
encontrado = False

while encontrado == False:

    intento = input("Introduzca numero entre 1 y 99 incluidos: ")
    intento = int(intento)

    if intento < numero:
        print("El numero es demasiado pequeño")
    elif intento > numero:
        print("El numero es demasiado grande")
    else:
        print("¡Has acertado!")
        encontrado = True
