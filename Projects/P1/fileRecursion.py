import os

path_base = os.getcwd() + '/testdir'

def find_files(path, suffix):
    if suffix == '':
        return

    if len(os.listdir(path)) == 0:
        return

    directory = os.listdir(path)
    files = []
    folders = []
    for elements in directory:
        if "."+suffix in elements:
            files.append(path+"/"+elements)
        elif "." not in elements:
            folders.append(elements)

    for folder in folders:
        new_files = find_files(path+"/"+folder, suffix)
        if new_files:
            files.append(new_files[0])
    if len(files) == 0:
        return None
    return files

if __name__ == "__main__":
    print(find_files(suffix='c', path=path_base)) #./testdir/subdir1/a.c, ./testdir/t1.c, ./testdir/subdir3/subsubdir1/b.c,

    print(find_files(suffix='h', path=path_base)) #./testdir/subdir1/a.h, ./testdir/t1.h, ./testdir/subdir3/subsubdir1/b.h

    print(find_files(suffix='gitkeep', path=path_base)) #./testdir/subdir2/.gitkeep, ./testdir/subdir4/.gitkeep

    print(find_files(suffix="a", path=path_base)) #None