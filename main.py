from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def enpoint():
    return "hello world"