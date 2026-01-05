""" 01 

You have a list of orders.
Each order contains a product name and price.
Write a function that:
- Selects orders over 500.
- Creates a list of the names of the selected products in alphabetical order.
- Returns the final list of names.

The data:
orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]

Example of an output:
['Chair', 'Laptop']

"""
orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]

sample = ['Chair', 'Laptop',]


def select_expensive_orders(ords):
    lst = []
    for j in orders:
        if j["price"] > 500:
            lst.append(j["product"])
    return  sorted(lst, key=lambda x: ord(x[0]))


result = select_expensive_orders(orders)
print(result)
print(result == sample)

""" 02 Sales Statistics

Given a two-dimensional array of sales (a list of tuples): (product, quantity, price).

Write a program that:
-Calculates the total revenue for each product.
-Returns a dictionary of products {product: revenue},
 sorted by descending revenue.
 
The data:
sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]

An output example:
{'Chair': 16000, 'Laptop': 6000, 'Monitor': 3000, 'Keyboard': 1500, 'Mouse': 1000}

"""

sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]

sample = {'Chair': 16000, 'Laptop': 6000, 'Monitor': 3000, 'Keyboard': 1500, 'Mouse': 1000}


def calculate_sales(sales):
    dict_ = {}
    for j in sales:
        dict_[j[0]] = j[1] * j[2]
    return dict(sorted(dict_.items(), key=lambda x: -x[1]))


result = calculate_sales(sales)
print(result)

print(str(result) == str(sample))
