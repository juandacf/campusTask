import os
import lists as l

def addCard(mainDict, userID):
    controlSwitch=True
    while(controlSwitch==True):
        boardName=l.viewList(mainDict, userID)
        listName= str(input("Por favor, ingrese el nombre de la lista a la cual desea añadirle la tarjeta: "))
        cardName= str(input("Por favor, ingrese el nombre de la tarjeta a agregar: "))
        title=str(input("Por favor, ingrese el título de la tarjeta: "))
        description=str(input("Por favor, ingrese la descripción de la tarjeta: "))
        state=str(input("Por favor, ingrese el estado de la tarjeta: "))
        mainDict.get(userID).get("boards").get(boardName).get(listName).update({cardName:{
            "titulo":title,
            "descripcion":description,
            "estado": state
        }})
        controlSwitch=bool(input("La tarjeta fue creada exitosamente. Si desea añadir otra, ingrese cualquier caracter y oprima enter. Si desea volver al menú, oprima enter: "))

    

    