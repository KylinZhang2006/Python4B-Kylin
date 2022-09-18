class Vehicle:
    def __init__(self, top_speed):
        self.top_speed = top_speed
        self.speed = 0

    def accelerate(self, speed_acc):
        self.speed += speed_acc
        if self.speed > self.top_speed:
            self.speed = self.top_speed
            print("Going at max speed!")

    def brake(self, speed_rit):
        self.speed -= speed_rit
        if self.speed < 0:
            self.speed = 0
            print("We have come to a halt")

    def get_current_speed(self):
        return self.speed


class Airplane(Vehicle):
    def __init__(self, top_speed):
        super().__init__(top_speed)
        self.is_flying = False

    def accelerate(self, speed_acc):
        super().accelerate(speed_acc)

    def brake(self, speed_rit):
        super().brake(speed_rit)

    def get_flying_status(self):
        if self.speed > 250:
            self.is_flying = True
        else:
            self.is_flying = False
        return self.is_flying

    def get_current_speed(self):
        return self.speed


class Car(Vehicle):
    def __init__(self, top_speed):
        super().__init__(top_speed)
        self.reverse_gear = False

    def accelerate(self, speed_acc):
        if self.speed > self.top_speed:
            self.speed = self.top_speed
            print("Going at max speed!")
        elif self.reverse_gear:
            if speed_acc > 0:
                super(Car, self).accelerate(-speed_acc)
            else:
                super(Car, self).accelerate(speed_acc)
        else:
            if speed_acc < 0:
                super(Car, self).accelerate(-speed_acc)
            else:
                super(Car, self).accelerate(speed_acc)

    def brake(self, speed_rit):
        if self.speed == 0:
            print("The car is already stopped")
        elif self.reversed:
            if speed_rit > 0:
                super(Car, self).brake(-speed_rit)
            else:
                super(Car, self).brake(speed_rit)
        else:
            if speed_rit < 0:
                super(Car, self).brake(-speed_rit)
            else:
                super(Car, self).brake(speed_rit)

    def enter_reverse_gear(self):
        if self.speed == 0:
            self.reverse_gear = not self.reverse_gear
        else:
            print("The gear can only be reversed if the speed is 0.")

    def get_current_speed(self):
        return self.speed


class Boat(Vehicle):
    def __init__(self, top_speed, max_passenger):
        self.max_passenger = max_passenger
        self.passenger_num = 0
        super().__init__(top_speed)

    def set_passenger_num(self, passenger_num):
        self.passenger_num = passenger_num

    def accelerate(self, speed_acc):
        self.speed += speed_acc - self.passenger_num
        if self.speed > self.top_speed:
            self.speed = self.top_speed
            print("Going at max speed!")
        elif self.speed < 0:
            self.speed = 0
            print("The boat is stopped by passenger's weight. Accelerate more!")

    def brake(self, speed_rit):
        self.speed -= speed_rit + self.passenger_num
        if self.speed < 0:
            self.speed = 0
            print("We have come to a halt")


"""Main Methods"""
airplane = Airplane(1200)
car = Car(240)

airplane.accelerate(200)
print(airplane.get_flying_status())
print(airplane.get_current_speed())
airplane.accelerate(60)
print(airplane.get_flying_status())

car.accelerate(50)
car.enter_reverse_gear()
car.accelerate(200)
print(car.speed)
print(car.get_current_speed())

boat = Boat(70, 30)
boat.set_passenger_num(20)
boat.accelerate(30)
boat.accelerate(90)
print(boat.get_current_speed())
boat.brake(60)
print(boat.get_current_speed())