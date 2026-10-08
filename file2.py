import json
student = {
    "name": "Sujit",
    "age": 20,
    "college": "Haldia Institute of Technology",
    "branch": "CSE",
    "skills": ["Python", "Java", "SQL"]
}
with open("student.json","w") as file:
     json.dump(student,file,indent=3)
