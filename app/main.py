from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

#create app
app = FastAPI(title="My API knowledege, Rockwell Automation, and Accenture")

# request body
class UserRequest(BaseModel):
    name: str
    age: int
    skills: List[str]

# Health check endpoint
@app.get("/")
def home():
    return {"message": "FastAPI is running successfully!"}

# Post endpoint to accept data
@app.post("/user_info")
def user_info(data: UserRequest):
    return {
        "message": "User data received",
        "name": data.name,
        "age": data.age,
        "skills": data.skills
    }

# 3. Example processing endpoint
@app.post("/score")
def calculate_score(data: UserRequest):
    score = len(data.skills) * 10

    return {
        "name": data.name,
        "score": score,
        "remark": "Good profile" if score > 20 else "Average profile"
    }

# 4. Example ML-style endpoint
@app.post("/predict-salary")
def predict_salary(data: UserRequest):
    predicted_salary = 30000 + (data.age * 500) + (len(data.skills) * 1000)
    return {
        "name": data.name,
        "predicted_salary": predicted_salary
    }


