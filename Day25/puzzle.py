from copy import deepcopy
def step(direction: str, data: list[list[str]]) -> list[list[str]]:
      m, n = len(data), len(data[0])
      _data = deepcopy(data)
      for i in range(m):
            for j in range(n):
                  if direction == 'east':
                        if data[i][j] == '>' and data[i][(j + 1) % n] == '.':
                              _data[i][j] = '.' 
                              _data[i][(j + 1) % n] = '>'
                  if direction == 'south':
                        if data[i][j] == 'v' and data[(i + 1) % m][j] == '.':
                              _data[i][j] = '.' 
                              _data[(i + 1) % m][j] = 'v'
      return _data

file_names = ['test_input', 'main_input']
folder_name = './Day25/'
for file_name in file_names:
      with open(folder_name + file_name) as input_file:
            data = [list(line.strip()) for line in input_file.readlines()]
            count, _data = 0, []
            while data != _data:
                  _data = deepcopy(data)
                  data = step('east', data)
                  data = step('south', data)
                  count += 1
            print(f'Puzzle 1 for {file_name}: {count}')