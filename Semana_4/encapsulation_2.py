class Vehicle:

    def __init__(self, speed):
        self.__speed = speed

    def accelerate(self, value):
        self.__speed += value

    def brake(self, value):
        if value > 0:
            self.__speed -= value
            if self.__speed < 0:
                self.__speed = 0

    def __str__(self):
        return f"Su velocidad es {self.__speed}"

vehicle1 = Vehicle(100)
print(vehicle1)

vehicle1.accelerate(20)
print(vehicle1)

vehicle1.brake(50)
print(vehicle1)

vehicle1.brake(100)
print(vehicle1)
