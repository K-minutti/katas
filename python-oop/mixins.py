"""
Mixin classes define new types, so they're not intended
to be instantiated. A mixin class provides methods that
you can use in other classes to quickly add functionality
"""

import json
import pickle

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class SerializerMixin:
    def to_json(self):
        return json.dumps(self.__dict__)
    
    def to_pickle(self):
        return pickle.dumps(self.__dict__)

#####################
# Delegation Example

class Serializer:
    def __init__(self, instance):
        self.instance = instance
    
    def to_json(self):
        return json.dumps(self.instance.__dict__)
    
    def to_pickle(self):
        return pickle.dumps(self.instance.__dict__)
    

class Employee(SerializerMixin, Person):
    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name, age)
        self.salary = salary
    

class EmployeeD(Person):
    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name, age)
        self.salary = salary
    
    # Delegation example
    def __getattr__(self, attr):
        return getattr(Serializer(self), attr)
    
  

if __name__ == "__main__":
    e = Employee("Tom", 23, 130000)
    ed = EmployeeD("Kit", 50, 200000)
    print(e.to_json())
    print(ed.to_pickle())

