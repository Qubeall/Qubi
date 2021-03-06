# % foramatting
print('%.3f' % (11 /  3))
name = 'Mary'; age = 15
print('Hi %s you are %d' % (name, age))

# .format()
print('{} {} {}'.format('Me', 'and', 'You'))
print('{who} {} {}'.format('Me', 'and', who='You'))
print('{who} {} {}'.format('Me', 'and', who='You'))
print('{2} {1} {0}'.format('Me', 'and', 'You'))

# f'{var]'
a = 5
print(f'%.{a}f' % (11 /  3))
name = 'Jonny Cage'
print(f'This is the end of you, {name}')
#adadada
nums = [n * 2 for n in range(1, 21)]
print(nums)
print(nums[2:7])

str1 = 'Python is not just a mere snake'
print(str1[10:18])

print(str1[::-1])
print(str1[7::])

new_str = str1[:]
print(new_str)

my_list = ['Java', 'Python', 'Kotlin']
print(my_list[:2])
print(my_list[:99999999])    

# !!NEVER DO THIS
def my_func(a, lst=[]):
  pass

# +DO THIS
def my_func(a):
  lst = []

# Linear and Binary Search
# Big O
# sorted and unsorted array

from random import randint
lst = [randint(0, 10) for _ in range(10)]
lst.sort()
print(lst)
mx = 0
for n in lst:
  if n > mx:
    mx = n

print(mx)








# map / takes a func

# -----------
nums = [n for n in range(10)]
double_nums = [n * 2 for n in nums]
print(nums)
print(double_nums)

# -----------
def doubler(x):
  return x * 2

double_numbers = list(map(doubler, nums))
print(double_numbers)

# -----------
a, b = map(int, (input(), input()))
print(a, type(a), b, type(b))

# -----------
double_numbers = list(map(lambda x: x * 2, nums))
print(double_numbers)

# -----------
x_list = [1, 2, 4]
y_list = [4, 6, 8]
z_list = [9, 10, 10]

res = list(map(lambda x, y, z: x + y + z, x_list, y_list, z_list))
print(res)


#filter / takes a Boolean func (True or False)
odd_numbers = [n for n in nums if n % 2]
print(odd_numbers)

# -----------
odd_numbers = list(filter(lambda x: x % 2, nums))
print(odd_numbers)

#--------------------------------------------------
# map and filter can be replaced with list comprehention
# which is more PYTHONIC yet
# map and filter are generally more efficient and faster








# iterators

# iterators use dunders __iter()__ & __next()__

my_list = [1, 2, 3]
my_iter = iter(my_list)  # turn list to generator
print(my_iter)
print(next(my_iter))  # get intance in generator
print(next(my_iter))  # get next intance in generator till error

for a in my_list:  # same concept
  print(a)


# zip

names = ['Mary', 'Ann']
surnames = ['Smith', 'Boul']
for name, surname in zip(names, surnames):
  print(name, surname)

names = ['Mary', 'Ann', 'Bob']
surnames = ['Smith', 'Boul']
for name, surname in zip(names, surnames):  # stops at shortest
  print(name, surname)

# from python 3.10 you can make sure lists are identical in length
names = ['Mary', 'Ann', 'Bob']
surnames = ['Smith', 'Boul']
for name, surname in zip(names, surnames, strict=True):  # throws error
  print(name, surname)
  
# enumerate
  
names = ['Mary', 'Ann', 'Bob']

i = 1
for name in names:
  print(i, name)

for i, name in enumerate(names):
  print(i + 1, name)
# or
for i, name in enumerate(names, start=1):
  print(i, name)










print('Hello')
print(10 / 0)  # code goes till first exception

# typical

# NameError
a = 5; print(a + b)  # b is not defined before call

# TypeError
print('15' + 2)  # operation or func is applied to OBJ of wrong type

# ValueError
print(int('five'))  # OBJ type is ok but value inappropriate

# PYTHON exception tree
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning
#            +-- EncodingWarning
#            +-- ResourceWarning

#NOTE!!

# if using parent name it will cover ALL exception in it
# so 
# RuntimeError will include both exceptions in it






from time import perf_counter

nums = [n for n in range(10000)]
i = 0

start = perf_counter()
for n in nums:
  
  if n % 6 == 1 or n % 6 == 5:
    print(n, 'possible prime')
    i += 1
print(i)
print(perf_counter() - start, 'secs')
  # else:
  #   print(n, 'not prime')












# Handling Exceptions

# list
# https://docs.python.org/3/library/exceptions.html

a = 5
b = 2

print(a / b)  # work as expected


a = 5
b = 0

print(a / b)  # ZeroDivision

# solution
try:
  result = a / b
except ZeroDivisionError as err:
  print('0 Error', err)  # err is exception description
else:
  print('The result is ', result)
finally:
  print("Thank you for using the service")

  
a = 5
b = 'five'

print(a / b)  # TypeError

# solution
try:
  result = a / b
except ZeroDivisionError as err:
  print('0 Error', err)  # err is exception description
except TypeError as err:
  print('T Error', err)  # err is exception description
else:
  print('The result is ', result)
finally:
  print("Thank you for using the service")

# line num of exception
import sys 
e_type, e_object, e_traceback = sys.exc_info()
e_line = e_traceback.tb_lineno


# exception name
# use __class__.__name__ called on err object

# multiple exceptions
# except (ZeroDivisionError, TypeError) as err:

