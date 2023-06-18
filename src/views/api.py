from uuid import uuid4

from src.actions.shipment_actions import ShipmentActions
from src.actions.tasks import task_process_shipment_file, generate_file_id
from src.actions.database_actions import DatabaseActions
from fastapi import FastAPI, UploadFile, File, BackgroundTasks, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Api em funcionamento!"}


@app.post("/oauth/token")
async def request_token(payload=Body(...)):
    if payload:
        return {"access_token": uuid4()}
    return ""


@app.post("/process_shipment_file")
async def request_process_shipment_file(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    file_id = generate_file_id()
    background_tasks.add_task(task_process_shipment_file, file=file, file_id=file_id)
    return {"status": "Adicionada a fila de processamento!", "file_id": file_id}


@app.get("/historic")
async def request_shipment_historic():
    database_actions = DatabaseActions()
    return database_actions.get_all_historic()


@app.get("/download/<file_id>")
def download_file(file_id: str):
    shipment_actions = ShipmentActions()
    return shipment_actions.download_file_data_shipment(file_id)
