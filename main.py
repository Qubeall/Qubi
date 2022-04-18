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
  calculate_procent = list(map(lambda x: (x[0] - x[1]) // x[0], profit)) 
  return calculate_procent

procent = procent()


nums =  [51, 45, 20, -1]

criteria = {50: 'great',
            24: 'decent',
            -1: 'need follow up',
            -2: 'critical'
            
}

words  = []

for num in nums:
  for crit in criteria:
    if num > crit:
      words.append(criteria[crit])
      break





for months, profits, procents, word in zip(month, profit, procent, words):
  print(months, profits, procents,'%', word)


  #jan 1000 --
  #feb 1500 +50% (1500 - 1000 / 1000)
  #mar 2250 +50% (2250 - 1500 / 1500)






