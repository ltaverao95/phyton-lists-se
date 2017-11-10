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
        if (self.head != None):
            temp: Node = self.head
            while (temp.getNext() != None):
                temp = temp.getNext()
            temp.setNext(Node(person))
        else:
            self.head = Node(person)

    def remove(self, person: Person):
        temp: Node = self.head

        if(self.head == None):
            return

        if(temp.person.__eq__(person)):
            temp.setNext(person)
            return

        while(temp.getNext() != None):
            if(temp.getNext().person == person):
                temp.setNext(temp.getNext().getNext())
                print("Node deleted")
                return

            temp = temp.getNext()
        print("Node not found")

    def clear(self):
        self.head = None

    def insert(self, index: Person, object: Person):
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
        else:
            print("Node not found")

    def getPerson(self, person: Person) -> Person:
        temp: Node = self.head
        while(temp != None):
            if(temp.getRecord().__eq__(person)):
                return temp
            temp = temp.getNext()
        return None

    def getPersonsList(self) -> []:
        temp: Node = self.head
        responseList: [] = []

        if(temp == None):
            return responseList

        while(temp != None):
            responseList.append(temp.person)
            temp = temp.getNext()
        return responseList