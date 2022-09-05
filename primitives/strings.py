
# Учимся писать строки!

s = "i am 'teapot'!"
s = 'i am \'teapot\'!'
s = """i ""am"" 'teapot'!"""
s = '''i """am""" 'teapot'!'''

multiline_string = """first
second
third"""

multiline_string = "first\nsecond\nthird"
print(multiline_string)

s = "first" + "second"

# Сырые строки
print(r"this is stri\ng")

# Индексы и слайсы

alphabet = "abcdefg"
alphabet[3]
alphabet[2:5]
alphabet[0:5:2]
alphabet[::-1]


# Оперируем


# Форматируем

first = "first"
second = "second"
third = "third"
n = 100

print(f"{first} {second} {third.title()} {n}")
print("{third} {1} {0}".format(first, second, third=third.title()))
print("%s %s %s" % (first, second, third.title()))

# Строку в число, и наоборот

str(52132)
int("1241241")
