# length of s after these operations?

s = set()
s.add('20') 
s.add(20)
s.add(20.0)

print(len(s)) # returs 2 as output

# this is because in python 1 == 1.0 

