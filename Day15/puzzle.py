def grid_dijkstra(weight: list[list[int]]):
      N = len(weight)
      start, target = (int(0), int(0)), (N-1, N-1)
      V = {(i, j) for i in range(N) for j in range(N)}
      neighbors = {v: {n for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)) 
                       if (n := (v[0]+dx, v[1]+dy)) in V}
                   for v in V} 
      distance = {v: 20 * N for v in V}
      distance[start] = 0
      visited = set()
      unvisited = {start}
      while target not in visited:
            current = min(unvisited, key=lambda v: distance[v])
            for n in neighbors[current] - visited:
                  if distance[n] > (_distance := weight[n[0]][n[1]] + distance[current]):
                        distance[n] = _distance
                  unvisited.add(n)
            unvisited.remove(current)
            visited.add(current)
      return distance[target]

def tile_area(tile: list[list[int]], repeat: int = 5):
      N = len(tile)
      area = [[0 for _ in range(N*repeat)] for __ in range(N*repeat)]
      for i in range(repeat):
            for ii in range(N):
                  for j in range(repeat):
                        for jj in range(N):
                              _value = tile[ii][jj]
                              for _ in range(i+j):
                                    _value = _value + 1 if _value != 9 else 1
                              area[i * N + ii][j * N + jj] = _value
      return area

file_names = ['test_input', 'main_input']
folder_name = './Day15/'
for file_name in file_names[:]:
      with open(folder_name + file_name) as input_file:
            risks = [[int(r) for r in line.strip()] for line in input_file.readlines()]
            print(f'Puzzle 1 for {file_name}: {grid_dijkstra(risks)}')
            tiled_risks = tile_area(risks)
            print(f'Puzzle 2 for {file_name}: {grid_dijkstra(tiled_risks)}')