""""""
from datetime import datetime
"""
Create a function, make_rounder(), that accepts the number of digits to round to and returns another function.
The resulting function should accept a number and return it rounded to the specified number of decimal places.
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
Create a function that returns a nested event logger.
Each logger call should store the event with the current time (if passed) and return the entire list of events.
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
Create a frame decorator that wraps the function's result in a 50-character frame - outputting one line before and one line after the function call.
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




