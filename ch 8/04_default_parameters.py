def greet(name, ending = "Thank You"):  # if value of ending parameter is given then accepts that otherwise will print "Thank You"
    print(f"Good Day, {name} ") 
    print(ending)

greet("Miyoko")   # here ending = Thank You i.e. default parameter
greet("Luffy","Thanks")   # here ending = Thanks