# 4 task 05

daily_temp_c = [20, 19, 15, 25, 27, 30, 31, 29, 26, 21,
                19, 25, 27.5, 28, 26, 29.5, 31, 27.5, 26, 29,
                18, 17.5, 17, 16.5, 19, 20, 25, 26.5, 27, 28,
                20.5, 19, 25, 27.5, 28, 26, 15, 25, 27, 28]


  

def celsius_to_fahrenheit(daily_temp_c):
   return (daily_temp_c * 9 / 5) + 32

fahrenheit = list(map(celsius_to_fahrenheit, daily_temp_c))


def temp_above_80 (fahreinheit):
  return fahreinheit < 80

days = list(filter(temp_above_80, fahrenheit))



for i, name in enumerate(days, start=1):
  print(i, name)

