from fastapi import FastAPI
import json

app = FastAPI()

def load_data():
    with open("patiens.json", "r") as f:
        data = f.read()
        return data

@app.get("/")
def hello():
    return {'message': 'Patient Management System API'}

@app.get("/about")
def about():
    return{'message': 'A fully functional API to manage your patient records'}

