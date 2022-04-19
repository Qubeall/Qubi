# 6 task 01


from math import ceil, sqrt

def get_all_dividers(num):

    first_half_dividers = [x for x in range(1, ceil(sqrt(num)) + 1)
                           if num % x == 0]

    second_half_dividers = [int(num / x) for x in reversed(first_half_dividers)
                            if int(num / x) not in first_half_dividers]

    return first_half_dividers + second_half_dividers

print(get_all_dividers(1000)) 

