# 4 task 07

list_1 = [i for i in range(0,10)]
list_2 = [i for i in range(10, 20)]

def my_product():
 res = list(map(lambda x, y: x * y ,list_1, list_2, ))
 return res
print(my_product())
