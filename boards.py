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
                    for t,y in b.items():
                        print(f'-{t}')
                        
    
    input("Presione enter para volver al menú de tableros.")

def updateBoardName(mainDict,userId):
    os.system("clear")
    for k,v in mainDict.items():
        if(k==userId):
            for l,b in v.items():
                if(l=='boards'):
                    counter=1
                    for t,y in b.items():
                        print(f'{counter}.{t}')
                        counter=+1