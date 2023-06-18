from src.actions.shipment_actions import ShipmentActions


def task_process_shipment_file(file):
    shipment_actions = ShipmentActions()
    shipment_actions.send_converted_file(file)
