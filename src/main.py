from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from math import floor
import json

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

@app.get("/{eq_number}")
def homeApi(eq_number: int):
    eq = ""
    with open("equations.json","r") as file:
        json_object = json.load(file)
        print(json_object)
        eq = json_object[str(eq_number)]

    return eq
