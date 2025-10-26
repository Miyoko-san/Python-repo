# it is a mode to open a file and append a given string at the end of it as many 
# times as the program is run 

# open("file_name","a")

st = "I am good"

f = open("myfile.txt","a")
f.write(st)
f.close()