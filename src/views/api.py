from uuid import uuid4
from fastapi import FastAPI, UploadFile, File, Body
from fastapi.exceptions import HTTPException
from src.actions.shipment_actions import ShipmentActions

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
async def process_shipment_file(file: UploadFile = File(...)):
    shipment_actions = ShipmentActions()
    if shipment_actions.send_converted_file(file):
        return {"status": "Cobrança gerada com sucesso!"}
    raise HTTPException(status_code=400, detail="Insira um arquivo!")
