# Check that a tuple type cannot be changed in python

a = (34, 45, 23, 18)

a[2] = "Miyoko"
print(a)

# TypeError: 'tuple' object does not support item assignment