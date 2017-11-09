from Persona import Persona
from Nodo import Nodo

class ListaSE():

    def __init__(self):
        self.cabeza: Nodo = None

    def adicionarNodo(self, persona: Persona):
        if (self.cabeza != None):
            temp: Nodo = self.cabeza
            while (temp.getSiguiente() != None):
                temp = temp.getSiguiente()
            temp.setSiguiente(Nodo(persona))
        else:
            self.cabeza = Nodo(persona)

    def buscarPersona(self, persona: Persona):
        temp: Nodo = self.cabeza
        while(temp != None):
            if(temp.getDato().__eq__(persona)):
                return temp
            temp = temp.getSiguiente()
        return None

    def getListaPersonas(self):
        temp: Nodo = self.cabeza
        listaResp = []

        if(temp == None):
            return listaResp

        while(temp != None):
            listaResp.append(temp.persona)
            temp = temp.getSiguiente()
        return listaResp