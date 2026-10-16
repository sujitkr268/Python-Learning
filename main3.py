
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hi, this is Sujit Kumar, BTech student at HIT"
    }

class Student(BaseModel):
    name: str
    course: str

@app.post("/student")
def create_student(student: Student):
    return {
        "message": "Student of Haldia Institute of Technology, West Bengal",
        "name": student.name,
        "course": student.course
    }
