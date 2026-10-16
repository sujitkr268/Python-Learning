
import json

book = {
    "name": "Right way to think",
    "author": "Sujit kumar",
    "release date": 2026
}

data = json.dumps(book)
print(data)
print(type(data))

book1 = json.loads(data)
book2 = json.dumps(book1)

print(book1)
print(type(book1))

# Dictionary -> JSON file
with open("book2.json", "w") as file:
    json.dump(book1, file, indent=4)

# JSON file -> Dictionary
with open("book2.json", "r") as file:
    book3 = json.load(file)

    print(book3)
    print(type(book3))
    print(book3["author"])
