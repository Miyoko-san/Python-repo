#  Write a recursive function to calculate the sum of first n natural numbers

'''
sum_n = n + n-1 + n-2 + ... + 2 + 1 

'''

n = int(input("Please enter the number of natural numbers : "))

def sum(n):
    if(n == 1):  # base condition : so that the fns does not keep calling it infinitely
        return 1
    return n + sum(n-1) # because of this condition the fn is a recursion 

print(sum(n))