# 4 task 02
nums = [n for n in range(5)]
even = list(map(lambda x: x * 2, nums))

odd = [1, 3, 5, 7, 9]

length = len(even)

my_sum = []
i = 0
while i < length:
    my_sum.append(even[i] + odd[i])
    i = i + 1

remainders = list(map(lambda x: x % 3, my_sum))

onzero_remainders = list(filter(lambda x: x % 3, remainders))

print(my_sum)
print(remainders)
print(onzero_remainders)



