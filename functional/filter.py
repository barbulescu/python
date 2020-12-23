numbers = [1, 89, 54, 35]

odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))
print(odd_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

words = ['Apple', 'Ant', 'Bat']
words_ending_in_at = list(filter(lambda x: x.endswith('at'), words))
print(words_ending_in_at)
