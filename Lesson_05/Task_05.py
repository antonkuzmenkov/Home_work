# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def summa():
    try:
        with open('file_5.txt', 'w+') as new_file:
            in_file = input('Введите цифры через пробел \n')
            new_file.writelines(in_file)
            my_numb = in_file.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Ошибка ввода')
summa()