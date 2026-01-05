#1 и 2 задачки в одном решении!
import time


input_repeats = int(input("Введите желаемое количество повторений для теста функции: "))
def measure_time(func,repeats=input_repeats):
    def wrapper():
        list_time = []
        c = 0
        for i in range(repeats):
            start = time.time()
            func()
            c += 1
            print("Функция выполнилась "+ str(c) +"-й раз!")
            end = time.time()
            list_time.append(end - start)
        print (f"Среднее время выполнения для {input_repeats} вызовов(вызова): {round(sum(list_time) / len(list_time), 2)}")
    return wrapper



@measure_time
def compute():
    total = 0
    for i in range(100000000):
        total += i
    return total



compute()

