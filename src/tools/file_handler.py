import os
from starlette.responses import FileResponse


class FileManager:
    INPUT_PATH = 'input_shipment/'
    SEND_PATH = 'send_shipment/'

    @staticmethod
    def write_file(filename, content, path):
        with open(path + filename, "w") as f:
            f.writelines(content.read().decode())

    @staticmethod
    def get_file(filename, path):
        return FileResponse(path, filename=filename)

    @staticmethod
    def get_filename(file_path):
        return os.path.basename(file_path)
