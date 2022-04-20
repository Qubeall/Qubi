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