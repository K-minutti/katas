"""
Protocols
> Iterator	
Allows you to create iterator objects	
.__iter__() and .__next__()
> Iterable	
Makes your objects iterable	
.__iter__()
> Descriptor	
Lets you write managed attributes	
.__get__() and optionally .__set__(), .__delete__(), and .__set_name__()
> Context manager	
Enables an object to work on with statements	
.__enter__() and .__exit__()
"""

class ThreeDPoint:
    
    def __init__(self, x, y, z: int):
        self.x: int = x
        self.y: int = y
        self.z: int = z
    
    def __iter__(self):
        yield from (self.x, self.y, self.z)

    @classmethod
    def from_sequence(cls, sequence):
        return cls(*sequence)
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.x}, {self.y}, {self.z})"
    

if __name__ == "__main__":

    p = ThreeDPoint(1,2,3)
    print(repr(p))

    pd = ThreeDPoint.from_sequence((4,5,6))
    print(repr(pd))

