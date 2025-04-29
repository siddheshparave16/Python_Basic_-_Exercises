import sys
import shutil

# Command-line arguments

# program for coping content of one file to another file through command-line arguments
argc = len(sys.argv)

if argc != 3:
    print('Incorrect usage')
    print('Correct usage: filecopy source target')
else:
    source = sys.argv[1]
    target = sys.argv[2]
    shutil.copyfile(source,target)

r"""
# for get output of above program run this at terminal:

PS D:\Siddhesh_files\Let_Us_python> D:\Siddhesh_files\Let_Us_python\Chapter_24_Miscellany\Chapter_23_Miscellany.py D:\Siddhesh_files\Let_Us_python\Chapter_23_File_Input_Output\Chapter_23_Solve_Questions\messages.txt D:\Siddhesh_files\Let_Us_python\Chapter_23_File_Input_Output\Chapter_23_Solve_Questions\messages2.txt  
"""
































