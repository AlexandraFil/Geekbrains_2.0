# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title="Something"):
        self.title = title

    def draw(self):
        print(f'Take {self.title} to draw!')

class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Start drawing with {self.title} pen.")


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Start drawing with {self.title} pencil.")


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Start drawing with {self.title} handle.")

st = Stationery()
st.draw()
pen = Pen("Gel")
pen.draw()
pencil = Pencil('Конструктор')
pencil.draw()
handle = Handle("Marker")
handle.draw()