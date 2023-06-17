from csv import DictReader
from os import path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __str__(self):
        return self.__name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {str(self.price)}, {str(self.quantity)})"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        return None

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str) -> None:
        if len(new_name) < 11:
            self.__name = new_name
        else:
            print("Exception: Длина наименования" + \
                  " товара превышает 10 символов.")

    @classmethod
    def instantiate_from_csv(cls, path=path.join('..', 'src', 'items.csv')):
        try:
            with open(path, 'r', encoding ='cp1251') as csvfile:
                read = DictReader(csvfile)
                for i in read:
                    cls(i['name'], i['price'], i['quantity'])
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')
        except KeyError:
            raise InstantiateCSVFile
    @staticmethod
    def string_to_number(string_number: str) -> int:
        number = int(float(string_number))
        return number


class MyException(Exception):
    pass


class InstantiateCSVFile(MyException):
    """Класс исключение при повреждении файла"""

    def __init__(self, *args, **kwargs):
        self.message = 'Файл item.csv поврежден'

    def __str__(self):
        return self.message
