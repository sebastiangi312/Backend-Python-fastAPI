from fastapi import FastAPI, File, UploadFile
from io import StringIO
from infrastructure.persistence.mongo.csv_repository import add
import pandas as pd

app = FastAPI()


@app.post("/upload")
def upload(file: UploadFile = File(...)):
    data = file.file.read().decode()
    df = pd.read_csv(StringIO(data))
    add(df.to_dict("records"))
    return {"message": f"Successfully uploaded {file.filename}"}
