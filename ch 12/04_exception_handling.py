'''
a = int(input("Please Enter a number : "))

print(a)

# if not entered anumber :
 # ValueError: invalid literal for int() with base 10: 'd'
'''

# To avoid displaying this error , we use :


try:
    a = int(input("Please Enter a number : "))
    print(a)

# if a entered is not int i.e. error occurs ,then programm will move to except condition :

except Exception as e:
    print(e)

# invalid literal for int() with base 10: 'hh' => Output


# specific exception handlling : as earlier it was a ValueError


try:
    a = int(input("Please Enter a number : "))
    print(a)

except ValueError as v:
    print("ValueError Occured")
    print(v)


# for rest of the errors we do : 
except Exception as e:
    print(e)