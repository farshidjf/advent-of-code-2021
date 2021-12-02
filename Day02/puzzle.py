def final_position_1(directions, values):
      n = len(values)
      x = sum([values[i] for i in range(n) if directions[i] == "forward"])
      y = sum([values[i] for i in range(n) if directions[i] == "down"])
      y-= sum([values[i] for i in range(n) if directions[i] == "up"])
      return x*y

def final_position_2(directions, values):
      aim, x, y = 0, 0, 0
      for d, v in zip(directions, values):
            if d == 'down':
                  aim += v
            elif d == 'up':
                  aim -= v
            elif d == 'forward':
                  x += v
                  y += aim * v
      return x*y

file_names = ['small_input', 'large_input']
folder_name = './Day02/'
for file_name in file_names[:]:
      with open(folder_name + file_name) as input_file:
            directions, values = zip(*(line.split() for line in input_file))
            values = [int(v) for v in values]
            print(f'Puzzle 1 for {file_name}: {final_position_1(directions, values)}')
            print(f'Puzzle 2 for {file_name}: {final_position_2(directions, values)}')
            