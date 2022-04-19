#5 task 04



print('Введите 3 числa для первого вектора:')
x = (int(input()))
y = (int(input()))
z = (int(input()))
     
v1 = (x, y ,z)


print('Введите 3 числа для второго векотра:')
a = (int(input()))
b = (int(input()))
c = (int(input()))

v2 = (a, b, c)



print('v1 =', v1, '& v2 =', v2) 

print('Сумма вектров равна:')
result = map(lambda x, y: x + y, v1, v2) 

print('\n'.join(map(str, result)))