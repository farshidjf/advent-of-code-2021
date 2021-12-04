import numpy as np

def parse_input(input_file):
      numbers = list(map(int, input_file.readline().split(',')))
      boards = []
      for _ in range(100):
            input_file.readline()
            boards.append(np.array([[int(n) for n in input_file.readline().split()] for _ in range(5)]))
      return numbers, boards

def score(board, xs, ys, n):
      _board = board.copy()
      for x, y in zip(xs, ys):
            _board[x, y] = 0
      return n * np.sum(_board)


bingo = lambda x, y: max([u.count(i) for i in range(5) for u in (x, y)]) == 5

def puzzle1(numbers, boards):
      nb = len(boards)
      xs, ys = [[] for _ in range(nb)], [[] for _ in range(nb)]
      for n in numbers:
            for b, board in enumerate(boards):
                  x, y = np.where(board == n)
                  if len(x) != 0:
                        xs[b].append(x[0])
                        ys[b].append(y[0])
                        if bingo(xs[b], ys[b]):
                              break
            else: continue
            break
      return score(boards[b], xs[b], ys[b], n)


def puzzle2(numbers, boards):
      nb = len(boards)
      xs, ys = [[] for _ in range(nb)], [[] for _ in range(nb)]
      loser_list = list(range(nb))
      for n in numbers:
            for b, board in enumerate(boards):
                  if b in loser_list:
                        x, y = np.where(board == n)
                        if len(x) != 0:
                              xs[b].append(x[0])
                              ys[b].append(y[0])
                              if bingo(xs[b], ys[b]):
                                    if len(loser_list) == 1:
                                          break
                                    loser_list.remove(b)
            else: continue
            break
      return score(boards[b], xs[b], ys[b], n)


file_names = ['test_input', 'main_input']
folder_name = './Day04/'
for file_name in file_names[1:]:
      with open(folder_name + file_name) as input_file:
            numbers, boards = parse_input(input_file)
            print(f'Puzzle 1 for {file_name}: {puzzle1(numbers, boards)}')
            print(f'Puzzle 2 for {file_name}: {puzzle2(numbers, boards)}')