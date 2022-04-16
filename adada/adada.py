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



# Custom Exceptions

# specifying message in arg
def example_exceptions_1(x, y):
  if y == 0:
    raise ZeroDivisionError('the dem is 0')
  elif y < 0:
    raise Exception('the dom is neg')
  else:
    print(x / y)

example_exceptions_1(10, 0)
example_exceptions_1(10, -1)


# raising with try/except
class NegativeResultException(Exception):
  pass
  
def example_exceptions_2(x, y):
  try:
    z = x / y
    if z < 0:
      raise NegativeResultException
    else:
      print(z)
  except NegativeResultException:
      print('res is negative')

example_exceptions_2(10, -1)

# raising several exceptions
class NegativeResultException(Exception):
  pass

class DenomOutOfBoundsException(Exception):
  pass
  
def example_exceptions_3(x, y):
  try:
    z = x / y
    if z < 0:
      raise NegativeResultException
    elif 1 < y < 10:
      raise DenomOutOfBoundsException
    else:
      print(z)
  except NegativeResultException:
      print('res is negative')
  except DenomOutOfBoundsException:
      print('denom can not be = from 2 to 9')

example_exceptions_3(10, -1)
example_exceptions_3(10, 4)

# by __str__ dunder
class OutOfBoundsException(Exception):
    def __str__(self):
      self.message = f'x can not be processed'
  

def example_exceptions_4(x):
    try:
        if 3 < x < 30:
            raise OutOfBoundsException
        else:
            print(x)
    except OutOfBoundsException as err:
        print(err)

example_exceptions_4(16)


# by __init__ dunder and parsing var to class
class NotInBoundException(Exception):
    def __init__(self, x):
      self.message = f'{x} can not be processed'
      super().__init__(self.message)


def example_exceptions_5(x):
    try:
        if 3 < x < 30:
            raise NotInBoundException(x)
        else:
            print(x)
    except NotInBoundException as err:
        print(err)

example_exceptions_5(10)







from time import perf_counter

# def get_primes(n):
#   primes = [2, 3]
#   for i in range(5, n + 1):
#     if i % 6 in (1, 5):
#       prime = True
#       for j in range(2, int(i ** 0.5) + 1):
#         if not i % j:
#           prime = False
#           break
#       if prime:
#         primes.append(i)
#   return primes


# n = 100_000
# start = perf_counter()
# primes = get_primes(n)
# print(perf_counter() - start)
# print(primes)


def get_prime_divs(n):
  res = []
  for i in range(2, int(n ** 0.5) + 1):
    while not n % i:
      if not i in res:
        res.append(i)
      n //= i
    if n < i:
      break
  if n > 1:
     res.append(n)
  return res

n = 999_999_999
start = perf_counter()
print(get_prime_divs(n))
print(perf_counter() - start)






# Decorator

def our_decor(func):
  def wrapper(arg_for_func):
    return func(arg_for_func), '$'
  return wrapper


@our_decor
def greet(name):
  return 90


print(greet('John'))

# string decorator 1

def my_decor1(func):
  def wrapper(arg_for_func):
    print('It is amazing see you here!')
    return func(arg_for_func)
  return wrapper


@my_decor1
def greet(name):
  return f'Hello, {name}!!'

print(greet('John'))

# string decorator2

def my_decor2(func):
  def wrapper(*args_for_func):
    return ' '.join((func(*args_for_func), 'RUB'))
  return wrapper


@my_decor2
def calculate(a, b):
  return str(a // b)

print(calculate(1000, 25))




#Random

import random
from functools import reduce


letters  = [chr(n) for n in range(65, 80)]
freqs = [n + 1 for n in range(len(letters))][::-1]
print(letters)
print(freqs)


print(random.choices(letters, freqs))

password = [random.choices(letters, freqs) for _ in range(6)]
print(password)

print(''.join(reduce(lambda a, b: a + b, password)))




















