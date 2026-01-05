""""""
from datetime import datetime
"""
Создайте функцию make_rounder(), которая принимает количество знаков для округления и возвращает другую функцию.
Полученная функция должна принимать число и возвращать его, округлённое до указанного ранее количества знаков после запятой.
"""
#1
def make_rounder(round_num):
    def inner_rounder(value):
       return round(value, round_num)
    return inner_rounder

round3 = make_rounder(3)
round2 = make_rounder(2)
round1 = make_rounder(1)
round0 = make_rounder(0)

print(round3(3.1414124124124))
print(round2(3.14159))
print(round1(3.766))
print(round0(9.999))

"""
Создайте функцию, которая возвращает вложенный логгер событий.
Каждый вызов логгера должен сохранять событие с текущим временем (если оно передано) и возвращать весь список событий.
"""
#2
def log():
    list_of_events = []
    def inner_log(text=None):
        if text is None:
            return list_of_events
        list_of_events.append(text + ": " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    return inner_log


logger = log()
logger("hello")
logger("master")
logger("van!")
for i in logger():
     print(i)

"""
Создайте декоратор frame, который оборачивает результат функции рамкой из 50 символов -, выводя по строке до и после вызова функции.
"""
#3
def say_hello():
    print("Hello, player!")


def frame(func=say_hello):
   def inner_frame():
        print("-" * 50)
        func()
        print("-" * 50)
   return inner_frame

frame()()



