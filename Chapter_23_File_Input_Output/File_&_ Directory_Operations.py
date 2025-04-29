import os
import platform
import sys
import shutil

print("OS name:", os.name)
print("Platform:", sys.platform)
print("System:", platform.system())
print("Version:", platform.version())
print("Release:", platform.release())


print('\n')
print("Current Working Directory:", os.getcwd())

# represent current directory
print(os.listdir('.'))

# represent Parent of current directory
print(os.listdir('..'))


if os.path.exists('mydir'):
    print('mydir already exists')
else:
    os.mkdir('mydir')


# change the current working directory to the specified path
os.chdir('mydir')
print("Current Working Directory:", os.getcwd())

# os.makedirs('.\\dir1\\dir2\\dir3')

# create a file
f = open('myfile', 'w')
f.write('Having one child makes you a parent...')
f.write('Having two you are a referee')
f.close()


stats = os.stat('myfile')
#  gives the size of the file in bytes.
print('Size =', stats.st_size)

# rename the file
os.rename('myfile', 'yourfile')

shutil.copyfile('yourfile', 'ourfile')

# removing file from directory
os.remove('yourfile')

curpath = os.path.abspath('.')
print(curpath)


os.path.join(curpath, 'yourfile')

if os.path.isfile(curpath):
    print('Yourfile file exists')
else:
    print("Your file doesn't exist")

if os.path.isdir(curpath):
    print('Yourfile Directory exists')
else:
    print("Your Directory doesn't exist")




