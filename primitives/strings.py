
# Учимся писать строки!

s = "i am 'teapot'!"

multiline_string = """first
second
third"""

print(multiline_string)

# Сырые строки
print(r"this is stri\ng")

# Индексы и слайсы

alphabet = "abcdefg"


# Оперируем


# Форматируем

first = "first"
second = "second"
third = "third"

print(f"{first} {second} {third.title()} {100}")
print("{2} {1} {0}".format(first, second, third.title()))
print("%s %s %s" % (first, second, third.title()))

# Строку в число, и наоборот
