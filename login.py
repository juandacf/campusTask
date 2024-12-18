def signUp (mainDict):
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


    if(permissionSwitch==True):
        mainDict.update({
            str(userID): {
                'userName':userName,
                'passWord':password,
                'boards': {}
            }})
    else:
        input("No se pudo crear su cuenta. Ya existe otro usuario con ese nombre")

    
    


def logIn(mainDict):
    userName= input("Por favor, ingrese su nombre de usuario para loggearse ")