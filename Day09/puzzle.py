def neighbors(i, j):
      cap = lambda i: i if i >= 0 else 1e10
      neighbors = []
      for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            try: 
                  heights[cap(i+di)][cap(j+dj)]
                  neighbors.append((i+di, j+dj))
            except: pass
      return neighbors

def find_mins():
      mins = []
      for i, row in enumerate(heights):
            for j, h in enumerate(row):
                  if h < min([heights[ni][nj] for ni, nj in neighbors(i, j)]):
                        mins.append((i, j))
      return mins

def extend_basin(basin, i, j):
      basin.add((i, j))
      for ni, nj in neighbors(i, j):
            if (ni, nj) not in basin and heights[ni][nj] != 9:
                  extend_basin(basin, ni, nj)
      return basin

def puzzle1():
      return sum([heights[i][j]+1 for i, j in find_mins()])

def puzzle2():
      bsize = [len(extend_basin(set(), i, j)) for i, j in find_mins()]
      ret = 1
      for _ in range(3):
            ret *= max(bsize)
            bsize.remove(max(bsize))
      return ret

file_names = ['test_input', 'main_input']
folder_name = './Day09/'
for file_name in file_names[:]:
      with open(folder_name + file_name) as input_file:
            heights = [[int(d) for d in line.strip()] for line in input_file]
            print(f'Puzzle 1 for {file_name}: {puzzle1()}')
            print(f'Puzzle 2 for {file_name}: {puzzle2()}')