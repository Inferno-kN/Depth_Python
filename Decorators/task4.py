def trace(func):

    def wrapper(*args, **kwargs):

        print(f"Вход в функцию {func.__name__} c аргументами {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Выход из функции {func.__name__} с результатом {result}")

        return result
    return wrapper


@trace
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial(3)

