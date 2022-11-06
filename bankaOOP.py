
from typing import List


class Person:
    def __init__(self,
                 person_id: int,
                 name: str,
                 age: int,
                 accounts: List['Account']):  # '' protože typ bude definován
        # TODO dokončit konstruktor
        self.person_id: int = person_id
        self.name: str = name
        self.age: int = age
        self.accounts: List['Account'] = accounts

    # TODO: doplňte zbytek funkcionality
    def check_integrity(self) -> bool:    
        if self.age is None or self.age < 18:
            return False
        if self.name is None or self.name == '':
            return False
        if self.accounts is None:
            return False
        for account in self.accounts:
                if account is None or account.owner is None or account.owner.person_id != self.person_id:
                    return False
        return True

class Account:
    def __init__(self,
                 account_id: int,
                 password: str,
                 balance: int,
                 limit: int,
                 owner: Person):
        # TODO dokončit konstruktor
        self.account_id: int = account_id
        self.password: str = password
        self.balance: int = balance
        self.limit: int = limit
        self.owner: Person = owner

    def add_balance(self, password: str, amount: int) -> bool:
        if self.password != password or 100000<amount:
            print('zle heslo alebo prekroceny limit')
            return False
        self.balance += amount
        return True
    def withdraw_balance(self, password: str, amount: int) -> bool:
        if self.password != password or amount > 100000 or amount > self.balance:
            return False
        self.balance -= amount
        return True

    def set_limit(self, password: str, new_limit) -> bool:
        if self.password != password:
            return False
        self.limit = new_limit
        return True

    def total_remaining(self) -> int:
        return self.balance
