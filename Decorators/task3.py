def validate_range(min_value, max_value):

    def decorator(func):

        def wrapper(*args, **kwargs):

            for elem in args:
                if not isinstance(elem, int or float):
                    raise TypeError
                if elem < min_value or elem > max_value:
                    raise ValueError (f'Аргумент \'value\' имеет значение {elem}, что выходит за пределы {min_value}, {max_value}')

            return func(*args, **kwargs)

        return wrapper

    return decorator

@validate_range(min_value=0, max_value=100)
def set_percentage(value):
    print(f"Установлено значение: {value}%")

set_percentage(50)     # Вывод: Установлено значение: 50%
set_percentage(150)    # ValueError: Аргумент 'value' имеет значение 150, что выходит за пределы [0, 100]