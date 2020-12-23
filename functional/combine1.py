from functools import reduce

numbers = [3, 7, 8, 15, 24, 35, 46]

result = reduce(lambda x, y: x + y,
                map(lambda x: x * x,
                    filter(lambda x: x % 2 == 0, numbers)))

print(result)