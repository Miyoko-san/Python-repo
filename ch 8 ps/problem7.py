# Write a python function to remove a given word from a list ad strip it at the same
# time.

l = ["Harry", "Rohan", "Shubhma", "an"]

def rem(l, word):
    n = []
    for item in l:
        if not(item == word):  # this means if item is not same as word or item != word
            n.append(item.strip(word))
    return n

print(rem(l , "an"))



# stip(): used to remove leading and trailing specified characters from a string
''' 
text = "###Welcome###"
cleaned = text.strip("#")
print(cleaned)

OUTPUT : Welcome
'''