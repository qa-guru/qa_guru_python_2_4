
# Объявляем функции и аргументы


# Возвращаем значение


# Переменное количество аргументов


def print_all_arguments(*args):
    for arg in args:
        print(arg)


print_all_arguments(1, 2, 3, 4, 5, 6, 7, 8)


def print_all_arguments(end, *args):
    for arg in args:
        print(arg, end=end)


print_all_arguments("", 2, 3, 4, 5, 6, 7, 8)


def print_all_arguments(*args, end="\n"):
    for arg in args:
        print(arg, end=end)


def print_all_arguments_v2(*args, end="\n"):
    print(*args, end=end)


print_all_arguments(2, 3, 4, 5, 6, 7, 8, end="")
print()
print_all_arguments_v2(2, 3, 4, 5, 6, 7, 8, end="\n")


# Переменное количество возвращаемых значений

def f():
    return 1, 2, 3

# Функция - тоже объект
