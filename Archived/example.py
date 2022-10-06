# FILE OPERATIONS
'''file_handler1 = open("myfile.dat", "rb")
plaintext = file_handler1.read(16)
file_handler1.close()
int_val = int.from_bytes(plaintext, "big")
print("Plaintext : "+str(int_val))

file_handler2 = open("myfile1.dat", "wb")
file_handler2.write(int_val.to_bytes(16, 'big'))
file_handler2.close()

file_handler3 = open("myfile1.dat", "rb")
plaintext = file_handler3.read(16)
file_handler3.close()
int_val = int.from_bytes(plaintext, "big")
print("Plaintext New: "+str(int_val))
'''

# DIRECTORY AND FILES LISTING
""" import os
path="Archived/"
for files in [path+f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]:
    file_handler1 = open(files, "r")
    print(file_handler1.read())
    file_handler1.close()
    print(files)
    print(files.split("/")[-1]) """


# CREATE FILE INSIDE NEW DIR
'''
def create_open(path,mode):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return open(path, mode)
with create_open('inside1/myfiletxt2.txt','w') as f:
    f.write("HELLOOOO")'''

# READ FILE TILL LAST WITH PADDING
'''file_handler1 = open("myfile.dat", "rb")
while(True):
    plaintext = file_handler1.read(16)
    len_pt = len(plaintext)
    if not len_pt:
        break
    elif len_pt<16:
        zero=0
        plaintext += zero.to_bytes(16-len_pt, 'big') 
    #print(type(plaintext))
    int_val = int.from_bytes(plaintext, "big")
    print("Plaintext : "+str(hex(int_val)))
file_handler1.close()'''