import os

ROOT_PATH = "F:\Anime"

for root, dirs, files in os.walk(os.path.join(ROOT_PATH)):
    for dir in dirs:
        if dir.startswith('['):
            os.rename(os.path.join(root,dir), os.path.join(root, ' '.join(dir.split(' ')[1:])))