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





from time import perf_counter

def get_primes(n):
 primes = [2, 3]
 for i in range(5, n + 1):
   if i % 6 in (1, 5):
     prime = True
     for j in range(2, int(i ** 0.5) + 1):
       if not i % j:
         prime = False
         break
   if prime: 
      primes.append(i)
 return primes


n = 100_000
start = perf_counter()
primes = get_primes(n)
print(perf_counter() - start)
print(primes)


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









# DAY 7

# -> Two Pointer in Python
# -> Binary Tasks
# -> Default Dict and Counter


# text = 'I\'ve become so numb \
# I can\'t feel you there \
# Become so tired \
# So much more aware'


lst = [1, 3, 6, 8, 9, 12, 13, 19]
num = 0
k = 1
for i in range(len(lst)):
  for j in range(i, len(lst)):
    if lst[j] - lst[i] >= 3:
      num += 1
      print(lst[i], lst[j])
      k += 1

print(num, k)

 # Двойной указатель
i = j = 0
num = 0
k = 1
while i < len(lst) and j < len(lst):
  if lst[j] - lst[i] < 3:
    j += 1
  else:
    num += len(lst) - j
    i += 1
  k += 1
print(num, k)




# Default Dict and Counter

text = '''I've become so numb
I can't feel you there
Become so tired
So much more aware
I'm becoming this
All I want to do
Is be more like me
And be less like you
And I know
I may end up failing too
But I know
You were just like me with someone disappointed in you'''

text_list = text.split()

# setdefault
freq_dict = {}
for word in text_list:
  freq_dict.setdefault(word, 0)
  freq_dict[word] += 1

print(freq_dict)
print(freq_dict['AAAAAAAAA'])  # KeyError / Not Added

index_dict = {}
for index, word in enumerate(text_list):
  index_dict.setdefault(word, []).append(index)

print(index_dict)

# default dict
from collections import defaultdict

freq_ddict = defaultdict(int)

for word in text_list:
  freq_ddict[word] += 1

print(freq_ddict)
print(freq_ddict['AAAAAAAAA'])  # No Error / Missing value is added
print(freq_ddict)  # See it added to Dict
  
freq_dict = defaultdict(list)

# Counter
from collections import Counter

freq_counter = Counter(text_list)

print(freq_counter)  # use it like normal dict
print(freq_counter.most_common)
print(freq_counter.most_common(2))
    
    



#Dictionary reverse
my_dict = {
  1: 'a',
  2: 'b'
}

print(my_dict.items())

rev_dict = {v: k for k, v in my_dict.items()}
print(rev_dict)



stock = [[2, 1], [2, 3]]

weights = {
  0: 7,
  1: 8
}

max_value = max(weights.values())
print(max_value)

rev_weights = {v: k for k, v in weights.items()}

max_key = stock[rev_weights[max_value]]
print(max_key)



my_dict = {
  'a': 5, 
  'b': 8,
  'c': 10
}

print([k for k, _ in my_dict.items()][:2])







#READ

with open('passwords.txt', 'r', encoding='utf-8') as file:
  print(file.read(4)) #  read 4 bytes
  print(file.read())  #  read all/rest of bytes in fileif read before like above

with open('passwords.txt', 'r', encoding='utf-8') as file:
  print(file.readline(5)) #  read 5 bytes
  print(file.readline())  #  read all/rest of bytes in line if read before like above

with open('passwords.txt', 'r', encoding='utf-8') as file:
  print(file.readlines()) #  returns list
  
with open('passwords.txt', 'r', encoding='utf-8') as file:
  for line in file:
    print(line) #  returns line + \n
    print(line.strip()) #  returns line stripped from \s\n\t etc.


#WRITE
with open('checked.txt', 'w', encoding='utf-8') as file:
  file.write('new entry - check')
  file.write('NEW new entry - check')  # re-writes the line above

with open('checked.txt', 'a', encoding='utf-8') as file:
  file.write('new entry - check')
  file.write('NEW new entry - check')  # appends the line to existing contents

checked = ['this', 'that', 'that over there']
with open('checked.txt', 'w', encoding='utf-8') as file:
  for check in checked:
    file.write(check + '\n')  # writes all in the list each on new line

checked = ['this\n', 'that\n', 'that over there\n']
with open('checked.txt', 'w', encoding='utf-8') as file:
    file.writelines(checked)  # writes all in the list each on new line





# DAY 9
# -> Start Hacker project
# -> Socket Module
# -> Custom Generators


'hello'.encode()
data = data.decode()

import socket


with socket.socket() as client_socket:

  hostname = '127.0.0.1'
  port = 5000
  
  client_socket.connect((hostname, port))
  
  data = 'Wake up Neo'
  
  client_socket.send(data.encode())
  
  buffer = 1024
  response = client_socket.recv(buffer)
  response = response.decode()
  
  print(response)

import socket

# 2 Вариант
with socket.socket() as client_socket:

  hostname = '127.0.0.1'  # str
  port = 5000  # int

  address = (hostname, port)
  
  client_socket.connect(address)  # one arg!!
  
  data = 'This is my test string'
  
  client_socket.send(data.encode())  # converting to bytes
  
  buffer = 1024  # response limit
  response = client_socket.recv(buffer)
  response = response.decode()  # converting back to rea

  print(response)
