#1
"""
Delete all list elements with spaces
"""
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]

for j in text_list:
    indx = text_list.index(j)
    if " " in j:
        text_list.remove(j)
    text_list[indx] = text_list[indx].lower()

print(text_list)
#2
"""
Ask the user to input a discount and output all products with old and new prices
"""
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
disc = int(input("Enter the discount (as a percentage): ")) / 100
print("Product","\t","Old price","\t","New price")

for j in products:
    print(f"{j[0]:<10}",f"{str(j[1])+"$":<10}",f"{str(j[1] - (j[1] * disc))+"$":>10}")

# HW 16
# 1
"""
Create nested lists with a description of a grade
"""
grades = [5, 3, 4, 2, 1, 5, 3]

for j in grades:
    indx2 = grades.index(j)
    if j == 5:
        grades[indx2] = [5,"Very well"]
    elif j == 3 or j == 4:
        grades[indx2] = [j,"Good"]
    elif j <= 2:
        grades[indx2] = [j,"Bad! Booooooo!"]


print(grades)
#2

"""
Check whether parentheses are correctly written
"""
string = "([{}])"
pars = []
for j in string:
    if j == "(" or j == "[" or j == "{":
        pars.append(j)
    elif j == ")" or j == "]" or j == "}":
        if not pars:
            break
        pars.pop()
if not pars:
    print("Valid: True")
else:
    print("Valid: False")

#HW 17

"""
check whether set2 is a subset of set1
"""
set1 = {1, 2, 3, 4}

set2 = {2,3}

if set2 & set1 != set():
    print("Amazing")
else:
    print("Damn it...")

print(set2.issubset(set1)) #shorter variant

#2
"""
check whether set4 is a subset of set3 and print the difference
"""
set3 = {2, 3,32,32,122,4, 5, 6}

set4 = {2,3}

if set4 & set3 != set():
    print("Is subset: True")
    print("Difference {set3.difference(set4)}: ",set3.difference(set4))
else:
    print("Is subset:False")

# HW 18

#1
"""
Create a new list with unique numbers and sort it in reverse order
"""
numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]
nums = []
for j in numbers:
    if numbers.count(j) > 1 and j not in nums:
        nums.append(j)
print(sorted(nums, reverse=True))


#2
"""
check whether dict2 has elements of dict1 and return True/False
"""
dict1 = {"a": 1, "b": 2}

dict2 = {"a": 1, "b": 2, "c": 3}

answer = None
for j in list(dict1.items()):
    if j in list(dict2.items()):
        answer = True
print("What is the answer?: ",answer)












