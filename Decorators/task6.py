def call_limit(max_calls):

    def decorator(func):
        count = 0

        def wrapper(*args, **kwargs):

            nonlocal count
            if count > max_calls:
                raise RuntimeError(f"Превышено максимальное к-во вызова функции")

            count += 1
            func(*args, **kwargs)

        return wrapper

    return decorator


@call_limit(max_calls=3)
def print_message(msg):
    print(msg)

print_message("Первый вызов")    # Вывод: Первый вызов
print_message("Второй вызов")    # Вывод: Второй вызов
print_message("Третий вызов")    # Вывод: Третий вызов
print_message("Четвертый вызов") # RuntimeError: Превышено максимальное количество вызовов функции '

