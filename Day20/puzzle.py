def pad(image: list[str], p: int) -> list[str]:
      n = len(image)
      new_image = ['.' * (n+2*p) for _ in range(p)]
      for line in image: new_image.append('.'*p + line + '.'*p)
      for _ in range(p): new_image.append('.' * (n+2*p))
      return new_image
      
def enhance(image: list[str], algorithm: str, padding: int) -> list[str]:
      index = lambda i, j: int(''.join([line[j-1:j+2] for line in padded_image[i-1:i+2]]).replace('.', '0').replace('#', '1'), 2)
      padded_image = pad(image, padding)
      mutable_image = [list(line) for line in padded_image]
      m = len(image)
      for i in range(1, m+2*padding-1):
            for j in range(1, m+2*padding-1):
                  mutable_image[i][j] = algorithm[index(i, j)]
      return [''.join(line) for line in mutable_image]

def puzzle(puzzle_num: int) -> int:
      new_image = image.copy()
      for _ in range(1 if puzzle_num == 1 else 25):
            new_image = enhance(new_image, algorithm, 4)
            new_image = enhance(new_image, algorithm, 0)
            new_image = [line[2:-2] for line in new_image[2:-2]]
      return sum([line.count('#') for line in new_image])
      
file_names = ['test_input', 'main_input']
folder_name = './Day20/'
for file_name in file_names[:]:
      with open(folder_name + file_name) as input_file:
            algorithm = input_file.readline().strip()
            input_file.readline()
            image = [line.strip() for line in input_file.readlines()]
            print(f'Puzzle 1 for {file_name}: {puzzle(puzzle_num=1)}')
            print(f'Puzzle 2 for {file_name}: {puzzle(puzzle_num=2)}')