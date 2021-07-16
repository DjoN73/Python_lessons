import os

dirs = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}


def make_dirs(f_dir):
    for key, val in f_dir.items():
        if not os.path.exists(key):
            for i in range(len(val)):
                os.makedirs(os.path.join(key, val[i]))


make_dirs(dirs)
