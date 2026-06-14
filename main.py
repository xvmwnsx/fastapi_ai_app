from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/requests")
def get_requests():
    return {"data": task}