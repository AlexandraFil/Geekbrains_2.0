# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"It's a new car: {self.name} цветом {self.color}. Police: {self.is_police}")

    def go(self):
        print(f"{self.name}: Машина поехала!")

    def stop(self):
        print(f"{self.name}: Машина остановилась!")

    def turn(self, direction="somewhere"):
        if direction == "right":
            print(f"{self.name}: Машина повернула направо!")
        elif direction == "left":
            print(f"{self.name}: Машина повернула налево!")
        else:
            print(f"{self.name}: Машина повернула в неизвестном направлении!")

    def show_speed(self):
        print(f'{self.name}: скорость {self.speed}.')

class TownCar(Car):

    def show_speed(self):
        print(f'{self.name}: скорость {self.speed}.', end=" ")
        if self.speed > 60:
            print(f"Превышение скорости!")

class WorkCar(Car):

    def show_speed(self):
        print(f'{self.name}: скорость {self.speed}.', end=" ")
        if self.speed > 40:
            print(f"Превышение скорости!")

class PoliceCar(Car):

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

class SportCar(Car):
    #
    # def show_speed(self):
    #     print(f"Спортивной машине вcе можно! Скорость {self.speed}.")

town_car = TownCar('Волга', 'черная', 75)
town_car.go()
town_car.show_speed()
town_car.turn(direction="left")
town_car.stop()

police_car = PoliceCar('Другая', "белая", 120)
police_car.go()
police_car.turn(5)

sport_car = SportCar("Красивая", "Красная", 220)
sport_car.show_speed()