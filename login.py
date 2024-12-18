import os
def signUp (mainDict):
    os.system("clear")
    userName =  input("Por favor, ingrese su nombre de usuario") 
    password = input("por favor, ingrese su contraseña")
    userID = len(mainDict) +1
    permissionSwitch = True
    if(len(mainDict)>0):     #Validación para que dos personas no puedan tener el mismo nombre de usuario
        for k,v in mainDict.items():
            for l,b in v.items():
                if(l=='userName'):
                    if(b==userName):
                        permissionSwitch=False


    if(permissionSwitch==True): # Constructor para la creación de usuarios junto a sus tableros
        mainDict.update({
            str(userID): {
                'userName':userName,
                'passWord':password,
                'boards': {}
            }})
        input("El usuario ha sido creado con éxito.")
    else:
        input("No se pudo crear su cuenta. Ya existe otro usuario con ese nombre")

    
    


def logIn(mainDict):
    os.system("clear")
    userName= input("Por favor, ingrese su nombre de usuario para loggearse: ")
    passWord= input("Por favor, ingrese su contraseña: ")
    userID = ''
    if (len(mainDict)>0):  #Localizar el diccionario del usuario dentro del diccionario principal
        for k,v in mainDict.items():
            for l,b in v.items():
                if(l=='userName'):
                    if(b==userName):
                        userID = k
                        if(passWord== mainDict.get(userID).get('passWord')):
                            return userID
                        else:
                            return False
    
    
    
                        
