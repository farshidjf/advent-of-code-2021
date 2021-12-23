import re
from itertools import product
from functools import reduce
from operator import mul
import sys
sys.setrecursionlimit(10000)

reg_str = r'^(?P<on>(on|off))\sx=(?P<x1>-?\d+)\.\.(?P<x2>-?\d+),y=(?P<y1>-?\d+)\.\.(?P<y2>-?\d+),z=(?P<z1>-?\d+)\.\.(?P<z2>-?\d+)\s?$'
def parse_input(file):
      ons, coords = [], []
      for line in file.readlines():
            m = re.match(reg_str, line)
            ons.append(int(m.group('on') == 'on'))
            coord = ((int(m.group('x1')), int(m.group('x2'))),
                     (int(m.group('y1')), int(m.group('y2'))),
                     (int(m.group('z1')), int(m.group('z2'))))
            coords.append(coord)
      return ons, coords

is_in_range = lambda coord, r1=-50, r2=50: all([x1 >= r1 and x2 <= r2 for x1, x2 in coord])
cuboid = lambda coord: set(product(*[range(x1, x2+1) for x1, x2 in coord]))
def initialization(on_off, coords):
      ons = set()
      for on, coord in zip(on_off, coords):
            if is_in_range(coord):
                  if on: ons.update(cuboid(coord))
                  if not on: ons -= cuboid(coord)
      return len(ons)

size = lambda c: reduce(mul, [x2 - x1 + 1 for x1, x2 in c])
overlap = lambda c1, c2: all(x2 >= xx1 and xx2 >= x1 for (x1, x2), (xx1, xx2) in zip(c1, c2))
is_inside = lambda c1, c2: all(xx1 <= x1 and x2 <= xx2 for (x1, x2), (xx1, xx2) in zip(c1, c2))

def overlap_break_down(c1, c2):
      intervals = []
      for (x1, x2), (xx1, xx2) in zip(c1, c2):
            a, b, c, d = sorted([x1, x2, xx1, xx2])
            if a < b and c < d:
                  intervals.append(((a, b-1), (b, c), (c+1, d)))
            elif a == b and c == d:
                  intervals.append(((b, c),))
            elif a == b:
                  intervals.append(((b, c), (c+1, d)))
            elif c == d:
                  intervals.append(((a, b-1), (b, c)))
      return product(*intervals)

def add(c1, c2):
      cuboids = overlap_break_down(c1, c2)
      ins, outs = set(), set()
      for c in cuboids:
            if overlap(c, c2): ins.add(c)
            elif overlap(c, c1): outs.add(c)
      return ins, outs

def subtract(c1, c2):
      cuboids = overlap_break_down(c1, c2)
      ret = set()
      for c in cuboids:
            if overlap(c, c1) and not overlap(c, c2):
                  ret.add(c)
      return ret

def join(new_cuboids, old_cuboids):
      for nc in new_cuboids:
            for oc in old_cuboids:
                  if is_inside(nc, oc):
                        return join(new_cuboids - {nc}, old_cuboids)
                  if is_inside(oc, nc):
                        return join(new_cuboids, old_cuboids - {oc})
                  if overlap(nc, oc):
                        ins, outs = add(nc, oc)
                        return join((new_cuboids - {nc}) | outs, (old_cuboids - {oc}) | ins) 
            return {nc} | join(new_cuboids - {nc}, old_cuboids)
      return new_cuboids | old_cuboids

def reboot(on_off, coords):
      cuboids = set()
      for on, c in zip(on_off, coords):
            if on: cuboids = join({c}, cuboids)
            if not on:
                  _cuboids = cuboids.copy()
                  for cc in cuboids:
                        if is_inside(c, cc):
                              break
                        if is_inside(cc, c):
                              _cuboids.remove(cc)
                        elif overlap(cc, c):
                              _cuboids.remove(cc)
                              _cuboids.update(subtract(cc , c))
                  cuboids = _cuboids
      return sum(size(c) for c in cuboids)

file_names = ['test1_input', 'test2_input', 'test3_input', 'main_input']
folder_name = './Day22/'
for file_name in file_names[:]:
      with open(folder_name + file_name) as input_file:
            on_off, coords = parse_input(input_file)
            print(f'Puzzle 1 for {file_name}: {initialization(on_off, coords)}')
            print(f'Puzzle 2 for {file_name}: {reboot(on_off, coords)}')