def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


for j in range(1, 20):
    prime = is_prime(j)
    if prime:
        print(f"is_prime({j}) -> {prime}")

print()
print("=============================")
print()


def sum_upto(number):
    total = 0
    for i in range(1, number):
        total += i
    return total


print(f"sum_upto: {sum_upto(10)}")

print()
print("=============================")
print()


def sum_of_divisors(number):
    total = 0
    for i in range(2, number):
        if number % i == 0:
            total += i
    return total


print(f"sum_of_divisor: {sum_of_divisors(10)}")

print()
print("=============================")
print()


def print_number_triangle(number):
    for i in range(1, number + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


print_number_triangle(5)
