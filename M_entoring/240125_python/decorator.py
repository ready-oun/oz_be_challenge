def log_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@log_decorator
def plus(x, y):
    return x + y


@log_decorator
def minus(x, y):
    return x - y
#
# numbers = [
#     [1, 2], [3, 4], [5,6]
# ]
#
# for n in numbers:
#     plus(*n)
#     plus(n[0], n[1])


k_numbers = [
    {'x': 1, 'y': 2}, {'x': 5, 'y':7}
]

for numbers in k_numbers:
    plus(**numbers)
    plus(x=numbers['x'], y=numbers['y'])
