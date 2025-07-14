import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    # 1. Геттеры
    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    # 2. Добавить товар в чек
    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        if name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        self.__name_items.append(name)
        self.__number_items += 1

    # 3. Удалить товар из чека
    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        self.__name_items.remove(name)
        self.__number_items -= 1

    # 4. Посчитать общую стоимость товаров
    def check_amount(self):
        total = [self.__item_price[item] for item in self.__name_items]
        total_sum = sum(total)
        if self.__number_items > 10:
            total_sum *= 0.9  # скидка 10%
        return total_sum

    # 5. НДС 20%
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = [item for item in self.__name_items if self.__tax_rate.get(item) == 20]
        total = [self.__item_price[item] for item in twenty_percent_tax]
        total_sum = sum(total)
        if self.__number_items > 10:
            total_sum *= 0.9
        return total_sum * 0.2

    # 6. НДС 10%
    def ten_percent_tax_calculation(self):
        ten_percent_tax = [item for item in self.__name_items if self.__tax_rate.get(item) == 10]
        total = [self.__item_price[item] for item in ten_percent_tax]
        total_sum = sum(total)
        if self.__number_items > 10:
            total_sum *= 0.9
        return total_sum * 0.1

    # 7. Общая сумма налогов
    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

    # 8. Статический метод: номер телефона покупателя
    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        str_number = str(telephone_number)
        if len(str_number) != 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        return f'+7{str_number}'

    # Дополнительный статический метод: дата и время покупки
    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()
        date = [
            ['часы', lambda x: x.hour],
            ['минуты', lambda x: x.minute],
            ['день', lambda x: x.day],
            ['месяц', lambda x: x.month],
            ['год', lambda x: x.year]
        ]
        for label, func in date:
            date_and_time.append(f'{label}: {func(now)}')
        return date_and_time


# Пример использования:
if __name__ == '__main__':
    register = OnlineSalesRegisterCollector()

    # Добавим товары
    register.add_item_to_cheque('чипсы')
    register.add_item_to_cheque('кола')
    register.add_item_to_cheque('молоко')

    print('Товары в чеке:', register.name_items)
    print('Количество товаров:', register.number_items)
    print('Общая сумма:', register.check_amount())
    print('НДС 20%:', register.twenty_percent_tax_calculation())
    print('НДС 10%:', register.ten_percent_tax_calculation())
    print('Общая сумма налогов:', register.total_tax())

    # Удалим товар
    register.delete_item_from_check('кола')
    print('Товары после удаления:', register.name_items)
    print('Количество товаров после удаления:', register.number_items)

    # Телефон
    try:
        print('Телефон:', register.get_telephone_number(9123456789))
    except ValueError as e:
        print('Ошибка:', e)

    # Дата и время
    print('Дата и время покупки:', register.get_date_and_time())
