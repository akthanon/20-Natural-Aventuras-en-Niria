import time
import random
import os

class Enemigo:
    def __init__(self, nombre, vida, ataques, velocidad):
        self.nombre = nombre
        self.vida = vida
        self.ataques = ataques
        self.velocidad = velocidad

    def atacar(self):
        ataque = random.choice(self.ataques)
        return f"{self.nombre} usa {ataque} para atacar."

    def recibir_danio(self, danio):
        self.vida -= danio
        if self.vida <= 0:
            return f"{self.nombre} ha sido derrotado."
        else:
            return f"{self.nombre} ha recibido {danio} de daño y tiene {self.vida} puntos de vida restantes."

    def escapar(self):
        chance = random.random()
        if chance < self.velocidad:
            return f"{self.nombre} ha escapado con éxito."
        else:
            return f"{self.nombre} no pudo escapar y sigue en la batalla."

    def usar_item(self, item):
        return f"{self.nombre} usa el item {item}."

# Enemigos
enemigo_orco = Enemigo("Orco", 100, ["Golpe fuerte", "Gruñido aterrador", "Ataque feroz"], 0.3)


def funcion_combate(enemigo):
    print("\nInicia un combate con: "+enemigo.nombre)
    time.sleep(1)
    print("Ganaste el combate.")
    time.sleep(1)

def dexto(texto,timp):
    for i in range(len(texto)):
        print(str(texto[i]),end="")
        time.sleep(timp)
    print("")
    
def iniciar_aventura():
    global x
    global y
    global terminar
    global mostrar_zona
    global zonas
    global coordenadas
    os.system('cls')
    print("¡Bienvenido a la Aventura titulada: 20 Natural, Aventuras en Niria!")
    time.sleep(1)
    print("Estás en un bosque misterioso de Kanta. No tienes idea de cómo llegaste aquí.")
    time.sleep(1)
    print("Frente a ti, ves cuatro caminos. ¿Cuál eliges?")
    time.sleep(1)
    input("\nContinuar...")
    os.system('cls')
    while terminar==False:
        mostrar_mapa()
        print("\n***Opciones***")
        print("1. Ir al Norte.")
        print("2. Ir al Sur.")
        print("3. Ir al Este.")
        print("4. Ir al Oeste.")
        print("5. Explorar.")
        print("6. Información.")
        eleccion = input("Elige una opción: ")
        os.system('cls')
        xtemp=x
        ytemp=y
        
        if eleccion == "1":
            y=y-1
        elif eleccion == "2":
            y=y+1
        elif eleccion == "3":
            x=x+1
        elif eleccion == "4":
            x=x-1
        elif eleccion=="5":
            mostrar_zona=True
        elif eleccion=="6":
            mostrar_inventario()
        else:
            print("Opción no válida. Elige una opción válida.")


        avanzado=False
        indis=0
        for funcion in zonas:
            cordis=coordenadas[indis]
            cx=cordis[0]
            cy=cordis[1]
            if x==cx and y==cy:
                funcion()
                input("\nContinuar...")
                os.system('cls')
                avanzado=True
            indis=indis+1
        if avanzado==False:
            print("No hay camino en esa dirección. Elige Otro camino.")
            x=xtemp
            y=ytemp
        mostrar_zona=False    
    print("HAZ MUERTO!!! O__o")
    time.sleep(5)
    os.system('cls')

