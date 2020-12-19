
def print_squares_of_numbers_up_to(limit):
    for i in range(1, limit + 1):
        print(i * i)


def print_squares_of_even_numbers_up_to(limit):
    for i in range(2, limit + 1, 2):
        print(i * i)


def print_numbers_in_reverse(limit):
    for i in range(limit, 0, -1):
        print(i)


print_squares_of_numbers_up_to(10)
print()
print_squares_of_even_numbers_up_to(10)
print()
print_numbers_in_reverse(10)
