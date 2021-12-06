from functools import cache

@cache
def _final_number(age, final_time):
      if final_time <= age:
            return 1
      return _final_number(6, final_time - age - 1) + _final_number(8, final_time - age - 1)

def final_number(ages, final_time=80):
      return sum([_final_number(age, final_time) for age in ages])

file_names = ['test_input', 'main_input']
folder_name = './Day06/'
for file_name in file_names[:]:
      with open(folder_name + file_name) as input_file:
            ages = list(map(int, input_file.readline().strip().split(',')))
            print(f'Puzzle 1 for {file_name}: {final_number(ages)}')
            print(f'Puzzle 2 for {file_name}: {final_number(ages, 256)}')