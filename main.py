# 5 task 03
from random import randint

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenue = [randint(90000, 100_000) for n in range(12)]
cost = [randint(10000,110_000) for n in range(12)]

def profit():
  calculate_profit = list(map(lambda x, y: x - y, revenue, cost))
  return calculate_profit
profit = profit()


def procent():
  calculate_procent = list(map(lambda x, y: (x/y)*100//1, profit, revenue)) 
  return calculate_procent
procent = procent()


nums =  procent
criteria = {50: 'great',
            25: 'decent',
            0: 'need follow up',
            -100: 'critical'
            }

words  = []

for num in nums:
  for crit in criteria:
    if num > crit:
      words.append(criteria[crit])
      break


for months, profits, procents, word in zip(month, profit, procent, words):
  print(months,':', profits, procents, '%',  '->', word)