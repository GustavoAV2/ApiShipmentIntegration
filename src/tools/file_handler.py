import os


class FileManager:
    def __init__(self):
        self.root_path = 'input_shipment/'

    def write_file(self, filename, content):
        with open(self.root_path + filename, "w") as f:
            f.writelines(content)

    @staticmethod
    def get_filename(file_path):
        return os.path.basename(file_path)
