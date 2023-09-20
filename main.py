from mylib.logic import wiki

name = input("Enter a name: ")
print(wiki(name, 2)) if name.isalpha() else print(wiki("wondder woman", 2))
