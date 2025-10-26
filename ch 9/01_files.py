'''
when you write a program it gets strored in RAM of the computer and is temporarily there

RAM = Volatile 
HDD/SSD/Pendrive = Non-Volatile 

if you want to persist a program i.e. save and store it permanently in the disc space 
we use file'''


'''
types of files : 
1. text fles (in which we use textual characters to write): .py , .txt , .c
2. Binary files : .jpg , .png , .dat 
'''


# open("file_name.extension","mode") :
# a built in fn in python use to open a file
# mode : by default it is in read mode "r". "w" => write mode


f = open("file.txt")
data = f.read()
print(data)
f.close()    # close() fn tells python that the opened file no longer is still in our program