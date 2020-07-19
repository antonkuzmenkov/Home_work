''' Реализовать функцию, принимающую два числа
(позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль. '''



def delenie(*args):

    try:
        arg1 = int(input("Введите  первое число: "))
        arg2 = int(input("Введите  второе число: "))
        res = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "Неправильно введено второе число. На ноль делить нельзя."

    return res

print(f'Результат:  {delenie()}')