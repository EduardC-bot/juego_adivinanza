import random

def juego_adivinanza(intentos_maximos):
    numero_secreto = random.randint(1,50)
    intentos = 0
    print("Bienvenido al juego de la adivinanza númerica")
    print(f"Tienes {intentos_maximos}intentos para adivinar el número entre 1 y 50.")

    while intentos < intentos_maximos:
        try:
            intentos_usuario = int(input(f"intento{intentos + 1}:Ingresa tu número: "))
        except ValueError:
            print("Por favor, Ingresa un número valido.")
            continue
    
        intentos += 1

        if intentos_usuario == numero_secreto:
            print("¡Felicidades! Adivinanste el número secreto.")
            break
        elif intentos_usuario > numero_secreto:
            print("El número secreto es menor.")
        else:
            print("El numero secreto es mayor.")

    else: 
        print(f"Se han agotado sus intentos. El número secreto era {numero_secreto}.")

