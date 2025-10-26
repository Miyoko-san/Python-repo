# writing a letter template
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>

letter = '''Dear <|Name|>,
    You are selected!
    <|Date|> '''
print(letter.replace("<|Name|>" , "Miyoko").replace("<|Date|>" , "27 June 2050"))
# here we have used Chaining of .replace() fn



