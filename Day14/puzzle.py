from collections import Counter

def insert(pair_counts: Counter[str], insertion: dict[str, str], n: int):
      if n == 0: return pair_counts
      new_counts = pair_counts.copy()
      for pair in pair_counts:
            if pair in insertion:
                  new_counts[pair[0]+insertion[pair]] += pair_counts[pair]
                  new_counts[insertion[pair]+pair[1]] += pair_counts[pair]
                  new_counts[pair] -= pair_counts[pair]
      return insert(new_counts, insertion, n-1)

def puzzle(n: int):
      pair_counts = Counter([template[i:i+2] for i in range(len(template)-1)])
      pair_counts = insert(pair_counts, insertions, n)
      # converting pair_count to char_count: 
      #     everything is double counted except the first and last
      char_count = Counter()
      for (c1, c2), n in pair_counts.items():
            char_count[c1] += n
            char_count[c2] += n
      char_count[template[0]] += 1
      char_count[template[-1]] += 1
      return (max(char_count.values()) - min(char_count.values()))//2

file_names = ['test_input', 'main_input']
folder_name = './Day14/'
for file_name in file_names[:]:
      with open(folder_name + file_name) as input_file:
            template, insertions = input_file.read().split('\n\n')
            insertions = dict(tuple(x for x in line.split(' -> ')) for line in insertions.split('\n'))
            print(f'Puzzle 1 for {file_name}: {puzzle(10)}')
            print(f'Puzzle 2 for {file_name}: {puzzle(40)}')