# 4 task 01
from string import ascii_lowercase
from random import choice
from random import randint
lst = []
new_list = []
for _ in range(randint(1, len(ascii_lowercase))):
  lst.append(choice(ascii_lowercase))
for _ in range(randint(1,len('aiueo'))):
  new_list.append(choice('aiueo'))
print(new_list)


  