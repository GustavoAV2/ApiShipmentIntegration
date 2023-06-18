import os

class FileManager:

    def write_file(self, filename, content, file_type, path):
        full_filename = f"{filename}.{file_type}"
        with open(path + "/" + full_filename, "w") as f:
            f.writelines(content)

    def generate_cnab_750(data):
        header = f'0{" " * 10}REMESSA{" " * 11}01COBRANCA       2047500000019000000000012345678901234NOME DA EMPRESA                  123BANCO DO BRASIL 12345678BRADESCO     06062201234567890RAZAO SOCIAL DA EMPRESA        12345678901234567890LOGRADOURO DO SACADO                                CIDADE                UF01234567890123456789012'
        trailer = f'9{" " * 10}{"0" * 6}{"0" * 6}{"0" * 10}{" " * 26}'

        detalhe = f'1{"A" * 9}{"A" * 20}{" " * 6}{"A" * 15}{" " * 6}{"A" * 15}{" " * 7}{"A" * 20}{" " * 15}{"0" * 5}{" " * 6}{"0" * 6}{"0" * 6}{" " * 7}{"0" * 3}{" " * 7}{"A" * 10}{" " * 40}{" " * 40}{" " * 40}'

        cnab_data = f'{header}\n{detalhe}\n{trailer}'

        return cnab_data

    @staticmethod
    def get_filename(file_path):
        return os.path.basename(file_path)
