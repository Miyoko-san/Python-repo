l = [3, 45, 785, 489]

index = 0
for item in l:
    print(f"The item number at {index} is {item}")
    index += 1


# The same can be done by enumerate fn:


for index,item in enumerate(l):
    print(f"The item number at {index} is {item}")
