import login as log
import jsonModule as j
import os


def loginMenu(mainDict):
    os.system("clear")
    optionChosen = int(input("""Bienvenido al sistema de gestión Campustasks. Por favor, escoja alguna de las siguientes opciones:
                             1.Crear un usuario.
                             2.Iniciar sesión como usuario.
                             3.Salir
                             """))
    match optionChosen:
        case 1:
            os.system('clear')
            log.signUp(mainDict)
            j.addData(mainDict)
            loginMenu(mainDict)
        case 2:
            os.system('clear') 
            loginReturn =log.logIn(mainDict)
            if (type(loginReturn)== str):
                input("el Usuario pudo ser validado. Presione enter para continuar.")
                featureMenu(mainDict, loginReturn)
            else:
                input("El usuario no pudo ser validado. Será devuelto al menú principal. Presione enter para volver al menú principal.")
                loginMenu(mainDict)
        case 3:
            os.system('clear')

        case _:
            os.system("clear")
            input("La opción elegida no es válida. Será regresado al menú principal")
            loginMenu(mainDict)


def featureMenu(mainDict, userID): #Completar con un match case las opcionesd el menú de opciones.
    os.system("clear")
    optionChosen = int(input("""
        Por favor, elija una de las siguientes opciones:
              1.Gestionar tablero
              2.Gestionar lista
              3.Gestionar tarjeta
              4. Cerrar sesión
    """))

    match optionChosen:
        case 1:
            boardMenu(mainDict,userID)
        case 2: 
            listMenu(mainDict, userID)
        case 3:
            cardMenu(mainDict, userID)
        case 4:
            loginMenu(mainDict)
        case _:
            input("el contenido digitado no coincide con ninguna opción del sistema. Oprima enter para ver el menú de nuevo.")
            boardMenu(mainDict, userID)

def boardMenu(mainDict,userID):
    os.system("clear")
    optionChosen= int(input("""
    Por favor, elija la opción de gestión para su tablero:
        1.Crear un nuevo tablero.
        2. Ver todos los tableros.
        3.Actualizar el nombre de un tablero.
        4. Eliminar un tablero.
        5. Volver al menú anterior
    """))

    match optionChosen:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            featureMenu(mainDict,userID)
        case _:
            input("el contenido digitado no coincide con ninguna opción del sistema. Oprima enter para ver el menú de nuevo.")
            boardMenu(mainDict, userID)

def listMenu(mainDict, userID):
    os.system("clear")
    optionChosen = int(input("""
        Por favor, escoja la opción de gestión para su lista:
        1.Crear una lista dentro de un tablero.
        2.Ver todas las listas de un tablero.
        3.Actualizar el nombre de una lista.
        4.Eliminar una lista.
        5. Volver al menú anterior.
    """))
    
    match optionChosen:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            featureMenu(mainDict,userID)
        case _:
            input("el contenido digitado no coincide con ninguna opción del sistema. Oprima enter para ver el menú de nuevo.")
            listMenu(mainDict, userID)

def cardMenu(mainDict, userID):
    os.system("clear")
    optionChosen = int(input("""
        Por favor, escoja la opción de gestión para su tarjeta:
        1.Crear una tarjeta dentro de una lista.
        2.Ver todas las tarjetas dentro de una lista.
        3.Actualizar  una tarjeta (Título, descripción, estado)
        4. Eliminar una tarjeta.
        5. Volver al menú anterior.
    """))
    match optionChosen: 
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            featureMenu(mainDict, userID)
        case _:
            input("el contenido digitado no coincide con ninguna opción del sistema. Oprima enter para ver el menú de nuevo.")
            cardMenu(mainDict, userID)            




    



    
