from fastapi import FastAPI, HTTPException
from models import User

app = FastAPI()

@app.post("/users/")
async def create_user(user: User):
    if user.age < 18:
        raise HTTPException(status_code=400, detail="User must be at least 18 years old.")
    return {"message": "User created successfully!", "user": user}

