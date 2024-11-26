class Person:
    def __init__(self, name, age, id):  
        self.__name = name
        self.age = age
        self._id = id  

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age 

    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name

    def get_id(self):
        return self._id

    def set_id(self, new_id):  
        self._id = new_id

#-------------------------
person1 = Person('Juana', 18, 1130543)  
print(person1.get_age(), person1.get_name(), person1.get_id())

person1.set_age(19)
person1.set_name('Juan')
person1.set_id('1130')
print(person1.get_age(), person1.get_name(), person1.get_id())
