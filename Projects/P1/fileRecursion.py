import os

path_base = os.getcwd() + '/testdir'

def find_files(path, suffix):
    if suffix == '':
        return []

    if len(os.listdir(path)) == 0:
        return []

    directory = os.listdir(path)
    files = []
    folders = []
    for elements in directory:
        if "."+suffix in elements:
            files.append(elements)
        elif "." not in elements:
            folders.append(elements)

    for folder in folders:
        files.append(find_files(path+"/"+folder, suffix))

    return files

print(find_files(suffix='c', path=path_base))
