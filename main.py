from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def enpoint():
    return "hello world"

@app.get('/2')
def enpoint():
    return "Hello i am double endpoind"