from fastapi import FastAPI
from .controllers import evaluate_payload

app = FastAPI()


@app.post("/eval")
def eval_model(payload: dict):
    return evaluate_payload(payload)
