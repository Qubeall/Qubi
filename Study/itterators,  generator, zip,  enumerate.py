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






# generators

def multiples(a, n):
  i = 1
  result = []
  while i <= n:
    result.append(a * i)
    i += 1
  return result  # list


print(multiples(3, 5))  # gives whole list
print(multiples(2, 10))  # # gives whole list


def multiples(a, n):
  i = 1
  while i <= n:
    yield a * i  # yield is used instead of return to make results one by one
    i += 1

my_gen = multiples(3, 5)  # generator object
print(next(my_gen))  # gives 1st result
print(next(my_gen))  # gives 2nd result
print(next(my_gen))  # gives 3d result


numbers = [1, 2, 3]
my_generator = (n ** 2 for n in numbers)  # generator object
print(next(my_generator))  # gives 1st result
print(next(my_generator))  # gives 2nd result
print(next(my_generator))  # gives 3d result
print(next(my_generator))  # StopIteration Exception

for n in my_generator:  # can be used with for loop 
  print(n)