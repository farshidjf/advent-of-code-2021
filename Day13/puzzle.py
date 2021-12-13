def fold(dots: set[tuple[int, int]], folds: list[tuple[str, int]]):
      if not folds: return dots
      dir, f = folds[0]
      if dir == 'y':
            folded = {(x, 2*f - y) for x, y in dots if y > f}
            return fold({(x, y) for x, y in dots if y <= f} | folded, folds[1:])
      else:
            folded = {(2*f - x, y) for x, y in dots if x > f}
            return fold({(x, y) for x, y in dots if x <= f} | folded, folds[1:])
      
def paper_print(dots: set[tuple[int, int]]):
      for i in range(max([y for x, y in dots]) + 1):
            print(''.join('#' if (j, i) in dots else ' ' for j in range(max([x for x, y in dots]) + 1)))

file_names = ['test_input', 'main_input']
folder_name = './Day13/'
for file_name in file_names[:]:
      with open(folder_name + file_name) as input_file:
            dots, folds = input_file.read().split('\n\n')
            dots = set(tuple(int(x) for x in line.split(',')) for line in dots.split('\n'))
            folds = [tuple((line.split('=')[0][-1], int(line.split('=')[1]))) for line in folds.split('\n')]
            print(f'Puzzle 1 for {file_name}: {len(fold(dots, [folds[0]]))}')
            print(f'Puzzle 2 for {file_name}:')
            paper_print(fold(dots, folds))