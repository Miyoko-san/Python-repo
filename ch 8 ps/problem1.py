# Write a program using functions to find greatest of three numbers.




def greatest(a, b, c):
    if(a>b and a>c):
        return a 
    elif(b>a and b>c):
        return b 
    else:
        print(f"{c} is the gretaest number.")
    return c

a = int(input("Please Enter the number here : "))
b = int(input("Please Enter the number here : "))
c = int(input("Please Enter the number here : "))


print(greatest(a, b , c))