from itertools import product
import heapq
def grid_dijkstra(weight: list[list[int]]) -> int:
      N = len(weight)
      start, target = (int(0), int(0)), (N-1, N-1)
      V = {(i, j) for i in range(N) for j in range(N)}
      neighbors = {v: {n for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)) 
                       if (n := (v[0]+dx, v[1]+dy)) in V}
                   for v in V}
      visited = set()
      unvisited = [(0, start)]
      while target not in visited:
            distance, current = heapq.heappop(unvisited)
            if current in visited: continue
            visited.add(current)
            for n in neighbors[current] - visited:
                  heapq.heappush(unvisited, (weight[n[0]][n[1]] + distance, n))
      return distance

def tile_area(tile: list[list[int]], repeat: int = 5) -> list[list[int]]:
      N = len(tile)
      area = [[0 for _ in range(N*repeat)] for __ in range(N*repeat)]
      for i, j  in product(range(repeat), repeat=2):
            for ii, jj in product(range(N), repeat=2):
                  area[i * N + ii][j * N + jj] = (tile[ii][jj] + i + j - 1) % 9 + 1
      return area

file_names = ['test_input', 'main_input']
folder_name = './Day15/'
for file_name in file_names[:]:
      with open(folder_name + file_name) as input_file:
            risks = [[int(r) for r in line.strip()] for line in input_file.readlines()]
            print(f'Puzzle 1 for {file_name}: {grid_dijkstra(risks)}')
            print(f'Puzzle 2 for {file_name}: {grid_dijkstra(tile_area(risks))}')
