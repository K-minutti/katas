class Point:
    __slots__ = ("x", "y")
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

class PointCls:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

if __name__ == "__main__":
    p = Point(4, 8)
    # p.__dict__ throws error no attr __dict__
    pc = PointCls(4,8)
    from pympler import asizeof
    print(asizeof.asizeof(Point(4,8)))
    print(asizeof.asizeof(PointCls(4,8)))
