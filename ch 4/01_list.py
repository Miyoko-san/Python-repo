# in lists we can store multiple types of data in a single list

friends = ["Apple", "Orange", 5 , 345.6 , False , "Aakash"  ]
print(friends[0])

#lists are mutable, unlike strings 

friends[0] = "Grapes"
print(friends[0])

print(friends[0:3])


# list of list is allowed in python 
l = [("harry",100), ("Miyoko",34 )]
print(type(l))
