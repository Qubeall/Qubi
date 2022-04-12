# task 5 slice
e = str(input('Enter your Email:'))

if '@' in e:
  a = e.split('@')[0]
else:
  print('Wrong Email')
if '.' in e:
  a = e.split('@') [0]
else:
  print('Wrong Email')
print(a)
