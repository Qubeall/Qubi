# 5 task 03
from random import randint

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenue = [randint(90000, 100_000) for n in range(12)]
cost = [randint(10000,110_000) for n in range(12)]

def profit():
  calculate_profit = list(map(lambda x, y: x - y, revenue, cost))
  return calculate_profit

profit = profit()
print(profit)

difference_of_profits = ['over 50 %','25% - 50%', '0% - 25%', 'less than 0%']
wording = ['great', 'decent', 'need follow up', ' critical']
  

def procent():
  calculate_procent = list(map(lambda x: x - y , profit, )) 
  return calculate_procent

procent = procent()
print(procent)


great = wording[0]
decent = wording[1]
need_follow_up = wording[2]
critical = wording[3]


 
    





for months, profits, procents in zip(month, profit, procent):
  print(months, profits, procents,'%')