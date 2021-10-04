import threading
#THREADS = 2

class init():
    contador = 0
    turn = 0
    states = [False, False]


#Algoritmos del primer intento
def primerIntentoT1():
    while True:
        while init.turn != 0:
            pass
        #Seccion critica
        init.contador += 1
            
        init.turn = 1

        print("Soy el {} y contador a: ".format(threading.current_thread().name), init.contador)

def primerIntentoT2():
    while True:
        while init.turn != 1:
            pass
        #Seccion critica
        init.contador += 1
        
        init.turn = 0

        print("Soy el {} y contador a: ".format(threading.current_thread().name), init.contador)
    

#Algoritmos del segundo intento#
def segundoIntentoT1():
    while True:
        while init.states[1]:
            pass
        init.states[0] = True

        #Seccion critica
        init.contador += 1
        
        init.states[0] = False

        print("Soy el {} y contador a: ".format(threading.current_thread().name), init.contador)


def segundoIntentoT2():
    
    while True:
        while init.states[0]:
            pass
        init.states[1] = True
            
        #Seccion critica
        init.contador += 1
        
        init.states[1] = False

        print("Soy el {} y contador a: ".format(threading.current_thread().name), init.contador)
    

#Algoritmos del tercer intento
def tercerIntentoT1():
    while True:
        init.states[0] = True
        while init.states[1]:
            pass
        #Seccion critica
        init.contador += 1
        
        init.states[0] = False

        print("Soy el {} y contador a: ".format(threading.current_thread().name), init.contador)

def tercerIntentoT2():
    while True:
        init.states[1] = True
        while init.states[0]:
            pass
        #Seccion critica
        init.contador += 1
        
        init.states[1] = False

        print("Soy el {} y contador a: ".format(threading.current_thread().name), init.contador)

#Algoritmos del cuarto intento
def cuartoIntentoT1():
    while True:
        init.states[0] = True
        while init.states[1]:
            init.states[0] = False
            init.states[0] = True

        #Seccion critica
        init.contador += 1
        
        init.states[1] = False

        print("Soy el {} y contador a: ".format(threading.current_thread().name), init.contador)

def cuartoIntentoT2():
    while True:
        init.states[1] = True
        while init.states[0]:
            init.states[1] = False
            init.states[1] = True

        #Seccion critica
        init.contador += 1
        
        init.states[0] = False

        print("Soy el {} y contador a: ".format(threading.current_thread().name), init.contador)

#Menu
def main():
    numero = input("Introduce el numero de uno de los 4 intentos que deseas ejecutar: ")
    numero = int(numero)

    if numero == 1:
        #Produce espera infinita si el proceso 1 no entra en seccion critica
        t1 = threading.Thread(target=primerIntentoT1)
        t2 = threading.Thread(target=primerIntentoT2)
        
        t1.start()
        t2.start()
            
    elif numero == 2:
        #No asegura exclusion mutua
        t1 = threading.Thread(target=segundoIntentoT1)
        t2 = threading.Thread(target=segundoIntentoT2)
        
        t1.start()
        t2.start()
        
    elif numero == 3:
        #Produce producir deadlock
        t1 = threading.Thread(target=tercerIntentoT1)
        t2 = threading.Thread(target=tercerIntentoT2)
        
        t1.start()
        t2.start()
    elif numero == 4:
        #No se puede asegurar que la espera estara limitada a un numero de pasos finito (livelock)
        t1 = threading.Thread(target=cuartoIntentoT1)
        t2 = threading.Thread(target=cuartoIntentoT2)
        
        t1.start()
        t2.start()
    else:
        print('Error...')

#Inicializador
if __name__ == "__main__":
    main()
