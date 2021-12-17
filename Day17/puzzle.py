def run(x1: int, x2: int, y1: int, y2: int, vx: int, vy: int) -> int:
      x, y = 0, 0
      max_height = 0
      while y >= y1:
            x += vx
            y += vy
            vx -= 1 if vx > 0 else 0
            vy -= 1
            max_height = max(y, max_height)
            if x1 <= x <= x2 and y1 <= y <= y2:
                  return max_height
      return -1

inputs = (((20, 30, -10, -5), 'test_input'), ((94, 151, -156, -103), 'main_input'))
for (x1, x2, y1, y2), label in inputs[:]:
      max_height = -1
      count = 0
      for vx in range(1, x2+1):
            for vy in range(y1, 1000):
                  height = run(x1, x2, y1, y2, vx, vy)
                  max_height = max(max_height, height)
                  if height != -1:
                        count += 1
      print(f'Puzzle 1 for {label}: {max_height}')
      print(f'Puzzle 2 for {label}: {count}')