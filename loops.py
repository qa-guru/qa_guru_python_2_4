
# While

i = 0

while i < 10:
    # print("hello! " + str(i))
    # i = i + 1
    i += 1

# For. Итерируем списки и словари

for i in range(5, 20, 3):
    print(f"hello {i}")


for element in [1, "two", "three"]:
    print(element)

for i, element in enumerate([1, "two", "three"]):
    print(i, element)

for key, value in {"first": 1, "second": 2}.items():
    print(f"В ключе {key} содержится значение {value}")
