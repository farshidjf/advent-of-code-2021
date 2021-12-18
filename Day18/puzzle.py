
import functools
import re

def find_left(x: str) -> tuple[bool, int, int]:
      try:
            left = re.findall(r'\d+', x)[-1]
            return True, (left1 := x.rfind(left)), left1 + len(left)
      except IndexError:
            return False, 0, 0
      
def find_right(x: str, offset: int = 0) -> tuple[bool, int, int]:
      try:
            right = re.findall(r'\d+', x)[0]
            return True, (right1 := x.find(right)) + offset, right1 + len(right) + offset
      except IndexError:
            return False, 0, 0

def search_explode(x: str) -> tuple[bool, str]:
      depth: int = 0
      for i, c in enumerate(x):
            if c == '[': depth += 1
            elif c == ']': depth -= 1
            if depth == 5:
                  to_explode: tuple[int, int] = eval(x[i: i + (length := x[i:].find(']') + 1)])
                  there_is_a_left, left1, left2 = find_left(x[:i])
                  there_is_a_right, right1, right2 = find_right(x[i+length:], i+length)
                  if there_is_a_left:
                        y = x[:left1] + str(eval(x[left1:left2]) + to_explode[0]) + x[left2: i]
                  else:
                        y = x[:i]
                  y += '0'
                  if there_is_a_right:
                        y += x[i+length: right1] + str(eval(x[right1: right2]) + to_explode[1]) + x[right2:]
                  else: 
                        y += x[i+length:]
                  return True, y
      return False, x

split = lambda x: f'[{x // 2},{(x + 1) // 2}]'
def search_split(x: str) -> tuple[bool, str]:
      numbers = re.findall(r'\d+', x)
      for number in numbers:
            if (n := int(number)) > 9:
                  p1 = x.find(number)
                  p2 = p1 + len(number)
                  return True, x[:p1] + split(n) + x[p2:]
      return False, x

def reduce(x: str) -> tuple[bool, str]:
      success, y = search_explode(x)
      if success: return reduce(y)
      success, y = search_split(y)
      if success: return reduce(y)
      return y

_magnitude = lambda x: x if type(x) == int else 3 * _magnitude(x[0]) + 2 * _magnitude(x[1])
magnitude = lambda x: _magnitude(eval(x))
add = lambda x, y: reduce(f'[{x},{y}]')

def find_largest_sum(numbers: list[str]) -> int:
      largest_sum = 0
      for n1 in numbers:
            for n2 in numbers:
                  if n1 != n2:
                        largest_sum = max(largest_sum, magnitude(add(n1, n2)))
      return largest_sum

file_names = ['test_input', 'main_input']
folder_name = './Day18/'
for file_name in file_names[:]:
      with open(folder_name + file_name) as input_file:
            snail_numbers: list[str] = [line.strip() for line in input_file.readlines()]
            total = functools.reduce(add, snail_numbers)
            print(f'Puzzle 1 for {file_name}: {magnitude(total)}')
            print(f'Puzzle 2 for {file_name}: {find_largest_sum(snail_numbers)}')