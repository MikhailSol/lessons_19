import logging


# from datetime import datetime
#
# """
# Теперь давайте создадим функцию, которая с помощью
# цикла for заполнит пустой список четными числами
# от 0 до 10  5
# """
#
#
# def count_the_time(func):  # создаем декоратор
#     def wrapper():  # создаем вложенную функцию обертку
#         start = datetime.now()  # отмечаем старт объекта
#         result = func()  # вызываем функцию которая придет в качестве аргументаcout_the_time(func)
#         print(datetime.now() - start)  # отмечаем время работы
#         return result  # возвращает результат переданной функуии
#
#     return wrapper()  # возвараем то, что вернула функция
#
#
# @count_the_time  # вызов декоратора функции
# def createlist():
#     # нецелевой код
#     list = []  # целевой код
#     for _ in range(10, 5):  # целевой код
#         if _ % 2 == 0:  # целевой код
#             list.append(_)  # целевой код
#
#     return list
#
#
# @count_the_time  # вызов декоратора функции
# def create_listgen():
#     list_ = [i for i in range(10 ** 5) if i % 2 == 0]  # целевой код
#     return list_
#
#
# createlist()
# create_listgen()

### Домашнее задание № 1 ###
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def decor(func):
    def wrapper():
        list_1 = []
        for i in arr:
            for c in i:
                if c % 3 != 0:
                    list_1.append(c)
        print(len(list_1))
    return wrapper()




@decor
def new_arr(arr):
    b = []
    for i in arr:
        for c in i:
            if c % 3 == 0:
                b.append(c)
        print(b)
    return b
