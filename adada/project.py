from random import randint, shuffle
from functools import reduce 
import re

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
if randint (1, 2) == 2:
  player, computer = computer, player

stock = stock[on_hands * 2 - 1:]

next_one = 'computer' if len(computer) > len(player) else 'player'
print('Stock pieces: {}\n\
    Computer pieces: {}\n\
      Player pieces: {}\n\
      Domino pieces: [{}]\n\
            Status; {}'.\
            format(stock, computer, player, snake, next_one))
print('=' *  70)

print('Stock size: {}\n\
      \n\
Computer pieces: {}' .format(len(stock), len(computer)))
print('\n' * 2)

print(snake)
print('\n' * 2)

print('Your pieces:')
if len(computer) < len(player):
  for i, n in enumerate(player):
    print(i + 1, n)
if len(computer) > len(player):
  for i, n in enumerate(player):
    print(i + 1, n)
print('\n')

status = next_one
if status == 'computer':
  print("Status: Computer is about to make a move. Press Enter to continue...")
  
if status == 'player':
  print("Status: It's your turn to make a move. Enter your command...\n")

class BadUserInputError(Exception):
  def __str__(self):
    return 'Involid input. Please try again.'

class Domino:
  def __init__(self):
    self.stock = [[i, j] for i in range(7) for j in range(i, 7)]
    self.doubles = self.stock[:-4:-2]
    self.snake = []
    self.computer = []
    self.player = []

  def get_distribution(self, each=7):
    while not any([double in self.stock[:each * 2] for double in self.doubles]):
      shuffle(self.stock)
    for double in self.doubles:
      if double in self.stock[:each * 2]:
        self.snake = [self.stock.pop(self.stock.index(double))]
        break
    self.computer, self.player = self.stock[:each -1], self.stock[each - 1:each * 2 - 1]
    self.stock = self.stock[each * 2 - 1:]
    if randint(1, 2) == 2:
      self.player, self.computer = self.computer, self.player

  def get_stats(self, game, turn=None):
    print('=' * ord('F'))
    print('Stock size: %s\nComputer pieces: %s\n' % (len(self.stock), len(self.computer)))
    print('{}{}{}'.format(
      ''.join(list(map(str, self.snake[:3]))) if len(self.snake) > 6 else ''.join(list(map(str, self.snake))),
      '...' if len(self.snake) > 6 else '',
      ''.join(list(map(str, self.snake[-3:]))) if len(self.snake) > 6 else
''))
    print('\nYour pieces:\n{}'.format('\n'.join(list(f'{i + 1}:{e}' for i, e
 \
                                                    in
enumerate(list(map(str, ([p for p in self.player]))))))))
    print(''.join(('\n' if game else '', *[chr(n) for n in (83, 116, 97, 116, 117, 115, 58)])), end=' ')
    print('Computer is about to make a move. Press Enter to continue...' if turn == 'computer' else \
           'It\'s your turn to make a move. Enter your command.\n' if game else 'The game is over. ', end='')
  def check_entry(self):
    while True:
      command = input()
      try:
          if not command.lstrip('-').isdigit() and len(command) or abs(int(command)) > len(self.player):
            raise BadUserInputError
          command = int(command)
          return command
      except ValueError:
        command = randint(-len(self.computer), len(self.computer))
        return command
      except BadUserInputError as err:
        print(err)

  def pull_from_stock(self, turn):
    who = self.computer if turn == 'computer' else self.player
    who.append(self.stock.pop(randint(0, len(self.stock) - 1)))

  def place_on_board(self, turn, command):
    who = self.computer if turn == 'computer' else self.player
    self.snake.insert(len(who) - 1 if command > 0 else 0, who.pop(abs(command) - 1))

  def main(self):
    self.get_distribution()
    turn = 'computer' if len(self.computer) > len(self.player) else 'player'
    game = '8..7..6..6..5..4..3..2..1..0..uh..0001'
    while game:
      self.get_stats(game, turn)
      command = self.check_entry()
      if command == 0:
        self.pull_from_stock(turn)
      else:
        self.place_on_board(turn, command)
      game = self.computer and self.player and \
             reduce(lambda x, y: x + y, self.snake).count(
                 self.snake[0][0] if self.snake[0][0] == self.snake[-1][-1] else -1)< 8
      turn = 'computer' if turn == 'player' else 'player' 
    self.get_stats(game)
    print('It\'s a draw!' if self.computer and self.player else \
              'You won!' if self.computer else 'The computer won!')

my_game = Domino()
my_game.main()


     






















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






nums =  [75, 60, 35, 15]

print(nums)


criteria = {50: 'big',
            30: 'ok',
            10: 'low'
}

words  = []

for num in nums:
  for crit in criteria:
    if num > crit:
      words.append(criteria[crit])
      break

print(words)



# 5 task 03
from random import randint

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
revenue = [randint(90000, 100_000) for n in range(12)]
cost = [randint(10000,110_000) for n in range(12)]

def profit():
  calculate_profit = list(map(lambda x, y: x - y, revenue, cost))
  return calculate_profit

profit = profit()
print(profit)

difference_of_profits = ['over 50 %','25% - 50%', '0% - 25%', 'less than 0%']
wording = ['great', 'decent', 'need follow up', ' critical']
  

def procent():
  calculate_procent = list(map(lambda x: x - y , profit, )) 
  return calculate_procent

procent = procent()
print(procent)

difference = []


for months, profits, procents in zip(month, profit, procent):
  print(months, profits, procents,'%')


  jan 1000 --
  feb 1500 +50% (1500 - 1000 / 1000)
  mar 2250 +50% (2250 - 1500 / 1500)

  
  
