# Переменная с числами
numbers = 1, 12, 5, 6, 22, 8, 49, 0, 4
# Преобразование в список
list_ = list(numbers)

# Ввод пользователя
number = int(input("Введите число от 0 до 50: "))

# Добавления элемента в список
list_.append(number)


# Функция: метод сортировки пузырьком
def qsort(mas):
    if len(mas) <= 1:
        return mas

    elem = mas[0]
    left = list(filter(lambda x: x < elem, mas))
    centre = [i for i in mas if i == elem]
    right = list(filter(lambda x: x > elem, mas))

    return qsort(left) + centre + qsort(right)


# Создание переменой с присвоением от сортированного списка
sort = qsort(list_)
print(sort)


# Бинарный поиск индекса элемента
def binary_search(array, num, left, right):
    if left > right:
        return False

    mid = (left + right) // 2
    if array[mid] == num:
        return mid - 1  # Что бы найти решение задачи указал, что индекс мида должен быть меньше на 1
    elif num <= array[mid]:
        return binary_search(array, num, left, mid - 1)
    else:
        return binary_search(array, num, mid + 1, right)


print("Индекс = ", binary_search(sort, number, 0, len(sort)))
