import json

class Persona():

    def __init__(self, nombre, edad, genero, telefono, correo):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.telefono=telefono
        self.correo=correo

    def __eq__(self, other):
        return self.__dict__ == other.__dict__