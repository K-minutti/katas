class Vehicle:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self._started = False

    def start(self):
        print("Starting engine...")
        self._started = True

    def stop(self):
        print("Stopping engine...")
        self._started = False

    def show_technical_specs(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")


class Car(Vehicle):
    # def __init__(self, make, model, year, num_seats=0):
    #     super().__init__(make, model, year)
    #     self.num_seats = num_seats

    def drive(self):
        print(f'Driving my "{self.make} - {self.model}" on the road')

    def __str__(self):
        return f'"{self.make} - {self.model}" has {self.num_seats} seats'


class Aircraft(Vehicle):
    # def __init__(self, thrust, lift, max_speed):
    #     self.thrust = thrust
    #     self.lift = lift
    #     self.max_speed = max_speed
    
    def fly(self):
        print("Flying in the sky...")
    
    # def show_technical_specs(self):
    #     print(f"Thrust: {self.thrust} kW")
    #     print(f"Lift: {self.lift} kg")
    #     print(f"Max speed: {self.max_speed} km/h")


class Helicopter(Aircraft):
    def __init__(self, thrust, lift, max_speed, num_rotors):
        super().__init__(thrust, lift, max_speed)
        self.num_rotors = num_rotors


class FlyingCar(Car, Aircraft):
    pass


saucer = FlyingCar("Space", "Flyer", "3000", "Black")
saucer.show_technical_specs()
