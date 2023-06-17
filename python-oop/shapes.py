import math

class PositiveNumber:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]
    
    def __set__(self, instance, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError(f"expected positive number not: {value}")
        instance.__dict__[self._name] = value
    

class Circle:
    radius: PositiveNumber = PositiveNumber()

    def __init__(self, radius: int | float):
        self.radius: int | float = radius
    
    # @property
    # def radius(self):
    #     return self._radius
    
    # @radius.setter
    # def radius(self, value):
    #     if not isinstance(value, int | float) or value <= 0:
    #         raise ValueError(f"expected positive number not: {value}")
    #     self._radius: int  | float = value

    def calculate_area(self):
        return round(math.pi * self.radius**2, 2)

class Square:
    side: PositiveNumber = PositiveNumber()

    def __init__(self, side: int | float):
        self.side: int | float = side
    
    # @property
    # def side(self):
    #     return self._side

    # @side.setter
    # def side(self, value):
    #     if not isinstance(value, int | float) or value <= 0:
    #         raise ValueError(f"expected positive number not: {value}")
    #     self._side = value

    def calculate_area(self):
        return round(self.side**2, 2)

if __name__ == "__main__":
    c = Circle(1)
    print("radius", c.radius)
    print(c.calculate_area())

    s = Square(10)
    print("side", s.side)
    print(s.calculate_area())