from true_math import divide as tm
from fake_math import divide as fm


result1 = tm(12, 2)
result2 = tm(12, 0)
result3 = fm(24, 12)
result4 = fm(24, 0)

print(result1)
print(result2)
print(result3)
print(result4)