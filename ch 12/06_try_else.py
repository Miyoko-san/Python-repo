try:
    a = int(input("Please Enter a number : "))
    print(a)

 
except Exception as e:
    print(e)


else:
    print("I am inside else")   # will get executed iff try block works i.e. entered number will be an int

