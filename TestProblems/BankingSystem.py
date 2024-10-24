import abc
from abc import ABC

class Account(ABC):
    def __init__(self, acc_number: int, acc_balance: float, acc_type: str):
        self.acc_number = acc_number
        self.acc_balance = acc_balance
        self.acc_type = acc_type

    @abc.abstractmethod
    def deposit(self, amount: float) -> None:
        ...

    @abc.abstractmethod
    def withdraw(self, amount: float) -> None:
        ...

    @abc.abstractmethod
    def transfer(self, destination: "Account", amount: float) -> None:
        ...

    @abc.abstractmethod
    def show_balance(self) -> None:
        ...

    @abc.abstractmethod
    def get_account_type(self, acc_type: str) -> str:
        ...

    def set_acc_number(self, new_number: int) -> None:
        if type(new_number) != int:
            raise TypeError("Account number type must be 'Int'!")
        self.acc_number = new_number

    def get_acc_number(self) -> int:
        return self.acc_number

    def set_acc_balance(self, amount: float) -> None:
        if type(amount) != float:
            raise TypeError("Balance type must be 'Float'!")
        self.acc_balance = amount

    def get_acc_balance(self) -> float:
        return self.acc_balance

class Transaction():
    def depo(amount: float, balance: float) -> float:
        if isinstance(amount, (int, float)):
            amount = float(amount)
            if amount <= 0:
                raise ValueError("The deposit amount cannot be less than or equal to 0")
            else:
                return balance + amount
        else:
            raise TypeError("The deposit amount type must be float")

    def draw(amount: float, balance: float, overdraft_limit: float=0.0) -> float:
        if isinstance(amount, (int, float)):
            amount = float(amount)
            if amount <= 0:
                raise ValueError("The withdraw amount cannot be less than or equal to 0")
            elif balance - amount < -overdraft_limit:
                raise ValueError("Overdraft limit exceeded")
            else:
                return balance - amount
        else:
            raise TypeError("The withdraw amount type must be float")


class CheckingAccount(Account):
    def __init__(self, acc_number: int, overdraft_limit: float, acc_balance: float, acc_type: str = "Checking Account" ):
        super().__init__(acc_number, acc_balance, acc_type)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount: float) -> None:
        self.set_acc_balance(Transaction.depo(amount, self.get_acc_balance()))

    def withdraw(self, amount: float) -> None:
        self.set_acc_balance(Transaction.draw(amount, self.get_acc_balance(), self.overdraft_limit))

    def transfer(self, destination: "Account", amount: float) -> None:
        self.set_acc_balance(Transaction.draw(amount, self.get_acc_balance(), self.overdraft_limit))
        destination.set_acc_balance(Transaction.depo(amount, destination.get_acc_balance()))

    def show_balance(self) -> None:
        print(self.get_acc_balance())

    def get_account_type(self, acc_type: str) -> str:
        return acc_type


# c = CheckingAccount(12, 0, 0)
#
# c.deposit(100.00)
# c.withdraw(25)
# c.show_balance()





