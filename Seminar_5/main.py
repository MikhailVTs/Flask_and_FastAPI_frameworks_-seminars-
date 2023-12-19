from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class User(BaseModel):
    id: int
    name: str
    email: str
    password: str

users = []

@app.get("/users", response_model=list[User])
async def get_users():
    return users

@app.get("/users/{id}", response_model=User)
async def get_user(id: int):
    for user in users:
        if user.id == id:
            return user

@app.post("/users", response_model=User)
async def add_user(user: User):
    users.append(user)
    return user

@app.put("/users/{id}", response_model=User)
async def update_user(id: int, user: User):
    for index, u in enumerate(users):
        if u.id == id:
            users[index] = user
            return user

@app.delete("/users/{id}")
async def delete_user(id: int):
    for index, user in enumerate(users):
        if user.id == id:
            del users[index]
            return {"message": "User deleted"}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "users": users})

# Для запуска используем команду: uvicorn main:app --reload