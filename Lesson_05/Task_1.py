# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

my_file = open('test.txt', 'w')
in_file = input('Введите текст \n')
while in_file:
    my_file.writelines(in_file)
    in_file = input('Введите текст \n')
    if not in_file:
        break

my_file.close()
my_file = open('test.txt', 'r')
cont = my_file.readlines()
print(cont)
my_file.close()