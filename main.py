from fastapi import FastAPI, Body
from grop_client import get_response

app = FastAPI()

@app.get("/requests")
def get_requests():
    return "Hello World"

@app.post("/requests")
def send_prompt(
    input: str = Body(embed=True)
):
    answer = get_response(input)
    return {"answer": answer}
    
