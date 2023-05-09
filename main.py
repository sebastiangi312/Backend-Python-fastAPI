from fastapi import FastAPI, File, UploadFile
from io import StringIO
from pymongo import MongoClient
import pandas as pd

app = FastAPI()
client = MongoClient('mongodb://localhost:27017/')
db = client['csvdb']
collection = db['csv_collection']

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    data = file.file.read().decode()
    df = pd.read_csv(StringIO(data))
    collection.insert_many(df.to_dict('records'))
    return {"message": f"Successfully uploaded {file.filename}"}