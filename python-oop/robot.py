class Bot:
    def __init__(self) -> None:
        self.body = Body()
        self.arm = Arm()

    def rotate_body_left(self, degrees: int = 10):
        self.body.rotate_left(degrees)

    def rotate_body_right(self, degrees: int = 10):
        self.body.rotate_right(degrees)
    
    def move_arm_up(self, distance: int = 10):
        self.arm.move_up(distance)
    
    def move_arm_down(self, distance: int = 10):
        self.arm.move_down(distance)

    def weld(self):
        self.arm.weld()

    def shoot(self):
        self.arm.shoot()

    def get_ammo(self):
        self.arm.show_ammo()

    def change_arm(self, arm):
        self.arm = arm
    

class Body:
    def __init__(self):
        self.rotation = 0

    def rotate_left(self, degrees: int = 10):
        print(f"Rotating body {degrees} degrees to the left...")
        self.rotation -= degrees
    
    def rotate_right(self, degrees: int = 10):
        print(f"Rotating body {degrees} to the right...")
        self.rotation += degrees

class Arm:
    def __init__(self):
        self.position = 0

    def move_up(self, distance: int = 1):
        print(f"Moving arm {distance} cm up...")
        self.position += distance
    
    def move_down(self, distance: int = 1):
        print(f"Moving arm {distance} cm down...")
        self.position -= distance
    
    def weld(self):
        print("Welding...")
    
class GunArm(Arm):
    def __init__(self):
        self.bullets = 42
        super().__init__()
    
    def shoot(self):
        print("Shooting...")
        self.bullets -= 1
    
    def reload(self, bullets: int):
        if self.bullets + bullets < 42:
            self.bullets += bullets
        else:
            self.bullets = 42
    
    def show_ammo(self):
        print(f"Bullet count {self.bullets}")

    
# Dependency Injection
class IndustrialRobot:
    def __init__(self, body: Body, arm: Arm):
        self.body = body
        self.arm = arm

    def rotate_body_left(self, degrees: int = 10):
        self.body.rotate_left(degrees)

    def rotate_body_right(self, degrees: int = 10):
        self.body.rotate_right(degrees)
    
    def move_arm_up(self, distance: int = 10):
        self.arm.move_up(distance)
    
    def move_arm_down(self, distance: int = 10):
        self.arm.move_down(distance)

    def weld(self):
        self.arm.weld()

    def shoot(self):
        self.arm.shoot()

    def get_ammo(self):
        self.arm.show_ammo()

    def change_arm(self, arm):
        self.arm = arm



if __name__ == "__main__":
    b = Bot()
    for _ in range(5):
        b.rotate_body_left(8)
    b.move_arm_up(15)
    b.weld()
    a = GunArm()
    b.change_arm(a)
    for _ in range(20):
        b.shoot()
    b.weld()
    b.get_ammo()
    print("--- DI - Robot ---")
    robot = IndustrialRobot(Body(), Arm()) # Deps injection
    robot.rotate_body_left()
    robot.move_arm_up(14)
    robot.weld()