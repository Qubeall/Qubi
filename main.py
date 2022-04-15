# 4 task 03
from random import randint


names = ['Денис', 'Дима0', 'Ваня', 'Дима1', 'Дима2', 'Лёша', 'Вова', 'Вадим', 'Богда', 'Юра', 'Антон', 'Артём', 'Костя']
names.sort()

math = [randint(25, 50) for _ in range(len(names))]

eng = [randint(25,50) for _ in range(len(names))]

phys = [randint(25,50) for _ in range(len(names))]

res = list(map(lambda x, y, z: x + y + z, math, eng, phys))


enroll = []
dont_pass = []
for name, mark in zip(names, res):
  if mark > 100:
    enroll.append(name)
    enroll.append(mark)
  

print(f'You are admitted: {enroll}')
print(30*'=')

for name, mark in zip(names, res):
  if mark < 100:
    dont_pass.append(name)

print(f'You are don\'t pass:{dont_pass}')