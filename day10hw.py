from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year

    def account_age(self):
        current_year = 2025
        return current_year - self.account_year

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Admin(User):
    def get_role(self):
        return "Admin"

    def __str__(self):
        return f"Admin User: {self.name}, Account Age: {self.account_age()} years"


class Guest(User):
    def get_role(self):
        return "Guest"

    def __str__(self):
        return f"Guest User: {self.name}, Account Age: {self.account_age()} years"



if __name__ == "__main__":
    admin = Admin("Alice", 2018)
    guest = Guest("Bob", 2022)

    print("Role:", admin.get_role())
    print("Account Age:", admin.account_age())
    print(admin)  

    print()

    print("Role:", guest.get_role())
    print("Account Age:", guest.account_age())
    print(guest)   
