from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, joining_year):
        self.name = name
        self.joining_year = joining_year

    def years_on_platform(self, current_year):
        return current_year - self.joining_year

    @abstractmethod
    def role(self):
        pass

    def __str__(self):
        return f"User: {self.name}, Role: {self.role()}, Joined: {self.joining_year}"


class Customer(User):
    def role(self):
        return "Customer"


class Vendor(User):
    def role(self):
        return "Vendor"


if __name__ == "__main__":
    current_year = 2025
    user1 = Customer("Alice", 2018)
    user2 = Vendor("Bob", 2016)

    print(f"{user1}, Years on Platform: {user1.years_on_platform(current_year)}")
    print(f"{user2}, Years on Platform: {user2.years_on_platform(current_year)}")
