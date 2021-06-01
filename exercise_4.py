from abc import ABC, abstractmethod


class Sklad:
    def __init__(self, name: str):
        self.name = name
        self.product = {}


class OfficeEquipment(ABC):

    def __init__(self, name, vendor_code):
        self.name = name
        self.vendor_code = vendor_code
        self.price = 0

    @abstractmethod
    def set_price(self, price):
        self.price = price


class Printer(OfficeEquipment):
    def set_price(self, price):
        super(Printer, self).set_price(price)

    def __init__(self, name, vendor_code, unique_characteristic_of_printers):
        super().__init__(name, vendor_code)
        self.unique_characteristic_of_printers = unique_characteristic_of_printers


class Scanner(OfficeEquipment):
    def set_price(self, price):
        super(Scanner, self).set_price(price)

    def __init__(self, name, vendor_code, unique_characteristic_of_scanner):
        super().__init__(name, vendor_code)
        self.unique_characteristic_of_scanner = unique_characteristic_of_scanner


class Copier(OfficeEquipment):
    def set_price(self, price):
        super(Copier, self).set_price(price)

    def __init__(self, name, vendor_code, unique_characteristic_of_copier):
        super().__init__(name, vendor_code)
        self.unique_characteristic_of_copier = unique_characteristic_of_copier


copier = Copier('Канон', 'AW200', 'бомбический копир')
printer = Printer('Ксерокс', 'S56DE58', 'эпический принтер')
