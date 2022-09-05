# Списки, словари и множества - изменяемые!
import copy

l = [1, 2, 3, ["abc", "def"]]
l2 = copy.deepcopy(l)

l2[0] = 10
l2[3][0] = "fake"

# Кортежи, frozenset  - нет

t = (1, 2, 3, 4, 5)
tt = t
