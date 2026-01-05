
import time

"""
Measure time of an execution of the function, and then output an average execution time
"""
input_repeats = int(input("Enter the desired number of repetitions to test the function: "))
def measure_time(func,repeats=input_repeats):
    def wrapper():
        list_time = []
        c = 0
        for i in range(repeats):
            start = time.time()
            func()
            c += 1
            print("The function was executed "+ str(c) +" times(time)!")
            end = time.time()
            list_time.append(end - start)
        print (f"Average execution time for {input_repeats} calls(call): {round(sum(list_time) / len(list_time), 2)}")
    return wrapper



@measure_time
def compute():
    total = 0
    for i in range(100000000):
        total += i
    return total



compute()


