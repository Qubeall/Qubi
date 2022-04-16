# 5 task 03
from random import randint

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

revenue = [randint(90000, 100_000) for n in range(12)]
print(revenue)

cost = [randint(50000,60000) for n in range(12)]
print(cost)

profit