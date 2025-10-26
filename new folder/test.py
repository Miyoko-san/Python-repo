dict = {
    "banana":"kela",
    "apple":"seb"
}

word = input("Enter the work you want to translate: ")

print(f"The translation of the word is {dict.get(word.lower())}")

