import uuid
from src.actions.shipment_actions import ShipmentActions


def generate_file_id():
    return uuid.uuid4()


def task_process_shipment_file(file, file_id):
    shipment_actions = ShipmentActions()
    shipment_actions.send_converted_file(file, file_id)
