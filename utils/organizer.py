import sys
import os
from glob import glob
import shutil

folder = sys.argv[1]
prefix = sys.argv[2]

full_path = os.path.abspath(folder)

all_files = []
idx = 1
for suffix in ['png', 'jpg', 'jpeg']:
    for filename in glob( full_path + '/**/*.' + suffix, recursive=True):
        all_files.append((idx, filename, suffix))
        idx+=1

for idx, file, suffix in all_files:
    if prefix in os.path.basename(file):
        print('found prefix!' ,  os.path.basename(file) )
        sys.exit(1)
    dst = os.path.join(full_path, prefix + '_' + str(idx) + '.' + suffix)
    shutil.copy(file, dst)
