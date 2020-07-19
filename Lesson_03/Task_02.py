'''
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
'''

def my_func (name, surname, year, city, email, phone):
     return ' '.join([name, surname, year, city, email, phone])
print(my_func(surname = 'Kuz', name = 'Anton', year = '1988', city = 'Moscow', email = 'error@gmail.ru', phone = '8-903-111-11-11'))