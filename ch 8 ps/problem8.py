# Write a python function to print multiplication table of a given number.

n = int(input("Please enter the number : "))

def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
        
print(table(n))