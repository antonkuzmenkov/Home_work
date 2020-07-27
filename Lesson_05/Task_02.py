# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

my_file = open('test_2.txt', 'r')
cont = my_file.read()
print(f'Содержит: \n {cont}')
my_file = open('test_2.txt', 'r')
cont = my_file.readlines()
print(f'Количество строк в файле : {len(cont)}')
my_file = open('test_2.txt', 'r')
my_file = open('test_2.txt', 'r')
cont = my_file.read().split()
print(f'Общее количество слов - {len(cont)}')
my_file.close()