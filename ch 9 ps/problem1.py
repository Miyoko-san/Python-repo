f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("The given poem contains twinkle in it.")
else:
    print("The given poem does not contain twinkle in it.")
f.close()
