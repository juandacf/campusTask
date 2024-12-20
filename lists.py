import boards as b
import os
def createList(mainDict, userID):
    controlSwitch=True
    while(controlSwitch==True):
        os.system("clear")
        b.viewBoards(mainDict, userID)
        boardName= str(input("Por favor, ingrese el nombre del tablero al que le quiere agregar una lista: "))
        listName= str(input("Por favor, ingrese el nombre de la lista que quiere agregarle al tablero: "))
        mainDict.get(userID).get("boards").get(boardName).update({listName:{}})
        controlSwitch=bool(input("Si desea añadir otra lista, oprima cualquier letra y enter. Si desea volver al menú de listas, oprima enter."))

def viewList (mainDict, userID):
    b.viewBoards(mainDict, userID)
    boardName = str(input("Por favor, ingrese el nombre del tablero del que quiere ver las listas: "))
    for k,v in mainDict.items(): 
        if(userID==k):
            for u,y in v.items():
                if(u=='boards'):
                    for q,w in y.items():
                        if(q==boardName):
                            contador=1
                            print('Las listas disponibles son:')
                            for e,r in w.items():
                                print(f'{contador}.{e}')
                                contador+=1
                            return boardName
                            

def updateListName(mainDict, userID):
    boardChosen=viewList(mainDict, userID)
    listChosen=str(input("Ingrese el nombre de la lista cuyo nombre desea cambiar: "))
    newname=str(input("ingrese el nuevo nombre para la lista: "))
    backup= mainDict.get(userID).get('boards').get(boardChosen).get(listChosen)
    del mainDict[userID]['boards'][boardChosen][listChosen]
    mainDict.get(userID).get('boards').get(boardChosen).update({newname:backup})
    input("El nombre de la lista ha sido actualizado con éxito. Oprima enter para volver al menú de listas.")


def deleteList(mainDict,userID):
    boardChosen=viewList(mainDict, userID)
    listChosen=str(input("Ingrese el nombre de la lista cuyo nombre desea eliminar: "))
    del mainDict[userID]['boards'][boardChosen][listChosen]
    input("Su lista ha sido eliminada con éxito. ")
