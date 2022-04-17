# Ввод количества билетов
ticket = int(input("Введите количество билетов: "))
# Список для получения чисел
age = []

# Цикл для ввода возраста по количеству билетов, сортировка по заданым суммам с добавлением в список
for x in range(ticket):
    i = int(input("Введите возраст: "))
    if i < 18:
        a = 0
        age.append(a)
    elif 18 < i <= 25:
        b = 990
        age.append(b)
    elif i > 25:
        c = 1390
        age.append(c)

# Сложение чисел внутри списка
total_amount = sum(age)

# Предоставление 10 % скидки при более трех билетов, вывод общей стоимости билетов
if ticket > 2:
    resultat = total_amount - total_amount * 10 / 100
    print("Сумма к оплате с учётом 10% скидки:", round(resultat))
else:
    print("Сумма к оплате:", total_amount)
