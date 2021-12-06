from functools import cache

def final_number(remaining_times, final_time=80):
      number = cache(lambda rem, time: 1 if time <= rem else number(6, time-rem-1) + number(8, time-rem-1))
      return sum([number(rem, final_time) for rem in remaining_times])

file_names = ['test_input', 'main_input']
folder_name = './Day06/'
for file_name in file_names[:]:
      with open(folder_name + file_name) as input_file:
            ages = list(map(int, input_file.readline().strip().split(',')))
            print(f'Puzzle 1 for {file_name}: {final_number(ages)}')
            print(f'Puzzle 2 for {file_name}: {final_number(ages, 256)}')