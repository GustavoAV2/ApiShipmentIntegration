import json
from uuid import uuid4
from src.actions.tasks import task_process_shipment_file
from src.actions.database_actions import DatabaseActions
from fastapi import FastAPI, UploadFile, File, Body, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware


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


@app.get("/<pix_url_access_token>")
async def request_pix_url(pix_url_access_token):
    return json.loads("example_data/pix_example.json")


@app.post("/oauth/token")
async def request_token(payload=Body(...)):
    if payload:
        return {"access_token": uuid4()}
    return ""


@app.post("/process_shipment_file")
async def request_process_shipment_file(background_tasks: BackgroundTasks, file: UploadFile = File(...)):
    background_tasks.add_task(task_process_shipment_file, file=file)
    return {"status": "Adicionada a fila de processamento!"}


@app.get("/historic")
async def request_shipment_historic():
    database_actions = DatabaseActions()
    return database_actions.get_all_historic()
