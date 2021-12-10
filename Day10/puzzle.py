from numpy import median

open_char = ['(', '[', '{', '<']
close_char = [')', ']', '}', '>']
match = {o: c for o, c in zip(open_char, close_char)}

def parse(chuck: str, 
          unmatched: list[str], 
          matched: list[tuple[str, str]]) -> tuple[list[tuple[str, str]], list[str]]:
      if len(chuck) == 0:
            return matched, unmatched
      if chuck[0] in open_char:
            return parse(chuck[1:], unmatched + [chuck[0]], matched)
      return parse(chuck[1:], unmatched[:-1], matched + [(unmatched[-1], chuck[0])])

is_valid_match = lambda o, c: match[o] == c
mistake_points = {c: p for c, p in zip(close_char, [3,57,1197,25137])}
incomplete_points = {c: p for c, p in zip(open_char, range(1,5))}
bad_chuck_points = lambda pairs: sum([mistake_points[c] for o, c in pairs if not is_valid_match(o, c)])
is_valid = lambda pairs: all([is_valid_match(o, c) for o, c in pairs])

def incomplete_score(singles: list[str], score: int = 0) -> int:
      if singles == []:
            return score
      return incomplete_score(singles[:-1], 5 * score + incomplete_points[singles[-1]])

def puzzle1() -> int:
      return sum([bad_chuck_points(pairs) for pairs, _ in parsed_chucks])

def puzzle2() -> int:
      return int(median([incomplete_score(singles) for pairs, singles in parsed_chucks if is_valid(pairs)]))

file_names = ['test_input', 'main_input']
folder_name = './Day10/'
for file_name in file_names[:]:
      with open(folder_name + file_name) as input_file:
            parsed_chucks = [parse(line.strip(), [], []) for line in input_file]
            print(f'Puzzle 1 for {file_name}: {puzzle1()}')
            print(f'Puzzle 2 for {file_name}: {puzzle2()}')