from random import randint, shuffle

stock = [[i,j] for i in range(7) for j in range(i,7)]
doubles = stock [:-4:-2]
on_hands = 7


while not any([double in stock[:on_hands *2] for double in doubles]):
  shuffle(stock)


for double in doubles:
  if double in stock[:on_hands * 2]:
    snake = stock.pop(stock.index(double))
    break
computer, player = stock[:on_hands - 1], stock[on_hands - 1:on_hands * 2 - 1]
if randint(1, 2) == 2:
  player, computer = computer, player

stock = stock[on_hands *2 - 1:]

next_one = 'computer' if len(computer) > len(player) else 'player'

print('Stock pieces: {}\n\
    Computer pieces: {}\n\
      Player pieces: {}\n\
      Domino snake: [{}]\n\
             Status: {}'.\
             format(stock, computer, player, snake, next_one))


print('='*70)

print('Stock pieces: {}\n\
Computer pieces: {}'.\
      format(len(stock), (len(computer))))

print('Snake:')
print(snake)

print('Your pieces:')

for i, name in enumerate(player):
  print(i + 1, name)

status = next_one
if status == 'computer':
  print("Status: Computer is about to make a move. Press Enter to continue...")
  
if status == 'player':
  print("Status: It's your turn to make a move. Enter your command...")



Денис
Дима
Ваня
Дима
Дима
Лёха
Вова
Вадим
Богдан
Юра
Антон
Артем
Костя