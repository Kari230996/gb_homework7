'''Первое задание'''

import os

my_values = ['settings','mainapp','adminapp','authapp']
my_keys = 'my_project'

for i in my_values:
    if not os.path.exists(os.path.join(my_keys, i)):
        dir_path = os.makedirs(os.path.join(my_keys, i))
        print(dir_path)

path = r'C:\Users\Deni\Downloads\python_gb\gb_homework7\my_project'

for root, dirs, files in os.walk(path):   # весь обзор папки my_project
    print(root)


