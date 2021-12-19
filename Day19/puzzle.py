from itertools import permutations, product, combinations
from functools import reduce
import numpy as np

rotations = []
for p in permutations(np.eye(3, dtype=int)):
      for sgns in product((1,-1), repeat=3):
            rotation = np.array([s*row for s, row in zip(sgns, p)])
            if np.linalg.det(rotation) == 1:
                  rotations.append(rotation)

to_set = lambda arr: set([tuple(row) for row in arr])
def overlaps(scanner1: np.ndarray, scanner2: np.ndarray
             ) -> tuple[bool, np.ndarray, np.ndarray]:
      beacons1 = to_set(scanner1)
      for rotation in rotations:
            rotated = scanner2 @ rotation
            for beacon1 in scanner1:
                  for beacon2 in rotated:
                        shifted = rotated + (shift := beacon1 - beacon2)
                        if len(beacons1 & to_set(shifted)) >= 12:
                              return True, shifted, shift
      return False, shifted, shift
                  
def assemble(scanners: list[np.ndarray]
             ) -> tuple[list[np.ndarray], list[np.ndarray]]:
      possitions = [np.array([0, 0, 0])]
      assembled = []
      def _assemble(scanner):
            matched = []
            for i, scanner2 in enumerate(scanners):
                  overlap, shifted, shift = overlaps(scanner, scanner2)
                  if overlap:
                        possitions.append(shift)
                        matched.append((i, shifted))
            assembled.append(scanner)
            for i, _ in matched[::-1]: scanners.pop(i)
            for _, shifted in matched: _assemble(shifted)
      _assemble(scanners.pop(0))
      return assembled, possitions
                  
file_names = ['test_input', 'main_input']
folder_name = './Day19/'
for file_name in file_names[:]:
      with open(folder_name + file_name) as input_file:
            data = [np.array([[int(c) for c in line.strip().split(',')]
                              for line in block.split('\n')[1:]])
                    for block in input_file.read().split('\n\n')]
            assembled, positions = assemble(data)
            count = len(reduce(lambda s1, s2: to_set(s1) | to_set(s2), assembled))
            print(f'Puzzle 1 for {file_name}: {count}')
            largest_distance = max([np.sum(abs(p1 - p2)) for p1, p2 in combinations(positions, 2)])
            print(f'Puzzle 2 for {file_name}: {largest_distance}')