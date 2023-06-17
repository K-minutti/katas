class Car:

    def __init__(self, make: str, model: str, year: int, color: str):
        self.make: str = make
        self.model: str = model
        self.year: int = year
        self.color: str = color 
        self.started: bool = False
        self.speed: int = 0
        self.max_speed: int = 200

    def start(self):
        print("Starting the car...")
        self.started = True

    def stop(self):
        print("Stopping the car...")
        self.started = False

    def accelerate(self, value):
        if not self.started:
            print("Car is not started")
            return 
        self.speed: int = min(self.speed+value, self.max_speed)
        print(f"Accelerating to {self.speed} km/h...")

    def brake(self, value):
        self.speed = max(self.speed-value, 0)
        print(f"Braking to {self.speed} km/h...")

    def __str__(self):
        return f"{self.make}, {self.model}, {self.color}: ({self.year})"
    
    def __repr__(self):
        return (
            f"{type(self).__name__}"
            f'(make="{self.make}"), '
            f'model="{self.model}", '
            f"year={self.year}, "
            f'color="{self.color}"'
        )


if __name__ == "__main__":
    car = Car("Porsche", "911 Turbo", 2022, "Black")
    car.start()

    car.accelerate(1000)
    car.brake(50)
    car.brake(20)
    car.brake(1000)
    car.stop()
    print(car.__repr__())
