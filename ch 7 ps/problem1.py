# Write a program to print multiplication table of a given number using for loop

n = int(input("Please enter the number : "))

i = 1

for i in range (1,11):
    print(n*i)
    i += 1
print("Done !")


# to make this programm more understbale in the terminal 
for i in range (1,11):
    print(f"{n} x {i} = ", n*i)
    i += 1
print("Done !")