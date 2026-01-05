"""
1. Unite any data into a string
"""

data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]

def unite(data : list) -> str:
    """
    :param data: the function gets a list with any types of data inside

    This function unites and returns at the same time all the list elements
    by using " | ".join(data)

    :return: A string representing the united list elements
    """
    if not data:
        return "The list is empty"
    newdata = [str(x) for x in data]
    return " | ".join(newdata)

print(unite(data))
"""
2. Sum of nested numbers

Example output:

Final score: 156
"""

data = [
    {"name": "Alice", "scores": [10, 20, 30]},
    {"name": "Bob", "scores": [5, 15, 25]},
    {"name": "Charlie", "scores": [7, 17, 27]}
]

def sum_grades(lst : list[dict] ) -> str:
    """
    :param lst: the function gets a list with dictionaries

    This function sums all the scores of the students by using for loop

    :return: the sum of all the scores of the students converted into string
    """
    summedscores = 0
    for j in lst:
        for i in j["scores"]:
            summedscores += i
    return "BEHOLD! The Final Score is: " + str(summedscores)
print(sum_grades(data))

