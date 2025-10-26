#Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

words = { 
    "Billi" : "Cat",
    "Kursi" : "Chair",
    "Kela" : "Banana"
}

word = input("Enter the hindi word : ")
# print(words[word])

print(words.get(word))