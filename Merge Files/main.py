import os, os.path
from time import clock_getres
path_input_files= "input_files/"
output_file = open("output_file","wb")
file_list = sorted([path_input_files+f for f in os.listdir(path_input_files) if os.path.isfile(os.path.join(path_input_files,f))])
print("Files are going to be merged in following order :\n"+"-"*44)
print(file_list)
print("To continue enter 'Yes'")
a = input()
if not (a=="Y" or a=="y" or a=="Yes" or a=="YES" or a=="yes"):
    print("\033[1;31mProgram Terminated\033[0m")
    exit()
print("\033[1;32mMerging Started\033[0m")
for input_files in file_list:
    print("Merging file : "+input_files)
    with open(input_files, "rb") as input_file:
        while(True):
            data = input_file.read(1024*1024) # to read and write 1MB chunks
            len_data = len(data)
            if not len_data:
                break
            else:
                output_file.write(data)
print("\033[1;32mMerging Finished\033[0m")
output_file.close()