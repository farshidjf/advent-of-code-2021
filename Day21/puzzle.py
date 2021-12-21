from functools import cache
from itertools import product
import numpy as np

def play(x: int, score: int, dice: tuple[int, int, int], count: int = 0) -> tuple[int, int, int]:
      return (xx := (x + sum(dice) - 1) % 10 + 1), score + xx, count + 3

def puzzle1(x1: int, x2: int) -> int:
      s1, s2, count = 0, 0, 0
      d = 1
      while s2 < 1000:
            x1, s1, count = play(x1, s1, (d, d+1, d+2), count)
            d = (d + 2) % 100 + 1
            x1, x2, s1, s2 = x2, x1, s2, s1
      return s1 * count

dices = list(product((1,2,3), repeat=3))
@cache
def puzzle2(x1: int, x2: int, s1: int = 0, s2: int = 0, until: int = 21, turn: int = 0) -> np.ndarray:
      if s2 >= until: return np.array([turn, 1-turn])
      wins = np.array([0, 0])
      for dice in dices:
            xx, ss, _ = play(x1, s1, dice)
            shift = min(ss, s2)
            wins += puzzle2(x2, xx, s2-shift, ss-shift, until-shift, 1-turn)
      return wins

inputs = (((4, 8), 'test_input'), ((6, 4), 'main_input'))
for (x, y), label in inputs[:]:
      print(f'Puzzle 1 for {label}: {puzzle1(x, y)}')
      print(f'Puzzle 2 for {label}: {max(puzzle2(x, y))}')