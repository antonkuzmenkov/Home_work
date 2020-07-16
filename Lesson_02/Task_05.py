# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

def rate(a, value):
    m_value = max(a)
    if value > m_value:
        a.insert(0, value)
    elif value in a:
        a.insert(a.index(value),value)
    else:
        a.append(value)

list = [7, 5, 3, 3, 2]
print(list)
rate(list, 3)
print(list)
start = input('смотрим с числом 8 (y/n) :')
if start == "y":
    list = [7, 5, 3, 3, 2]
    rate(list, 8)
    print(list)
elif start == "n":
    print("Bye")
start = input('смотрим с числом 1 (y/n) :')
if start == "y":
    list = [7, 5, 3, 3, 2]
    rate(list, 1)
    print(list)
elif start == "n":
    print("Bye")
# Ввел в коце if для того чтобы избежать некорректного ответа
# так как list = [7, 5, 3, 3, 2]
# print(list)
# rate(list, 3)
# print(list)
# rate(list, 8)
# print(list)
# rate(list, 1)
# print(list)
# прведет -
# list = [7, 5, 3, 3, 2]
# print(list)
# rate(list, 3)
# print(list)
# rate(list, 8)
# print(list)
# rate(list, 1)
# print(list)
# по-другому никак не придумал как этого избежать