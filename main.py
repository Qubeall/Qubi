# 4 task 04

inputs =  [1, 2, 3, 4, 5]

a = list(map(lambda x: x * 10, inputs))
b = inputs * 10
c = [10 * x for x in inputs]

if a == c:
  print('a and c perform the same task')
if a == b:
  print('a and b perform the same task')
if b == c:
  print('b and c perform the same task')
  
  

