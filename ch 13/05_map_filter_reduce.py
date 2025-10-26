from functools import reduce

# Map : applies a function to all the items in an input_list.

# syntax : map(fn, input_list)


l = [1, 2, 3 ,4 ,5]

square = lambda x: x*x

sqList = map(square,l)
print(list(sqList))


# Filter : creates a list of items for which the function returns true.

def even(n):
    if (n%2 == 0):
        return True
    return False

onlyEven = filter(even,l)       # filter(fn_name , input_list)
print(list(onlyEven))



# Reduce : applies a rolling computation to sequential pair of elements. 
# needs to be imported from functools

def sum(a,b):
    return a+b

print(reduce(sum,l))            # reduce(fn,input_list)

mul = lambda a,b: a*b
print(reduce(mul,l))