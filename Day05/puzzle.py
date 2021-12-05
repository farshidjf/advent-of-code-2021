from collections import Counter

def count_cross_per_point(coordinates, diagonal=False):
      counter = Counter()
      for x1, y1, x2, y2 in coordinates:
            if x1 == x2:
                  for y in range(min(y1,y2), max(y1,y2) + 1):
                        counter[(x1, y)] += 1
            elif y1 == y2:
                  for x in range(min(x1,x2), max(x1,x2) + 1):
                        counter[(x, y1)] += 1
            elif diagonal:      # puzzle2
                  if (slope := (y2-y1)/(x2-x1)) in (1, -1):
                        y = y1 if x1 < x2 else y2
                        for d, x in enumerate(range(min(x1,x2), max(x1,x2) + 1)):
                              counter[(x, y + int(slope) * d)] += 1
      return sum([1 for k, v in counter.items() if v > 1])
            

file_names = ['test_input', 'main_input']
folder_name = './Day05/'
for file_name in file_names[:]:
      with open(folder_name + file_name) as input_file:
            coordinates = []
            for line in input_file:
                  coordinates.append( tuple(int(x) for p in line.split(' -> ') for x in p.split(',')) )
            print(f'Puzzle 1 for {file_name}: {count_cross_per_point(coordinates)}')
            print(f'Puzzle 2 for {file_name}: {count_cross_per_point(coordinates, diagonal=True)}')