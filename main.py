#8 task 02

def enter_name():
  try:
      name, surname = input('Введите фамилию и имя:').split()
     
          
  except ValueError:
      print('You need to enter exactly 2 words. Try again!')
      enter_name()
      
  else:
      print('Welcome to our party,', name, surname)
enter_name()


