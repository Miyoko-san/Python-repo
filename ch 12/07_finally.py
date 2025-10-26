try:
    a = int(input("Please Enter a number : "))
    print(a)

 
except Exception as e:
    print(e)


finally:
    print("Hey, I am inside of finally")  # will get executed irrespective of result of try-except block



# how is it different from normal commands ?? in fns we can explain that 


def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return   # will not let the code below run if this piece runs successfully 

        
    except Exception as e:
        print(e) 
        return


    finally:   # will overwrite the return command and works unconditionally when the fn is called
        print("Hey I am inside of finally")