from enum import Enum


class Currency(Enum):
    USD = 1
    EUR = 2
    RON = 3


for currency in Currency:
    print(f'{currency.name} -> {currency.value}')
