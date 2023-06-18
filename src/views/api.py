from fastapi import FastAPI, File
from fastapi.exceptions import HTTPException
from src.actions.shipment_actions import ShipmentActions

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Api em funcionamento!"}


@app.get("/process_shipment_file")
async def process_shipment_file(file=File()):
    if file:
        shipment_actions = ShipmentActions()
    raise HTTPException(status_code=400, detail="Insira um arquivo!")
