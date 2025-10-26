# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

class Class:
    a = "something"

hehe = Class()
hehe.a = 0
print(hehe.a)
print(Class.a)


# YES this change the class attribute

