def do_this_and_print(func, data):
    print(func(data))


do_this_and_print(lambda data: data * 3, 125)
do_this_and_print(lambda data: data * data, 125)
