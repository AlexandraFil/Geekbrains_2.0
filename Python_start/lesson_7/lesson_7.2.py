# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractclassmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractclassmethod
    def consumption(self):
        pass

class Coat(Clothes):

    @property
    def consumption(self):
        return round(self.param/6.5) + 0.5


class Suit(Clothes):

    @property
    def consumption(self):
        return 2 * self.param + 0.3

coat_1 = Coat(44)
coat_2 = Coat(46)
coat_3 = Coat(50)
coat_4 = Coat(40)
suit_1 = Suit(165)
suit_2 = Suit(155)
suit_3 = Suit(178)
suit_4 = Suit(180)

print(f"Расход ткани на пальто: {coat_1.consumption + coat_2.consumption + coat_3.consumption + coat_4.consumption}.")
print(f"Расход ткани на костюмы: {suit_1.consumption + suit_2.consumption + suit_3.consumption + suit_4.consumption}.")

