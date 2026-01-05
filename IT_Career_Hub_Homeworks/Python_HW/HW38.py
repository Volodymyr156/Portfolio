""""""

"""
Create class BankAccount that contains name and balance, operates with balance, and returns the result
"""
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self.__history = []

    @property
    def history(self):
        print("Operation history:")
        return tuple(self.__history)

    def deposit(self, amount):
        if amount <= 0:
            print("Can't deposit negative or empty amount")
        else:
            self.__balance += amount
            self.__history.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Cannot withdraw more money")
        elif amount <= 0:
            print("Can't withdraw negative or empty amount")
        else:
            self.__balance -= amount
            self.__history.append(f"Withdraw: {amount}")

    def __str__(self):
        return f'{self.name}`s balance: {self.__balance}'

gachiboy = BankAccount('Gachiboy', 150)


gachiboy.deposit(2000)
gachiboy.withdraw(34)
for i in gachiboy.history:
    print("\t"+i)
print(gachiboy)