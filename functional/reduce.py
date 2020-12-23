from functools import reduce

numbers = [3, 15, 12, 10]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)

words = ['Apple', 'Ant', 'Bat']
print(reduce(lambda x, y: x if len(x) > len(y) else y, words))
