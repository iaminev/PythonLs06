from random import randint
import time

def create_array(objs: int):
    return [randint(1, 19) for _ in range(objs)]

def sequence_recursion(a_1, n, d):
    if n <= 0:
        return a_1
    else:
        return d + sequence_recursion(a_1, n-1, d)

def task30():
    print("Задача 30.")
    a_1 = int(input("Введите a1: "))
    d = int(input("Введите d: "))
    n = int(input("Введите n: "))

    result_list_1 = []
    result_list_2 = list()

    tic_1 = time.perf_counter()
    for i in range(n):
        result_list_1.append(a_1+i*d)
    toc_1 = time.perf_counter()
    print(f'Результат заполнения в цикле:   {result_list_1} \n за {toc_1 - tic_1:0.5f} секунд')

    tic_2 = time.perf_counter()
    for i in range(n):
        result_list_2.append(sequence_recursion(a_1, i, d))
    toc_2 = time.perf_counter()
    print(f'Результат заполнения рекурсией: {result_list_2} \n за {toc_2 - tic_2:0.5f} секунд')

    print(f'Рекурсия сработала медленнее в {(toc_2 - tic_2)/(toc_1 - tic_1):0.5f} раз')

def task32():
    print("Задача 32.")
    my_array = create_array(20)
    print(f'Исходный массив: {my_array}')
    min_value = int(input("Введите минимальное значение(1..19): "))
    max_value = int(input("Введите максимальное значение(1..19): "))
    filtered_array = list(filter(lambda x: (x >= min_value)&(x <= max_value), my_array))
    print(f'Отфильтрованный массив: {filtered_array}')

if __name__ == '__main__':
    task30()
    task32()
