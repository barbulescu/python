def print_multiplication_table(table=5, start=1, end=10):
    for i in range(start, end + 1):
        print(f"{table} X {i} = {table * i}")


print_multiplication_table()
