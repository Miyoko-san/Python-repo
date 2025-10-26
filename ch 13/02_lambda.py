# Lambda : to create fns in single line expressions


# syntax : 
'''
lambda arguments:expressions

it can be used as a nornal fn 

'''


'''
def square(n):
    print(n*n)

print(square(5))
'''

# the same can be done using lambda :


square = lambda x: x*x
print(square(5))


#Multiple arguments

sum =lambda a,b,c:a+b+c
print(sum(1,2,3))