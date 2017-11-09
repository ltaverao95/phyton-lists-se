from ListaSE import ListaSE
from Persona import Persona

listaSE: ListaSE = ListaSE()

listaSE.adicionarNodo(Persona("pepito", 27, "m", 34870, "sf"))
listaSE.adicionarNodo(Persona("pepito2", 27, "m", 34870, "sf"))
listaSE.adicionarNodo(Persona("pepito3", 27, "m", 34870, "sf"))
listaSE.adicionarNodo(Persona("pepito4", 27, "m", 34870, "sf"))

print(listaSE.buscarPersona(Persona("pepito4", 27, "m", 34870, "sf")).persona.__dict__)
print("\n")

listaPersonas = listaSE.getListaPersonas()
if(listaPersonas.__len__() > 0):
    for persona in listaPersonas:
        print(persona.__dict__)
