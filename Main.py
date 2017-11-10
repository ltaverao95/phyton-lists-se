from ListSE import ListSE
from Person import Person

listSE: ListSE = ListSE()

#Aditions at the end
listSE.append(Person("pepito", 27, "m", 34870, "sf"))
listSE.append(Person("pepito2", 27, "m", 34870, "sf"))
listSE.append(Person("pepito3", 27, "m", 34870, "sf"))
listSE.append(Person("pepito4", 27, "m", 34870, "sf"))

#Aditions in position
listSE.insert(Person("pepito3", 27, "m", 34870, "sf"), Person("pepito5", 27, "m", 34870, "sf"))

#Get by person
print(listSE.getPerson(Person("pepito4", 27, "m", 34870, "sf")).__dict__)

#Remove by person
listSE.remove(Person("pepito5", 27, "m", 34870, "sf"))

#List length
print(listSE.__len__())

personsList = listSE.getPersonsList()
if(personsList.__len__() > 0):
    for person in personsList:
        print(person.__dict__)