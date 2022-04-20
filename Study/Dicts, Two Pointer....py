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