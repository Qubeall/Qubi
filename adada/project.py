# stage 5

from random import randint, shuffle, choice, choices
from functools import reduce
from collections import Counter
import itertools
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

class IllegalMoveError(Exception):
  def __str__(self):
    return 'Illegal move. Please try again.'

class Domino:
  def __init__(self):
    self.stock = [[i, j] for i in range(7) for j in range(i, 7)]
    self.doubles = self.stock[:-4:-2]
    self.snake = []
    self.snake_left_end = None
    self.snake_right_end = None
    self.snake_ends = None
    self.computer = []
    self.player = []

  # USER ENTRY
  def get_command(self):
    while True:
      command = input()
      if command == '':
          return self.get_ai_command()
      try:
          if re.match(r'^-?\d{,2}$', command) is None or abs(int(command))  > len(self.player):
            raise BadUserInputError
            command = int(command)
            if command > 0 and self.snake_right_end not in self.player[command - 1 ] or \
            command < 0 and self.snake__left_end not in self.player[abs(command) - 1]:
              raise IllegalMoveError
            return  command
      except BadUserInputError as err:
            print(err)
      except IllegalMoveError as err:
            print(err)



  # AI MOVE COMPUTATION
  def get_ai_command(self):
      all_options = [opt for opt in self.computer if opt[0] in self.snake_ends or opt[1] in self.snake_ends]
      frequencies = Counter(list(itertools.chain.from_iterable(self.computer + self.snake)))
      options_weights = [frequencies[opt[0]] + frequencies[opt[1]] for opt in all_options]
      highest_score_options = [opt for opt, freq in zip(all_options, options_weights) if freq == max(options_weights)]
      if all_options:
          if self.diff == 1:
              move_choice = choice(all_options)
          if self.diff == 2:
              move_choice = choices(all_options, options_weights)[0]
          if self.diff == 3:
              move_choice = choice(highest_score_options)
          command_right: int = self.computer.index(move_choice) + 1
          command_left: int = command_right * - 1
          if all((self.snake_right_end in move_choice, self.snake_left_end in move_choice)):
              command = choice((command_right, command_left))
          elif self.snake_right_end in move_choice:
              command = command_right
          else: command = command_left
      else:
          command = 0
      return command



  # PRE-GAME

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


      
    # IN-GAME
  def update_snake_ends(self):
    self.snake_right_end, self.snake_left_end = self.snake[-1][-1], self.snake[0][0]
    self.snake_ends = [self.snake_left_end, self.snake_right_end]

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

  def check_game_run(self):
      ends_match: bool = len({self.snake_right_end, self.snake_left_end}) == 1
      ends_less_8: bool = reduce(lambda x,y: x + y, self.snake).count(self.snake_left_end if ends_match else -1) < 8
      return all((self.computer, self.player, ends_less_8))
  # /IN-GAME

    

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

  # MOVE (USER, AI)
  def place_on_board(self, turn, command):
      who = self.computer if turn == 'computer' else self.player
      what = self.flip_if_needed(who.pop(abs(command) - 1), command)
      self.snake.insert(len(self.snake) if command > 0 else 0, what)

  def flip_if_needed(self, what, command):
      if command > 0 and self.snake_right_end !=what[0] or \
              command < 0 and self.snake_left_end !=what[1]:
            return [what[1], what[0]]
      return what


  def pull_from_stock(self, turn):
      who = self.computer if turn == 'computer' else self.player
      who.append(self.stock.pop(randint(0, len(self.stock) - 1)))
  # /MOVE (USER, AI)



  # GAME
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





  
  
