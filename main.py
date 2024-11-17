from fastapi import FastAPI
from  routes import users, ratings, recipes, comments;

app = FastAPI()

@app.get("/")
def read_root():
    return {"Exe": "Ntjaka"}

app.include_router(users.router, prefix="/users")