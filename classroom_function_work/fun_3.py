def outer_arg(x, y):
    return x * y
    inner_arg()


def inner_arg(a, b):
    return a / b


print(outer_arg(1, 1) + inner_arg(2, 2))