def mostrar_mapa():
    global coordenadas
    global x
    global y
    print("\n****Mapa****\n")
    max_x = max(coordenada[0] for coordenada in coordenadas)
    max_y = max(coordenada[1] for coordenada in coordenadas)
    min_x = min(coordenada[0] for coordenada in coordenadas)
    min_y = min(coordenada[1] for coordenada in coordenadas)

    # Crea una cuadrícula de asteriscos
    grid = [[' * ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Marca las coordenadas con 'X' en la cuadrícula
    con=0
    actual_indice=coordenadas.index([x,y])
    for ux, uy in coordenadas:
        if con==actual_indice:
            grid[uy][ux] = ' O '
        else:
            grid[uy][ux] = ' X '
        con=con+1

    # Imprime la cuadrícula en pantalla
    for fila in grid:
        print(''.join(fila))
    
    
def mostrar_inventario():

    print("\n****Inventario****\n")
    if len(inventario) == 0:
        print("*inventario vacio.")
    else:
        for item in inventario:
            print(f"- {item}")
    print("\ntienes "+str(dinero)+"$ murciemonedas")
    print("\n****Descripción****")
    


def camino_norte():
    global dinero
    global terminar
    if mostrar_zona==False:
        print("\nVisualisas un sendero.")
        time.sleep(1)
    if mostrar_zona==True:
        print("Caminas por un sendero estrecho y encuentras un cofre escondido.")
        time.sleep(1)
        print("¿Qué haces?")
        time.sleep(1)
        while True:
            print("\nOpciones:")
            print("1. Abrir el cofre.")
            print("2. Ignorar el cofre y seguir adelante.")
            eleccion = input("Elige una opción (1/2): ")
            releccion=random.randint(1,4)
            
            if eleccion == "1":
                if releccion == 1:              
                    print("\nDentro del cofre encuentras una gema preciosa con un valor de 500 murciemonedas. ¡Has tenido suerte!")
                    inventario.append("Gema")
                    dinero=dinero+500
                if releccion == 2:              
                    print("\nDentro del cofre encuentras una chanwich. ¡al menos no te moriras de hambre!")
                    inventario.append("Chanwich")
                if releccion == 3:              
                    print("\nEra un cofre trampa. ¡Te comió!")
                    inventario.append("Cabeza")
                    terminar=True
                if releccion == 4:              
                    print("\nDentro del cofre encuentras 1000 murciemonedas. ¡eres murciemillonario!")
                    inventario.append("Bolsa con dinero")
                    dinero=dinero+1000
                break
            elif eleccion == "2":
                print("\nDecides seguir adelante sin abrir el cofre.")
                break
            else:
                print("Opción no válida. Elige una opción válida (1/2).")
        if terminar==False:
            print("Sigues avanzando y te encuentras con un leñador que te ofrece comida y refugio para la noche. Aceptas su amable oferta y descansas.")
            time.sleep(1)
            print("A la mañana siguiente, el leñador te da un mapa que te muestra el camino de regreso a casa.")
            time.sleep(1)
            print("¡Has completado la primera parte de la aventura!")
            mostrar_inventario()

def camino_sur():
    global llave_oeste
    if mostrar_zona==False:
        print("\nVes un gran rio a lo lejos.")
        time.sleep(1)
    if mostrar_zona==True:
        print("Sigues el camino y llegas al río.")
        time.sleep(1)
        print("¿Qué haces?")
        time.sleep(1)
        
        while True:
            print("\nOpciones:")
            print("1. Intentar cruzar el río a nado.")
            print("2. Buscar un puente cercano.")
            eleccion = input("Elige una opción (1/2): ")
            
            if eleccion == "1":
                print("\nIntentas cruzar el río a nado, pero la corriente es demasiado fuerte y te arrastra. Game over.")
                break
            elif eleccion == "2":
                print("\nEncuentras un puente cercano y cruzas el río con seguridad.")
                break
            else:
                print("Opción no válida. Elige una opción válida (1/2).")

        print("Del otro lado del río, encuentras una cueva misteriosa. ¿Deseas explorarla?")
        time.sleep(1)
        
        while True:
            print("\nOpciones:")
            print("1. Entrar en la cueva.")
            print("2. Continuar por el camino.")
            eleccion = input("Elige una opción (1/2): ")
            
            if eleccion == "1":
                print("\nDentro de la cueva, encuentras tesoros antiguos y una llave secreta, además decides quedarte un tiempo explorándola.")
                time.sleep(1)
                print("Cuando finalmente sales de la cueva, te das cuenta de que ha pasado mucho tiempo.")
                time.sleep(1)
                print("Decides continuar tu aventura con tesoros en tu mochila.")
                inventario.append("Tesoro antiguo")
                inventario.append("Llave Oeste")
                llave_oeste=True
                break
            elif eleccion == "2":
                print("\nDecides continuar por el camino y no entras en la cueva.")
                break
            else:
                print("Opción no válida. Elige una opción válida (1/2).")

        print("Sigues caminando por el bosque y encuentras una bifurcación. Uno de los caminos parece llevar a un pueblo. ¿Qué haces?")
        time.sleep(1)

        while True:
            print("\nOpciones:")
            print("1. Tomar el camino hacia el pueblo.")
            print("2. Tomar el otro camino.")
            eleccion = input("Elige una opción (1/2): ")
            
            if eleccion == "1":
                print("\nTe diriges hacia el pueblo en busca de ayuda y refugio.")
                time.sleep(1)
                print("La gente del pueblo te da la bienvenida y te ofrece un lugar donde quedarte. Continuarás tu aventura mañana.")
                break
            elif eleccion == "2":
                print("\nOptas por tomar el otro camino, curioso por lo que te deparará.")
                break
            else:
                print("Opción no válida. Elige una opción válida (1/2).")
        

def camino_este():
    if mostrar_zona==False:
        print("\nLlegaste a un camino empinado y a lo lejos visualizas una colina.")
        time.sleep(1)
    if mostrar_zona==True:
        print("Caminas por ese camino y llegas a la colina.")
        time.sleep(1)
        print("Desde la cima de la colina, ves un pueblo en la distancia.")
        time.sleep(1)
        print("¿Qué haces?")
        time.sleep(1)
        
        while True:
            print("\nOpciones:")
            print("1. Descender la colina y dirigirte al pueblo.")
            print("2. Explorar la colina en busca de tesoros ocultos.")
            eleccion = input("Elige una opción (1/2): ")
            
            if eleccion == "1":
                print("\nDeslizas por la colina y te diriges al pueblo en busca de ayuda.")
                time.sleep(1)
                print("La gente del pueblo te da la bienvenida y te ofrece refugio. Continuarás tu aventura mañana.")
                break
            elif eleccion == "2":
                print("\nDecides explorar la colina, pero no encuentras tesoros. Finalmente, te diriges al pueblo.")
                time.sleep(1)
                print("La gente del pueblo te da la bienvenida y te ofrece refugio. Continuarás tu aventura mañana.")
                break
            else:
                print("Opción no válida. Elige una opción válida (1/2).")
    

def camino_oeste():
    global llave_oeste
    if mostrar_zona==False:
        print("\nObservas una cabaña en la zona...")
        time.sleep(1)
    if mostrar_zona==True:
        print("Te acercas a la cabaña donde observas una pueta secreta.")
        time.sleep(1)
        while True:
            print("\nOpciones:")
            print("1. Intentar abrir la puerta.")
            print("2. Tocar la puerta.")
            eleccion = input("Elige una opción (1/2): ")
                
            if eleccion == "1":
                print("\nIntentas abrir la puerta.")
                time.sleep(1)
                if llave_oeste==True:
                    print("Abres la puerta con la llave que tienes en tu inventario y observas que no hay nadie.")
                elif llave_oeste==False:
                    print("Intentas abrir la puerta pero notas que está cerrada con llave.")
                    time.sleep(1)
                    print("No pasa nada.")
                break
            elif eleccion == "2":
                print("\nDecides tocar la puerta.")
                time.sleep(1)
                print("No pasa nada.")
                break
            else:
                print("Opción no válida. Elige una opción válida (1/2).")

def camino_inicio():
    if mostrar_zona==False:
        print("\nTe encuentras en el punto de inicio.")
        time.sleep(1)
    if mostrar_zona==True:
        v_gerundio=gerundio[random.randint(0,len(gerundio))-1]
        animal=animales[random.randint(0,len(animales))-1]
        print("Estás "+v_gerundio+" "+animal)
        time.sleep(1)


def camino_lago():
    if mostrar_zona==False:
        print("\nHaz ido por un camino largo.")
        time.sleep(1)
    if mostrar_zona==True:
        print("Objservas la longitud del camino, es muy largo.")
        time.sleep(1)
def camino_desierto():
    if mostrar_zona==False:
        print("\nHas entrado a un desierto.")
        time.sleep(1)
    if mostrar_zona==True:
        print("Tienes mucho calor.")
        time.sleep(1)    
def camino_piramide():
    if mostrar_zona==False:
        print("\nHaz encontrado una piramide.")
        time.sleep(1)
    if mostrar_zona==True:
        print("La observas.")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("No pasa nada.")
        time.sleep(1)
def camino_vista():
    if mostrar_zona==False:
        print("\nHaz encontrado un camino con una hermosa vista.")
        time.sleep(1)
    if mostrar_zona==True:
        print("La vista es muy hermosa.")
        time.sleep(1)
def camino_santuario():
    if mostrar_zona==False:
        print("\nA lo lejos ves un santuario.")
        time.sleep(1)
    if mostrar_zona==True:
        print("Te quedas mirando el santuario pero decides no entrar.")
        time.sleep(1)

def camino_normal():
    if mostrar_zona==False:
        print("\nUn camino normal.")
        time.sleep(1)
    if mostrar_zona==True:
        print("No hay nada interesante :C.")
        time.sleep(1)
        funcion_combate(enemigo_orco)

       
if __name__ == "__main__":
    while True:

        gerundio= [
        "corrompiendo", "oliendo",
        "moviendo","amordazando","amarrando","mordizqueando",
        "atrayendo", "sacando",
        "aclarando", "venciendo",
        "despertando","extenuando",
        "haciendo","enriqueciendo","pintando",
        "jalando","jalando","besando","observar",
        "filmando","acariciando","llevando a nadar",
        "cocinando", "contrayendo", "perseguiendo", "mordiendo",
        "estacionando", "rompiendo", "partiendo",
        "pintando", "arrancando", "arrojando al foso","yendo a buscar"
        "escuchando","arrastrando","empollando",
        "limpiando", "moviendo", "sintiendo", "dando de comer", "dando apoyo a", "atormentando",
        "combatiendo", "extrangulando","yendo a vender",
        "teniendo", "repartiendo", "asesinando",
        "batiendo", "hechando a la cazuela", "partiendo","venciendo",
        "escogiendo", "recibiendo","acariciando",
        "donando", "excluyendo", "matando","yendo a jalar el cuello a",
        "conteniendo", "hirviendo", "escarbando", "viendo aplaudir",
        "paseando", "comprimiendo", "pelando","sacudiendo", 
        "obedeciendo","sacando a pasear"
        ]

        presente=[]
        pasado=[]
        animales = [
        "el camello", "el lobo", "el topo",
        "la liebre", "la pantera", "la gallina",
        "la tarántula",
        "la oveja", "el cerdo", "la iguana",
        "el búfalo", "el gusano", "el mapache",
        "el alce", "el escorpión", "el elefante",
        "el tlacuache", "el venado", "el oso",
        "la araña", "el rinoceronte", "la mula",
        "el orangután", "la rata", "la chita",
        "el avestruz", "el leopardo", "el gorila",
        "la serpiente", "el ganso", "el ratón",
        "el cocodrilo", "el tigre", "la anaconda",
        "el gallo", "la cucaracha", "el caballo",
        "el pingüino", "la cabra", "el jaguar",
        "la vaca", "la víbora", "el castor",
        "la rana", "el canguro", "el hámster",
        "el conejo", "el asno", "la lagartija",
        "el becerro", "el alacrán", "el mandril",
        "el armadillo", "el caimán", "el oso",
        "el camaleón", "la tortuga",
        "el koala", "la ardilla", "la hormiga",
        "el burro", "la jirafa", "el león",
        "el mono", "el chango", "el toro"
        ]

        # Inventario del jugador
        inventario = []
        zonas = [camino_inicio, camino_norte, camino_sur, camino_este, camino_oeste, camino_lago, camino_desierto, camino_piramide, camino_vista, camino_santuario]
        
        tx=random.randint(100,200)
        ty=random.randint(100,200)
        coordenadas=[[tx,ty]]

        normales=[camino_normal]*random.randint(0,2*len(zonas))

        
        for camino in normales:
            zonas.append(camino)

        
        random.shuffle(zonas)

        inicio_indice=zonas.index(camino_inicio)

        for i in range(len(zonas)-1):
            colocado=False
            newcor=[]
            while colocado==False:
                
                dire=random.randint(0,1)
                if len(coordenadas)>0:
                    ranindice=random.randint(0,len(coordenadas)-1)
                else:
                    ranindice=0
                rancor=coordenadas[ranindice]
                tx=rancor[0]
                ty=rancor[1]
                
                if dire==0:
                    ex=random.randint(-1,1)
                    tx=tx+ex
                elif dire==1:
                    ey=random.randint(-1,1)
                    ty=ty+ey
                newcor=[tx,ty]
                if not(newcor in coordenadas):
                    colocado=True
                    
            coordenadas.append(newcor)

            
        min_x = min(coordenada[0] for coordenada in coordenadas)
        min_y = min(coordenada[1] for coordenada in coordenadas)

        coordenadas_a_restar=[min_x,min_y]
            
        coordenadas = [[nx - coordenadas_a_restar[0], ny - coordenadas_a_restar[1]] for nx, ny in coordenadas]
        
        inicio_cords=coordenadas[inicio_indice]
        x=inicio_cords[0]
        y=inicio_cords[1]
        terminar=False
        dinero=0
        mostrar_zona=False
        #OBJETOS
        llave_oeste=False
        iniciar_aventura()


