import login as log
import jsonModule as j
import menus as m

mainDictionary = {}
j.checkFile()
mainDictionary = j.readFile()


m.loginMenu(mainDictionary)