
import math
from functools import total_ordering
from datetime import datetime

#1
"""
Create Email class that contains information about sender, recipient, subject, body, date and check its functionality
"""
@total_ordering
class Email:
    def __init__(self, sender, recipient,
                 subject, body, date):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = date

    def __eq__(self, other):
        if not isinstance(other, datetime):
            return NotImplemented
        return self.date == other.date

    def __lt__(self, other):
        return self.date <= other.date

    def __bool__(self):
        return self.body.isspace() == False and self.body != ""

    def __len__(self):
        return len(self.body)

    def __repr__(self):
        return f"From: {self.sender}\nTo: {self.recipient}\nSubject: {self.subject}\nBody:\n{self.body}"


e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
e2 = Email("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))
print(e1,"\n")
print(e2)
print("Length:", len(e1))
print("Has text:", bool(e1))
print("Is newer:", e2 > e1)


#2
"""
Create Money class that operates with money, returns the result of arithmetical operations with self.amount and other.amount as another object 
"""
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.amount + other.amount)

    def __sub__(self, other):
        if self.amount < other.amount:
            return 0
        return Money(self.amount - other.amount)

    def __str__(self):
        return f"${self.amount}"


money1 = Money(100)
money2 = Money(50)
print(money1 + money2)
print(money1 - money2)

print(money2 - money1)
