from Person import Person

class Node():

    def __init__(self, person: Person):
        self.person: Person = person
        self.next: Node = None

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

    def haveNext(self):
        return self.next != None

    def setRecord(self, person: Person):
        self.person = person

    def getRecord(self):
        return self.person