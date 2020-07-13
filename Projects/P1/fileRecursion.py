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
    # print(folders)
    for folder in folders:
        new_files = find_files(path+"/"+folder, suffix)
        if new_files:
            files.append(new_files[0])
    return files

print(find_files(suffix='c', path=path_base))

# print(find_files(suffix='h', path=path_base))
#
# print(find_files(suffix='gitkeep', path=path_base))