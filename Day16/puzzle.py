from itertools import count
import operator as op
from functools import reduce

def parse(packet: str) -> tuple[int, dict]:
      version = int(packet[:3], 2)
      ID = int(packet[3:6], 2)
      if ID == 4:       # literal
            value = ''
            for i in count():
                  current = packet[6+5*i: 6+5*(i+1)]
                  value += current[1:]
                  if current[0] == '0':
                        value = int(value, 2)
                        break
            return 6 + 5 * (i + 1), {'version': version, 'ID': ID, 'value': value, 'sub': []}
      else:             # operator
            subs = []
            if packet[6] == '0':
                  n_bits = int(packet[7: 22], 2)
                  bit_read = 22
                  while bit_read < n_bits + 22:
                        br, sub = parse(packet[bit_read:])
                        bit_read += br
                        subs.append(sub)
            else:
                  n_sub = int(packet[7: 18], 2)
                  bit_read = 18
                  for i in range(n_sub):
                        br, sub = parse(packet[bit_read:])
                        bit_read += br
                        subs.append(sub)
      return bit_read, {'version': version, 'ID': ID, 'value': -1, 'sub': subs}
      
def total_version(packet: dict) -> int:
      return packet['version'] + sum([total_version(sub) for sub in packet['sub']])

def evaluate(packet: dict) -> int:
      operators = [sum, lambda x: reduce(op.mul, x), min, max, lambda: None,  op.gt, op.lt, op.eq]
      if packet['ID'] == 4: return packet['value']
      if packet['ID'] < 4: return (operators[packet['ID']])([evaluate(sub) for sub in packet['sub']])
      return int((operators[packet['ID']])(*[evaluate(sub) for sub in packet['sub']]))

file_names = ['test_input', 'main_input']
folder_name = './Day16/'
for file_name in file_names[:]:
      with open(folder_name + file_name) as input_file:
            for raw_hex in input_file.readlines():
                  packet = bin(int(raw_hex, 16))[2:].zfill(4*len(raw_hex.strip()))
                  _, parsed_packet = parse(packet)
                  print(f'Puzzle 1 for {file_name}: {total_version(parsed_packet)}')
                  print(f'Puzzle 2 for {file_name}: {evaluate(parsed_packet)}')