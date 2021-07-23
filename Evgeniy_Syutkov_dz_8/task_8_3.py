from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        nums_list = [el for el in (*args, *kwargs.values())]
        n = [f'{func.__name__}({el}: {type(el)})' for el in nums_list]
        print(*n, *func(*args, **kwargs), sep=', ')

    return wrapper


@type_logger
def calc_cube(*x, **y):
    nums_list = [el for el in (*x, *y.values()) if isinstance(el, int) or isinstance(el, float)]
    return [i ** 3 for i in nums_list]


calc_cube(5, 8.5, [5, 7], el=15, name='Petr')
print(calc_cube.__name__)
