'''Четвертое задание'''

import os


files = []

for root, dirs, file in os.walk('./'):

    for my_file in file:
        file_path = os.path.join(root, my_file)
        files.append(os.stat(file_path).st_size)

max_size = max(files)

i = 1

out_dict = {}

for _ in range(len(str(max_size))):
    i *= 10
    out_dict[i] = 0



for my_file in files:
    out_dict[10 ** len(str(my_file))] += 1

print(out_dict)
