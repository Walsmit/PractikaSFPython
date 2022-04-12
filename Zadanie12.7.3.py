# Ввод данных с преобразованием в целые числа
money = int(input("Введите сумму:"))

# Словарь с процентными ставками
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

# Операции по вычеслению чисел
deposit1 = money * per_cent['ТКБ'] / 100
deposit2 = money * per_cent['СКБ'] / 100
deposit3 = money * per_cent['ВТБ'] / 100
deposit4 = money * per_cent['СБЕР'] / 100

# Создание одной переменной с округлением числа
deposit = round(deposit1), round(deposit2), round(deposit3), round(deposit4)

# Вывод расчетов
print(deposit)
# Вывод максимального числа
print("Максимальная сумма, которую вы можете заработать -", max(deposit))
