import networkx as nx

def walk(G: nx.graph, nodes: list, count: int, revisited: bool):
      if (last := nodes[-1]) == 'end':
            return count + 1
      for neighbor in G[last]:
            if neighbor.islower() and neighbor in nodes:
                  if revisited or neighbor == 'start':
                        continue
                  else: # for puzzle 2
                        count = walk(G, nodes + [neighbor], count, True)
            else:
                  count = walk(G, nodes + [neighbor], count, revisited)
      return count

file_names = ['test_input_1', 'test_input_2', 'test_input_3', 'main_input']
folder_name = './Day12/'
for file_name in file_names[:]:
      with open(folder_name + file_name) as input_file:
            edges = {tuple(line.strip().split('-')) for line in input_file}
            G = nx.Graph()
            G.add_edges_from(edges)
            print(f'Puzzle 1 for {file_name}: {walk(G, ["start"], 0, True)}')
            print(f'Puzzle 2 for {file_name}: {walk(G, ["start"], 0, False)}')