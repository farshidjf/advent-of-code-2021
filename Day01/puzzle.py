def sliding_window_sum(lst, window=3):
    return [sum(lst[i:i+window]) for i in range(len(lst)-window+1)]

def count_increase(lst):
      return sum([lst[i+1] - lst[i] > 0 for i in range(len(lst)-1)])

file_names = ['small_input', 'large_input']
folder_name = './Day01/'
for file_name in file_names:
  with open(folder_name + file_name) as input_file:
    depths = [int(line) for line in input_file]
    print(f'Puzzle 1 for {file_name}: {count_increase(depths)}')
    print(f'Puzzle 2 for {file_name}: {count_increase(sliding_window_sum(depths))}')