from Persona import Persona

class Nodo():

    def __init__(self, persona: Persona):
        self.persona: Persona = persona
        self.siguiente: Nodo = None

    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def getDato(self):
        return self.persona