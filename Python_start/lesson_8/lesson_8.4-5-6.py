# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class Storehouse:
    def __init__(self, address, owner):
        self.address = address
        self.owner = owner

    def __str__(self):
        return f"Новый склад:\nадрес: {self.address}, владелец: {self.owner}."

class Items:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.selling_price = price * 1.5
        self.quantity = quantity
        self.item_info = {'Название': self.name, 'Закупочная цена': self.price, 'Минимальная цена при продаже': self.selling_price, 'Количество на складе': self.quantity}
        self.my_store = []
        self.my_store.append(self.item_info)
        self.my_store_all = []
        self.my_store_all.append(self.my_store)

    def __str__(self):
        return f'{self.name}: {self.quantity} единиц на складе, рассчитываемый доход от партии {(self.selling_price - self.price) * self.quantity}'

    def add_items(self):
        print(f'Добавление новых наименований класса:')
        try:
            self.name = input(f'Введите название: ')
            self.price = int(input(f'Введите закупочную цену за единицу: '))
            self.quantity = int(input(f'Введите количество: '))
            self.item_info = {'Название': self.name, 'Закупочная цена': self.price,
                              'Минимальная цена при продаже': self.selling_price, 'Количество на складе': self.quantity}
            self.my_store.append(self.item_info)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных. Выход.'

        print(f'Для выхода введите Q, чтобы продолжить Enter:')
        q = input()
        if q == 'Q' or q == 'q':
            self.my_store_all.append(self.my_store)
            for i in range(len(self.my_store_all)):
                print(self.my_store_all[i])
            return f'Выход'
        else:
            return Items.add_items(self)

class Printer(Items):
    def to_print(self):
        return f'{self.name} can print something'


class Scanner(Items):
    def to_scan(self):
        return f'{self.name} can scan something'


class Xerox(Items):
    def to_copy(self):
        return f'{self.name} can copy something'


storage_1 = Storehouse('Moscow', 'Ivanov')
print(storage_1)

printer_1 = Printer('hp', 2000, 5)
print(printer_1)
print(printer_1.item_info)
print(printer_1.add_items())
print(printer_1.my_store_all)

scan_1 = Scanner('Canon', 1200, 5)
print(scan_1)
print(scan_1.item_info)

copier_1 = Xerox('Xerox', 1500, 7)
print(copier_1)
print(copier_1.item_info)

print(printer_1.to_print())