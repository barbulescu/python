def multiple_by_2(data):
    return data * 2


def do_this_and_print(func, data):
    print(func(data))


do_this_and_print(multiple_by_2, 125)

func_reference = multiple_by_2

print(func_reference(23))
