'''Третье задание'''

import os
import shutil

my_values = ['settings','mainapp','adminapp','authapp', 'templates']
my_keys = 'my_project'

for i in my_values:
    if not os.path.exists(os.path.join(my_keys, i)):
        dir_path = os.makedirs(os.path.join(my_keys, i))

if not os.path.isdir('my_project\\templates\\authapp') and not os.path.isdir('my_project\\templates\\mainhapp'):
    dir_1 = shutil.copytree('my_project\\authapp\\templates\\authapp', 'my_project\\templates\\authapp')
    dir_2 = shutil.copytree('my_project\\mainapp\\templates\\mainapp', 'my_project\\templates\\mainhapp')

path = r'C:\Users\Deni\Downloads\python_gb\gb_homework7\my_project\templates'

for root, dirs, files in os.walk(path): # весь обзор папки my_project/templates
    print(root)



