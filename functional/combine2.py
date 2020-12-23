from functools import reduce

months = [('Jan', 31), ('Feb', 28), ('Mar', 31)]

result = reduce(lambda x, y: x + y,
                map(lambda x: x[1], months))

print(result)
