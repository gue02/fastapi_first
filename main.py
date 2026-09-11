from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : "Hello, World!"}

@app.get("/login")
def read_login():
    return {"message" : "Login.."}