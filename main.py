from mylib.logic import wiki

name = input("Enter a name: ")

if name and name.isalpha:
    print(wiki(name, 2)) 
else:
    print(wiki("wondder woman", 2))
