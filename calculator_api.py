
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

class Number(BaseModel):
    a: float
    b: float

@app.get("/")
def home():
    return "Hello welcome to the calculator API"

@app.post("/add")
def add(numbers: Number):
    result = numbers.a + numbers.b
    return {"result": result}

@app.post("/sub")
def sub(numbers: Number):
    result = numbers.a - numbers.b
    return {"result": result}

@app.post("/mul")
def mul(numbers: Number):
    result = numbers.a * numbers.b
    return {"result": result}

@app.post("/div")
def div(numbers: Number):
    if numbers.b == 0:
     raise HTTPException(
         status_code=400,
         detail="no valid division by 0"
)
    result = numbers.a / numbers.b
    return {"result": result}
@app.get("/greet")
def greet(name:str="SK"):
  return{"message":" myself"+name}
