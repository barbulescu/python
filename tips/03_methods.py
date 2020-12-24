def example_method(
        mandatory_parameter,
        default_parameter='Default',
        *args,
        **kwargs
):
    print(f"""
mandatory_parameter = {mandatory_parameter}
default_parameter = {default_parameter}
args = {args}
kwargs = {kwargs}
""")


example_method('p1')
example_method(mandatory_parameter='p1')
example_method('p1', 'p2')
example_method('p1', 'p2', 1, 2)
example_method('p1', 'p2', 1, 2, k1='v1', k2='v2')
example_method(k1='v1', k2='v2', mandatory_parameter='p1', default_parameter='p2')

# unpacking
numbers = [1, 2, 3, 4, 5, 6]
example_method(*numbers)

d = {'a': 1, 'b': 2}
example_method(*numbers, **d)
