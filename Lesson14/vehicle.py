import self as self


class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def accelerate(self, speed_acc):
        self.speed += speed_acc

    def brake(self, speed_rit):
        self.speed -= speed_rit

    def get_current_speed(self):
        return self.speed


class Airplane(Vehicle):
    def __init__(self, speed):
        super().__init__(speed)



class Car(Vehicle):
    def __init__(self, speed):
        super().__init__(speed)
        self.reverse_gear = False

    def accelerate(self, speed_acc):
        super(Vehicle, self).accelerate(speed_acc)

    def brake(self, speed_rit):
        if self.speed = 0
            print("The car is already stopped")
        else:
            super(Vehicle, self).brake(speed_rit)

    def get_current_speed(self):
        return self.speed

    def enter_reverse_gear(self):
        if self.speed == 0:
            if self.reverse_gear == False:
                self.reverse_gear = True
            else:
                self.reverse_gear = False
        else:
            print("The gear can only be reversed if the speed is 0.")












