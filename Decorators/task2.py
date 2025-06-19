def type_check(*types):

    def decorator(func):

        def wrapper(*args, **kwargs):

            for i in range(len(args)):
                if not isinstance(args[i], types[i]):
                    raise TypeError(f"Неверный тип аргумента {func.__code__.co_varnames[i]}. Ожидался {types[i]} получен {type(args[i])}")

                return func(*args, **kwargs)

        return wrapper

    return decorator

@type_check(int, int)
def add(a, b):
    return a + b

print(add(2, 3))
print(add(2, '3'))