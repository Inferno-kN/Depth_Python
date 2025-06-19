def count_calls(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Функция {func.__name__} вызвана {count} раз")
        return func(*args, **kwargs)
    return wrapper

@count_calls
def greet(name):
    print(f"Привет, {name}!")

greet("Алексей")
greet("Мария")



