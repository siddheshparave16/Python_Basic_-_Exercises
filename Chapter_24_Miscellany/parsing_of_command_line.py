import sys
import getopt
import shutil

if len(sys.argv) == 1:
    print('Incorrect usage')
    print('Correct usage: filecopy.py -s <source> -t<target>')
    sys.exit(1)

source = ''
target = ''

try:
    options, arguments = getopt.getopt(sys.argv[1:], 'hs:t:')
except getopt.GetoptError:
    print('filecopy.py -s <source> -t <target>')
else:
    for opt, arg in options:
        if opt == '-h':
            print('filecopy.py -s <source> -t <target>')
            sys.exit(2)
        elif opt == '-s':
            source = arg
        elif opt == '-t':
            target = arg
    else:
        print('Source file:', source)
        print('Target file:', target)
        if source and target:
            shutil.copyfile(source, target)















