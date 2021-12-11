import numpy as np

cap = lambda i: i if i >= 0 else 11
def step(energy):
      just_flashed = np.zeros((10,10)).astype(int)
      energy += 1
      while(np.max(energy) > 9):
            for i in range(10):
                  for j in range(10):
                        if energy[i, j] > 9 and just_flashed[i, j] == 0:
                              just_flashed[i, j] = 1
                              for ii in range(-1,2):
                                    for jj in range(-1,2):
                                          try:
                                                if just_flashed[i+ii,j+jj] == 0:
                                                      energy[cap(i+ii), cap(j+jj)] += 1
                                          except: pass
                              energy[i, j] = 0
      return np.sum(just_flashed)

def puzzle1(energy) -> int:
      return sum(step(energy) for _ in range(1, 101))

def puzzle2(energy) -> int:
      for t in range(1, 10000):
            if step(energy) == 100:
                  return t
      return -1

file_names = ['test_input', 'main_input']
folder_name = './Day11/'
for file_name in file_names[:]:
      with open(folder_name + file_name) as input_file:
            energy = np.array([[int(c) for c in line.strip()] for line in input_file]).astype(int)
            print(f'Puzzle 1 for {file_name}: {puzzle1(energy.copy())}')
            print(f'Puzzle 2 for {file_name}: {puzzle2(energy.copy())}')