
# Заводим словарики
a = 123
d = {
    "key": "value",
    123: a,
    10: {"another": "first"},
    (1, 2, 3): "fafafa"
}

print(d[(1, 2, 3)])

print(d["key"])

# Функции словарей

print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

print(d.get("browser", "chrome"))
