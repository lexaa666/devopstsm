### Урок 32 задача N1
## Скрипт с функцией, которые будут умножать два числа, указанные в качестве параметров. Скрипт должен вернуть 0, если результат четное число, и 1 если нет.

task_first = lambda a, b: 0 if (a * b % 2 == 0) else 1
print("Задача N1")
print(f'Результат скрипта : {task_first(3, 2)}')
print("################\n")

### Урок 32 задача N2
import os

print("Задача N2")
param = input('Введите путь:')


def path_to_file(path):
    for paths, dirs, files in os.walk(path):
        for name in files:
            print(os.path.join(paths, name))


path_to_file(param)
print("################\n")

### Урок 32 задача N3
lists = ['Первый', 'Пятый', 'Десятый', 'Двенадцатый', 'Двадцатый']


def task_three(list):
    for ls in list:
        print(f'Элемент списка : {ls}')


print("Задача N3")
task_three(lists)
print("################")
