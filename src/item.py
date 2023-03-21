import csv


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
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)


    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value: str):
        if len(value) > 10:
          print('Длина наименования товара превышает 10 символов')
        else:
          self.__name = value


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        with open('../src/items.csv','r',encoding='windows-1251') as file:
            data = csv.DictReader(file)
            for line in data:
                cls.all.append(line)

    @staticmethod
    def string_to_number(number):
        return int(number.split('.')[0])

