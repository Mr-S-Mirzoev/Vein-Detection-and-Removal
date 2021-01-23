from os import listdir, path

prefix = "/usr/include/x86_64-linux-gnu/qt5/"

for name in listdir(prefix):
    fullpath = path.join(prefix, name)
    if path.isdir(fullpath):
        print("\"{}\",".format(fullpath))
