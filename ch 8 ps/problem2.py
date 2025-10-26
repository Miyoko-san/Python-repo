# Write a python program using function to convert Celsius to Fahrenheit.

'''
C X 9/5 + 32 = F
'''

c = int(input("Enter the celcius temperature : "))

def conversion(c):
    f = (c * 9/5) + 32
    return f

print(f"the given temperature in farenheit is {conversion(c) }")

# round(variable_name , upto nth decimal place)

print(f"the given temperature in farenheit is {round(conversion(c) , 2) }")