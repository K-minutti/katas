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
    
class Employee(SerializerMixin, Person):
    def __init__(self, name: str, age: int, salary: int):
        super().__init__(name, age)
        self.salary = salary


if __name__ == "__main__":
    e = Employee("Tom", 23, 130000)
    print(e.to_json())