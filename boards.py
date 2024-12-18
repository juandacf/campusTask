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
            
