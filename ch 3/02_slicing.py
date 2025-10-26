# skip value slicing x:y:z

a = "0123456789"
print(a[1:7:4])

# Explanation : first resolve print(a[1:7])  
#  this will yield 123456
# now include only fist character + 4 (in this case only once)
# this yields 15

