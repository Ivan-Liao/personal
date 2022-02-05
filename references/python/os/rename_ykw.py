import os

BASE_ECH_PATH = os.path.join("D:",os.sep,"Downloads",'Others','MMCE_Win32','ecchi')

for root, dirs, files in os.walk(os.path.join(BASE_ECH_PATH)):
    # for dir in dirs:
    #     print(root, '+', dir)
    for file in files:
        if file.endswith('.zip'):
            if file.startswith('('):
                split_file = file.split(') ')
                os.rename(os.path.join(root,file), os.path.join(root,' '.join(split_file[1:])))
                print(f'renamed {file} to {split_file[1:]}')