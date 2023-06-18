from uuid import uuid4
from src.actions.tasks import task_process_shipment_file
from fastapi import FastAPI, UploadFile, File, Body, BackgroundTasks
from fastapi.exceptions import HTTPException

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Api em funcionamento!"}


@app.post("/oauth/token")
async def request_token(payload=Body(...)):
    if payload:
        return {"access_token": uuid4()}
    return ""


@app.post("/process_shipment_file")
async def process_shipment_file(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    background_tasks.add_task(task_process_shipment_file, file=file)
    return {"status": "Adicionada a fila de processamento!"}
