import numpy as np

def fuel(ps, puzzle2=False):
      cost = (lambda n: n * (n + 1) // 2) if puzzle2 else (lambda n: n)
      return np.min([np.sum(cost(np.abs(ps - n))) for n in range(max(ps))])

file_names = ['test_input', 'main_input']
folder_name = './Day07/'
for file_name in file_names[:]:
      with open(folder_name + file_name) as input_file:
            positions = np.array(list(map(int, input_file.readline().strip().split(','))))
            print(f'Puzzle 1 for {file_name}: {fuel(positions)}')
            print(f'Puzzle 2 for {file_name}: {fuel(positions, puzzle2=True)}')