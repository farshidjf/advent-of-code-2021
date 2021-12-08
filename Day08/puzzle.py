from itertools import permutations

def parse_input(file):
      input, output = [], []
      for line in file:
            ii, oo = line.strip().split(' | ')
            input.append(ii.split())
            output.append(oo.split())
      return input, output

def puzzle1(output):
      return len([o for oo in output for o in oo if len(o) in (2,4,3,7)])

alphabet = set([chr(i) for i in range(ord('a'), ord('g') + 1)])
correct_code = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
correct_code = [set(code) for code in correct_code]

def replace(string, dictionary):
      for k, v in dictionary.items():
            string = string.replace(k, v)
      return string

def to_digit(string, matching):
      return correct_code.index(set(replace(string, matching).lower()))

def to_number(lst, matching):
      return int(''.join([str(to_digit(ds, matching)) for ds in lst]))

def puzzle2(input, output):
      total = 0
      for ii, oo in zip(input, output):
            matching = dict()
            for p in permutations(alphabet):
                  matching = {a: b.upper() for a, b in zip(alphabet, p)}
                  try: 
                        _ = [to_digit(i, matching) for i in ii]
                        break
                  except: continue
            total += to_number(oo, matching)
            
      return total
      
file_names = ['test_input', 'main_input']
folder_name = './Day08/'
for file_name in file_names[:]:
      with open(folder_name + file_name) as input_file:
            input, output = parse_input(input_file)
            print(f'Puzzle 1 for {file_name}: {puzzle1(output)}')
            print(f'Puzzle 2 for {file_name}: {puzzle2(input, output)}')