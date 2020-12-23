try:
    i = 0
    number = 10 / i
except ZeroDivisionError as error:
    print(error)
    number = 0
else:
    print('else')
finally:
    print('finally')

print(number)


class CurrenciesDoNotMatchException(Exception):
    pass


class Amount:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def add(self, other):
        if self.currency == other.currency:
            self.amount += other.amount
        else:
            raise CurrenciesDoNotMatchException('Currency does not match')

    def __repr__(self):
        return repr((self.currency, self.amount))


amount1 = Amount("EUR", 2)
amount2 = Amount("EUR", 3)
amount3 = Amount("USD", 4)

amount1.add(amount2)
print(amount1)
amount3.add(amount2)
print(amount3)
