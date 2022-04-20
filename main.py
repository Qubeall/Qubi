# 9 task 01
print('Programm will display "Exception: Something went wrong!"')


a = -2
b = 10
c = a / b

if c >= 0:
    print(c)
else:
    raise Exception('Something went wrong!')