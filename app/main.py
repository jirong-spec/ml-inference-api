from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    x: float

@app.post("/predict")
def predict(data: InputData):
    y = data.x * 2
    return {"result": y}
