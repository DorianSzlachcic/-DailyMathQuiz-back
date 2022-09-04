from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from math import floor

from .equation import generate_equation

app = FastAPI()

origins = [
    "http://127.0.0.1:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],
)


@app.get("/")
def homeApi():
    data = {}
    n = 2
    for i in range(1,11):
        data[i] = str(generate_equation(n, -2*i + 35))
        n += 1 if i % 4 == 0 else 0

    return data