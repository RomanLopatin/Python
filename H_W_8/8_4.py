"""
coding=utf-8
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""


class Storage:
    def __init__(self, storage_name, total_number=0, total_volume=0, total_weight=0):
        self.storage_name = storage_name
        self.total_number = total_number
        self.total_volume = total_volume
        self.total_weight = total_weight

    def take_on_storage(self, what, how_many):
        self.total_number += how_many

    def write_off_storage(self, what, how_many):
        self.total_number -= how_many

    def __str__(self):
        return f"storage_name: {self.storage_name} \n " \
               f"total_weight: {self.total_weight} \n " \
               f"total_volume: {self.total_volume} \n " \
               f"total_number: {self.total_number}"


class OfficeMachines:
    def __init__(self, machine_id="", machine_name="noName", country="", year_of_production=1900,
                 machine_model="-", machine_weight=0, machine_volume=0):
        self.machine_id = machine_id
        # self.country = country
        # self.year_of_production = year_of_production
        # self.machine_name = machine_name
        # self.machine_model = machine_model
        # self.machine_weight = machine_weight
        # self.machine_volume = machine_volume

    def __str__(self):
        return f"machine_id: {self.machine_id} "
        # f"machine_name: {self.machine_name} \n " \
        # f"country: {self.country} \n " \
        # f"year_of_production: {self.year_of_production} \n " \
        # f"machine_model: {self.machine_model} \n " \
        # f"machine_weight: {self.machine_weight} \n " \
        # f"machine_volume: {self.machine_volume}"


class Printers(OfficeMachines):
    def __init__(self, machine_id, printer_type=""):
        super().__init__(machine_id=machine_id, machine_name="printer")
        self.printer_type = printer_type

    def __str__(self):
        return f"{super().__str__()} " \
               f"\n printer_type: {self.printer_type}"


class Scanners(OfficeMachines):
    def __init__(self, machine_id, scanner_resolution=0):
        super().__init__(machine_id=machine_id, machine_name="scanner")
        self.scanner_resolution = scanner_resolution


class Xerox(OfficeMachines):
    def __init__(self, machine_id, is_mfu=False):
        super().__init__(machine_id=machine_id, machine_name="xerox")
        self.is_mfu = is_mfu


store1 = Storage("store1", 10, 20)
print(store1)
printer1 = Printers("Printer133", "laser")
print(printer1)
printer2 = Printers("Printer177", "Matrix")
print(printer2)
scanner1 = Scanners("Scanner_SCN320", scanner_resolution=360)
print(scanner1)
xerox1 = Xerox("Xrx132_50", is_mfu=True)
store1.take_on_storage(printer1, 10)
print(store1)
store1.write_off_storage(scanner1, 3)
print(store1)
