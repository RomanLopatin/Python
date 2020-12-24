"""
coding=utf-8
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""


class IsNotANumberError(Exception):
    def __init__(self, msg):
        pass


class CheckError(Exception):
    def __init__(self, msg):
        pass


class Storage:
    storage_count = 0

    def __init__(self, storage_name, total_number=0, total_volume=0, total_weight=0):
        Storage.storage_count += 1
        self.storage_name = storage_name
        self.total_number = total_number
        self.total_volume = total_volume
        self.total_weight = total_weight
        self.what_n_how_many = dict()

    def take_on_storage(self, what, how_many):

        if not self.data_check_is_ok(what, how_many):
            return

        self.total_number += how_many
        if what.machine_id in self.what_n_how_many.keys():
            self.what_n_how_many[what.machine_id] += how_many
        else:
            self.what_n_how_many.update({what.machine_id: how_many})

    def write_off_storage(self, what, how_many):
        if not self.data_check_is_ok(what, how_many):
            return False
        if not self.write_off_storage_chek_is_ok(what, how_many):
            return False
        self.write_off_storage_chek_is_ok(what, how_many)
        self.total_number -= how_many
        if what.machine_id in self.what_n_how_many.keys():
            self.what_n_how_many[what.machine_id] -= how_many
        else:
            self.what_n_how_many.update({what.machine_id: -how_many})

    def move_from_self_to_other(self, other, what, how_many):
        if not self.data_check_is_ok(what, how_many):
            return False
        if not self.write_off_storage_chek_is_ok(what, how_many):
            return False
        self.total_number -= how_many
        if what.machine_id in self.what_n_how_many.keys():
            self.what_n_how_many[what.machine_id] -= how_many
        else:
            self.what_n_how_many.update({what.machine_id: -how_many})
        other.total_number += how_many
        if what.machine_id in other.what_n_how_many.keys():
            other.what_n_how_many[what.machine_id] += how_many
        else:
            other.what_n_how_many.update({what.machine_id: how_many})

    def __str__(self):
        return f"storage_name: {self.storage_name} \n " \
               f"total_weight: {self.total_weight} \n " \
               f"total_volume: {self.total_volume} \n " \
               f"total_number: {self.total_number}"

    def show_what_is_onboard(self):
        print(f"{self.storage_name}: {self.what_n_how_many}")

    def data_check_is_ok(self, what, how_many):
        try:
            if type(how_many) != int:
                raise IsNotANumberError("Ошибка ввода данных!")
        except IsNotANumberError as err:
            print(err)
            return False
        except Exception:
            return False
        else:
            return True

    def write_off_storage_chek_is_ok(self, what, how_many):
        if what.machine_id in self.what_n_how_many.keys() and self.what_n_how_many[what.machine_id] >= how_many:
            return True
        else:
            try:
                raise CheckError("Ошибка товарных остатков! Опреация отклонена!")
            except  CheckError as err:
                print(err)
                return False
            except Exception:
                return False


class OfficeMachines:
    def __init__(self, machine_id="", machine_name="noName", country="", year_of_production=1900,
                 machine_model="-", machine_weight=0, machine_volume=0):
        self.machine_id = machine_id
        self.count = 0
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
store2 = Storage("store2", 0, 0)
# Storage.show_what_is_onboard(store2)
printer1 = Printers("Printer133", "laser")
printer2 = Printers("Printer177", "Matrix")
scanner1 = Scanners("Scanner_SCN320", scanner_resolution=360)
xerox1 = Xerox("Xrx132_50", is_mfu=True)
store1.take_on_storage(printer1, 1000)
store1.show_what_is_onboard()
store1.take_on_storage(printer1, 10)
store1.write_off_storage(printer1, 333)
Storage.show_what_is_onboard(store1)
store1.take_on_storage(printer2, 18)
store1.take_on_storage(scanner1, 6)
store1.take_on_storage(xerox1, 56)
Storage.show_what_is_onboard(store1)
store1.write_off_storage(scanner1, 333)  #  вызвывает ошибку товарных остатков
store1.show_what_is_onboard()
Storage.show_what_is_onboard(store2)
store2.take_on_storage(printer1, 33)
Storage.show_what_is_onboard(store2)
store2.take_on_storage(printer2, 3)
store2.show_what_is_onboard()
Storage.move_from_self_to_other(store1, store2, printer1, 77)
Storage.show_what_is_onboard(store1)
Storage.show_what_is_onboard(store2)
Storage.move_from_self_to_other(store1, store2, printer1, 1000)
Storage.show_what_is_onboard(store1)
Storage.show_what_is_onboard(store2)
# store1.show_what_is_onboard()
# print(Storage.storage_count)
