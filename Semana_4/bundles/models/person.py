from abc import ABC

#esta es una clase abstracta
#es no 

class Person(ABC):
    def __init__ (self,name,lastname,age,addres):
        self.name=name
        self.lastname=lastname
        self.age=age
        self.addres=addres
        