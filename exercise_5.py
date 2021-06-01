from abc import ABC, abstractmethod


class Sklad:
    def __init__(self, name: str):
        self.name = name
        self.product = {}

    def move_position(self, to_sklad, sku, amount):
        if self.check_available(sku, amount):
            # сюда бы транзакцию)))
            self.consumption(sku, amount)
            to_sklad.coming(sku, amount)
        else:
            print(f'Недостаточно товара {sku}')

    def check_available(self, sku, amount) -> bool:
        return self.get_available_sku(sku) >= amount

    def coming(self, sku, amount):
        """Приход товара на склад"""
        new_coming = {sku: self.get_available_sku(sku) + amount}
        self.product.update(new_coming)

    def consumption(self, sku, amount):
        """Расход товара со склада"""
        new_coming = {sku: self.get_available_sku(sku) - amount}
        self.product.update(new_coming)

    def get_available_sku(self, sku):
        return 0 if self.product.get(sku) is None else self.product.get(sku)


class OfficeEquipment(ABC):

    def __init__(self, name, vendor_code):
        self.name = name
        self.vendor_code = vendor_code
        self.price = 0

    @abstractmethod
    def set_price(self, price):
        self.price = price

    @abstractmethod
    def __str__(self):
        return f'{self.name} {self.vendor_code}'


class Printer(OfficeEquipment):
    def __str__(self):
        return super().__str__()

    def set_price(self, price):
        super(Printer, self).set_price(price)

    def __init__(self, name, vendor_code, unique_characteristic_of_printers):
        super().__init__(name, vendor_code)
        self.unique_characteristic_of_printers = unique_characteristic_of_printers


class Scanner(OfficeEquipment):
    def __str__(self):
        return super().__str__()

    def set_price(self, price):
        super(Scanner, self).set_price(price)

    def __init__(self, name, vendor_code, unique_characteristic_of_scanner):
        super().__init__(name, vendor_code)
        self.unique_characteristic_of_scanner = unique_characteristic_of_scanner


class Copier(OfficeEquipment):
    def __str__(self):
        return super().__str__()

    def set_price(self, price):
        super(Copier, self).set_price(price)

    def __init__(self, name, vendor_code, unique_characteristic_of_copier):
        super().__init__(name, vendor_code)
        self.unique_characteristic_of_copier = unique_characteristic_of_copier


copier = Copier('Канон', 'AW200', 'бомбический копир')
printer = Printer('Ксерокс', 'S56DE58', 'эпический принтер')

sklad = Sklad('Основной')
office = Sklad('Офис')

sklad.coming(copier, 10)
sklad.coming(printer, 10)

sklad.move_position(office, printer, 5)
sklad.move_position(office, copier, 5)
sklad.move_position(office, printer, 50)

pass
