# 4 task 08

my_list = [i for i in range(-10,11)]

def find_positive(my_list):
   return my_list > 0

positive = list(filter(find_positive, my_list))

print(positive)
        


