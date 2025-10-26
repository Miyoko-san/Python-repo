marks = {
    "Harry" : 100,
    "Miyoko" : 45,
    "Luffy" : 34
}


# .items() : gives key value pairs in tuples 
print(marks.items())

# .keys() : gives keys of the dict
print(marks.keys())

# .values()
print(marks.values())


# .update({key: updated value}) # hence dictionaries are mutable
marks.update({"Miyoko":77})
print(marks["Miyoko"])

# also used to include a new key-value pair in dict
marks.update({"Nami":69})
print(marks)


# .get()
print(marks.get("Miyoko"))
print(marks["Miyoko"])
   #Both seem to be same but are not 

print(marks.get("Robin")) # gives None as output
print(marks["Robin"])   # gives Error as output