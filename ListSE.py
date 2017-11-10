from Person import Person
from Node import Node

class ListSE():

    def __init__(self):
        self.head: Node = None

    def __len__(self):
        length: int = 0
        if(self.isEmpty()):
            return length

        temp: Node = self.head
        while(temp != None):
            length += 1
            temp = temp.getNext()
        return length

    def isEmpty(self) -> bool:
        if(self.head == None):
            return True
        return False

    def append(self, person: Person):

        if(self.head == None):
            self.head = Node(person)
            return

        temp: Node = self.head
        while (temp.getNext() != None):
            temp = temp.getNext()
        temp.setNext(Node(person))

    def remove(self, person: Person):

        if(self.head == None):
            return

        temp: Node = self.head

        if(temp.person.__eq__(person)):
            self.head = temp.getNext()
            return

        while(temp.getNext() != None):
            if(temp.getNext().person.__eq__(person)):
                temp.setNext(temp.getNext().getNext())
                return

            temp = temp.getNext()

    def clear(self):
        self.head = None

    def insert(self, index: Person, object: Person):

        if(index is None or object is None):
            return

        newPerson: Node = Node(object)
        temp: Node = self.head
        if(temp == None):
            self.head = Node(index)
            return
        while((temp.getRecord() != index) and temp.haveNext()):
            temp = temp.getNext()
        if(temp.getRecord().__eq__(index)):
            newPerson.setNext(temp.getNext())
            temp.setNext(newPerson)

    def getPerson(self, person: Person) -> Person:

        if(self.head == None):
            return None

        temp: Node = self.head
        while(temp != None):
            if(temp.getRecord().__eq__(person)):
                return temp.person
            temp = temp.getNext()
        return None

    def getPersonsList(self) -> []:

        responseList: [] = []

        if(self.head == None):
            return responseList

        temp: Node = self.head

        while(temp != None):
            responseList.append(temp.person)
            temp = temp.getNext()
        return responseList