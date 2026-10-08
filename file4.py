import json

student1 = {
    "name": "Sujit",
    "age": 20,
    "skills": ["Python", "SQL", "AI"]
}

data = json.dumps(student1)

student1 = json.loads(data)

print(type(data))
print(type(student1))
