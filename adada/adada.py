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



# # map

  

nums = [n for n in range(10)]
# # # double_n = [n * 2 for n in nums]
# # print(nums)
# # # print(double_n)

# # def doubler(x):
# #   return x * 2

# # double_numbers = list(map(doubler, nums))
# # print(double_numbers)

# # a, b = map(int, (input(), input()))
# # print(a, b)


# double_numbers = list(map(lambda x: x * 2, nums))

# print(double_numbers)


# x_list = [1, 2, 4]
# y_list = [4, 6, 8]
# z_list = [9, 10, 10]

# res = list(map(lambda x, y, z: x + y + z, x_list, y_list, z_list))
# print(res)

#filter

odd_numbers = list(filter(lambda x: x % 2, nums))
print(odd_numbers)
