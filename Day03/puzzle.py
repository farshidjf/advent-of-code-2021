import numpy as np

def puzzle1(data):
      n, m = data.shape
      gamma = int(''.join(['0' if d < n/2 else '1' for d  in np.sum(data, axis=0)]), 2)
      epsilon = 2**m-1 - gamma
      return gamma * epsilon


def puzzle2(data):
      _data = data.copy()
      
      list_to_binary = lambda lst: int(''.join(str(d) for d in lst), 2)
      majority = lambda column: 0 if sum(_data[:, column]) < _data.shape[0]/2 else 1
      
      for c in range(_data.shape[1]):
            _data = _data[_data[:,c] == majority(c),:]
      gamma = list_to_binary(_data[0])
      
      _data = data.copy()
      for c in range(_data.shape[1]):
            _data = _data[_data[:,c] != majority(c),:]
            if _data.shape[0] == 1: break
      epsilon = list_to_binary(_data[0])
      
      return gamma * epsilon


file_names = ['test_input', 'main_input']
folder_name = './Day03/'
for file_name in file_names[:]:
      with open(folder_name + file_name) as input_file:
            data = np.array([[int(c) for c in line.strip()] for line in input_file])
            print(f'Puzzle 1 for {file_name}: {puzzle1(data)}')
            print(f'Puzzle 2 for {file_name}: {puzzle2(data)}')