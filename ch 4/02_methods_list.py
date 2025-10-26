friends = ["Apple", "Orange", 5 , 345.6 , False , "Aakash"  ]


#.append() : to add a new character at the end of the list
friends.append("Miyoko")
print(friends)
# .sort() : to sort a number list in increasing order
l1 = [23, 45, 33, 67, 78]
l1.sort()
print(l1)

# .reverse() : to get the list in reversed order
l1.reverse()
print(l1)

# .insert(index,element) : to add an element at a specific index
l1.insert(3,333)
print(l1)

# .pop(index) : to delete an element at an index
# when asked to print it will give the return value of the popped element
print(l1.pop(3))
print()

#.remove(element) : to directly remove an element
l1.remove(78)
print(l1)
