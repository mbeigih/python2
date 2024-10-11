from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/random-number/")
def get_random_number():
    return {"random_number": random.randint(1, 100)}
