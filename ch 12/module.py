def myfunc():
    print("Hello World ! ")

myfunc()


# print(__name__)  # since it is used from this file only Output => __main__

# if imported from some other file => file name of the fn i.e. module




# if we don't want a piece of code to work if this code if imported somewhere else from it then we write it under __name__

if __name__ == "__main__":
    # If the code is directy executed by running the file its present in
    print("We are directly running this code")
    myfunc()
    print(__name__) 
    