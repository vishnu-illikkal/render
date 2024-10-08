from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, this is a demo FastAPI site deployed on Render!"}

@app.get("/about")
def read_about():
    return {"message": "This is the about page."}
