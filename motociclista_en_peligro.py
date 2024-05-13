import random

print("Juego de la Mazmorra\n"
      "--------------------\n"
      "\n"
      "Tu y tu mejor amigo volviendo de una ruta increible en motocicleta (conduciendo cada uno su moto) se despiden\n"
      "para tomar cada uno camino a su casa cuando en plena despedida los alcanza un grupo de motoristas\n"
      "con intenciones de robarles las motos y uno de ellos golpea a tu mejor amigo con una cadena desviandolo\n"
      "del camino, haciendo que colisione contra un arbol y los demas motociclistas del grupo empiezan a\n"
      "encerrarte con sus motos para que frenes y comenzar con el atraco. Pero te das cuenta que delante tuyo tenés\n"
      "dos caminos para desviarte con posibilidades de dejarlos atrás. Cual camino eliges?\n"

      "Por la izquierda camino complicado lleno de piedras y baches; por la derecha un camino que te lleva a un\n"
      "autocine con un parking gigante lleno de vehiculos.\n")

camino = input("Elije: Derecha, camino complicado (A) o izquierda, autocine (B)")

if camino == "A": #camino complicado
    camino = input("Reduces la velocidad para no perder agarre en el camino y comerte un bache (A) o aceleras\n"
                   "a tope con intencion de perder de vista a la banda motorista (B)")

    if camino == "A": #reduce la velocidad
            print("No te caes pero te alcanza la banda motorista, te atraca y te deja desnudo atado a un arbol.\nFIN")
            exit()

    elif camino == "B": #acelera a tope
            print("Al acelerar y avanzar rapido pierdes de vista a la banda pero la motocicleta pierde\n"
                  "agarre y pasas por arriba de un bache tan fuerte que te pincha la rueda trasera con la\n"
                  "consecuencia de que tienes que bajarte la moto, esconderla y esconderte (A) o continuar con\n"
                  "la rueda pinchada arriesgandote a la muerte (B), que decides?")

            camino = input("Opcion (A) Esconderse, opcion (B) Continuar")

            if camino == "A": #esconderse
                    print("Escondes la moto entre unos arbustos, apagas el motor y te quedas unos cuantos minutos\n"
                      "esperando que la banda pase de largo y asi consigues volver a casa.")

            elif camino == "B": #continua con la rueda pinchada
                    print("Continuas a fuego, la moto derrapa perdiendo el control hacia un risco y caes al vacio\nFIN")
                    exit()

elif camino == "B": #autocine
    print("Entras al autocine y te vas detras de un camion a relajar un poco, te das cuenta que\n"
                   "hay una llave inglesa olvidada al lado de la rueda del camión la cual podria ser util pero\n"
                   "a su vez muy pesada y puede retrasarte.")

    camino = input("Opcion (A) la coges, opcion (B) no la coges?")

    llave_inglesa = False

    if camino == "A": #coge la llave inglesa
        print("Coges la llave inglesa")
        llave_inglesa = True

    elif camino == "B": #no coge la llave inglesa
        print("No coges la llave inglesa")

    else: #no elige nada
        print("No has elegido ninguna opcion, estas frito\nFIN")
        exit()

    camionero = random.randint(1, 100)

    print("Estas terminando de relajar para irte a casa y aparece el camionero dueño del camion de donde robaste la llave\n"
      "y te pregunta, ¿que haces husmeando por aqui? tengo ganas de jugar contigo por cotilla, respondeme esto\n"
      f"o estas muerto: ¿cuanto es 10 * {camionero}?")

    camino = int(input("¿Cual es el resultado?"))
    if camino == 10 * camionero: #acierta el numero
        print("El camionero te corta el cuello, odia a los matematicos\nFIN")
        exit()

    else: #no acierta
        print("Por ser tonto le caes bien al camionero y te abre paso a un camino oculto del autocine en el cual\n"
        "te encuentras un bar lleno de borrachos un poco violentos que van a buscarte para darte una paliza\n"
        "como lo resuelves?")

        camino = input("Opcion (A) esperas que algun cinefilo del autocine te ayuda\n"
                       "Opcion (B) intentas salir de esta.")

        if camino == "A": #espera ayuda
            print("todos los cinefilos estaban demasiados ocupados para darse cuenta, estas muerto.\nFIN")
            exit()

        elif camino == "B" and llave_inglesa == True: #se defiende y tiene la llave
            print("Usas la llave inglesa que cogiste anteriormente, y les das una paliza\n"
                  "a esos borrachos sin reflejos. FELICIDADES! VUELVES A CASA")
            exit()

        elif camino == "B" and llave_inglesa == False: #se defiende y no tiene la llave
            print("Intentas escaparte de ahi, si solo tuvieras algo para golpearlos...  Se te vienen encima y te dan\n"
            "hostias de todos lados, te dejan desangrandote en el suelo y es tu final.\nFIN")
            exit()
        else: #no elige ninguna opcion
            print("No elegiste ninguna opcion, estas muerto\n")
            exit()
