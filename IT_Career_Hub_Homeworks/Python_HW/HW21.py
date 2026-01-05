""" 01 Count characters of a string

Implement a function that
- takes text
- and returns a dictionary counting the number of each letter, ignoring case.

The data:
text = "Programming is fun!"
The output example:
{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}
"""

from collections import Counter

def char_count(text):
        t = text.lower()
        chars = Counter(t)
        for k in list(chars):
            if k in "! ":
                del chars[k]
        return chars
text = "Programming is fun!"
sample = {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}


print(char_count(text))
print(char_count(text) == sample)

"""02 Group students by class

Create a function to group students by class.
Add students to the appropriate groups.

The data:
students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]

The output:
{'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}
"""

from collections import defaultdict

def get_students_groups(students):
    newdict = defaultdict(list)
    for student in students:
        newdict[student[0]].append(student[1])
    return newdict

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]
sample = {'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}




print(get_students_groups(students))

print(get_students_groups(students) == sample)
