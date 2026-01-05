
"""Create a class User that contains username, password, counts users and checks whether password and/or password are valid"""

class User:
    total_users = 0

    def __init__(self, username, password):
        if username == "":
            raise ValueError("Username must be a non-empty string.")
        elif len(password) < 5:
            raise ValueError("Password must be at least 5 characters.")
        self.username = username
        self.password = password
        User.total_users += 1

    def __str__(self):
        return f'User: {self.username}, Password: {self.password}'

    @classmethod
    def get_total(cls):
        return cls.total_users



user1 = User("alice", "pass123")
user2 = User("bob", "secure456")


print(f"Total users: {User.get_total()}")

try:
    user1 = User("alice", "pass123")
    print(user1)  # User(username='alice')
except ValueError as e:
    print("Error:", e)

try:
    user2 = User("", "12345")  # Incorrect name
except ValueError as e:
    print("Error:", e)
try:
    user3 = User("bob", "123")  # Too short password
except ValueError as e:
    print("Error:", e)

print(f"Total users: {User.get_total()}")


# User(username='alice')
# Error: Username must be a non-empty string.
# Error: Password must be a string with at least 5 characters.
# Total users: 1

