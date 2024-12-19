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
                            for e,r in w.items():
                                print(e)
                                contador+=1