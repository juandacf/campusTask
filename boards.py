import os

def addBoard(mainDict, userID):
    os.system("clear")
    controlSwitch = True
    while(controlSwitch==True):
        boardName = str(input("Por favor, escoja el nombre de su tablero."))
        for k,v in mainDict.items():
            if(k==userID):
                mainDict.get(userID).get('boards').update({boardName: {}})
                controlSwitch = bool(input("El tablero fue añadido con éxito. Si desea añadir otro, oprima cualquier letra. Si quiere volver al menú de tableros, oprima enter."))
            

def viewBoards(mainDict,userId):
    os.system("clear")
    print("Los tableros actualmente disponibles son: ")
    for k,v in mainDict.items():
        if(k==userId):
            for l,b in v.items():
                if(l=='boards'):
                    counter=1
                    for t,y in b.items():
                        print(f'{counter}.{t}')
                        counter+=1

def updateBoardName(mainDict,userId):
    os.system("clear")
    viewBoards(mainDict,userId)
    boardChosen=str(input("Por favor, ingrese el nombre del tablero que desea modificar (sin su número de índice): "))
    newName= str(input("Por favor, ingrese el nuevo nombre para el tablero: "))
    backup= mainDict.get(userId).get("boards").get(boardChosen)
    del mainDict[userId]["boards"][boardChosen]
    mainDict.get(userId).get("boards").update({newName:backup})

def deleteBoard(mainDict,userID):
    os.system("clear")
    viewBoards(mainDict,userID)
    boardChosen=str(input("Por favor, ingrese el nombre del tablero que desea eliminar (sin su número de índice): "))
    del mainDict[userID]["boards"][boardChosen]
    input("El nombre ha sido borrado con éxito. Cuando presione enter, será regresado al menú de tableros.")
    
