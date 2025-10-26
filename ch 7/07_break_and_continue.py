# break

for i in range(100):
    if(i == 34):
        break # Exits the loop immediately
    print(i)


# continue

for i in range(100):
    if(i == 34):
        continue # skip this iteration and move forward
    print(i)


# pass

'''
for i in range(645):


i = 0 
while(1<45):
    print(i)
    i += 1
''' # to execute this program without woking on the 'for' loop use pass command

for i in range(645):
    pass # it instructs to do nothing

i = 0 
while(i<45):
    print(i)
    i += 1
