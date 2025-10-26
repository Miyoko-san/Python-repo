a = int(input("Please enter your age : "))

# if elif else ladder :

if(a>=18):
    # this tab is called indentation and implies we have entered into if fn
    print("You are above age of consent")
elif(a<=0):
    print("Please enter a valid age !")
else:
    print("You are below age of consent")

# elif and else can not work alone unlike if 