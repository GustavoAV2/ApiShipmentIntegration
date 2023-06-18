
class CnabProcessor:
    def __init__(self, cnab_filename):
        self.cnab_filename = cnab_filename
        self.root_path = '../../input_shipment/'

    def process(self):
        cnab_data = {}
        header_data = {}
        detail_data = {}
        additional_data = {}

        with open(self.root_path + self.cnab_filename, 'r', encoding='ascii') as file:
            for line in file:
                register_type = line[0]
                print(register_type + " - " + line)

                if register_type == '0':
                    self._process_header(line, header_data)
                elif register_type == '1':
                    self._process_detail(line, detail_data)
                elif register_type == '2':
                    self._process_additional(line, additional_data)

        cnab_data['header_data'] = header_data
        cnab_data['detail_data'] = detail_data
        cnab_data['additional_data'] = additional_data

        return cnab_data

    @staticmethod
    def _process_header(line, data):
        data['register_type'] = line[0:1].strip()
        data['operation'] = line[1:2].strip()
        data['literal'] = line[2:9].strip()
        data['service_code'] = line[9:11].strip()
        data['service_literal'] = line[11:26].strip()
        data['ispb'] = line[26:34].strip()
        data['person_type'] = line[34:36].strip()
        data['cpf_cnpj'] = line[36:50].strip()
        data['agency'] = line[50:54].strip()
        data['account'] = line[54:74].strip()
        data['account_type'] = line[74:78].strip()
        data['pix_key'] = line[78:155].strip()
        data['generation_date'] = line[155:163].strip()
        data['convenio_code'] = line[163:193].strip()
        data['exclusive_psp'] = line[193:253].strip()
        data['name'] = line[253:353].strip()
        data['blank'] = line[353:731].strip()
        data['sequential_number'] = line[731:741].strip()
        data['version'] = line[741:744].strip()
        data['sequential_number_register'] = line[744:750].strip()

    @staticmethod
    def _process_detail(line, data):
        data['register_type'] = line[0:1].strip()
        data['identifier'] = line[1:36].strip()
        data['type_of_receiver'] = line[36:38].strip()
        data['cpf_cnpj_receiver'] = line[38:52].strip()
        data['receiver_agency'] = line[52:56].strip()
        data['receiver_account'] = line[56:76].strip()
        data['receiver_account_type'] = line[76:80].strip()
        data['pix_key'] = line[80:157].strip()
        data['billing_type'] = line[157:158].strip()
        data['occurrence_code'] = line[158:160].strip()
        data['expiration_timestamp'] = line[160:174].strip()
        data['expiration_date'] = line[174:182].strip()
        data['validity_after_expiry'] = line[182:186].strip()
        data['original_value'] = line[186:203].strip()
        data['debtor_person_type'] = line[203:205].strip()
        data['debtor_cpf_cnpj'] = line[205:219].strip()
        data['debtor_name'] = line[219:359].strip()
        data['payer_request'] = line[359:499].strip()
        data['exclusive_psp_receiver'] = line[499:559].strip()
        data['blank'] = line[559:744].strip()
        data['sequential_number'] = line[744:750].strip()

    @staticmethod
    def _process_additional(line, additional_data):
        additional_data['register_type'] = line[0:1].strip()
        additional_data['identifier'] = line[1:36].strip()
        additional_data['name_one'] = line[36:86].strip()
        additional_data['value_one'] = line[86:286].strip()
        additional_data['name_two'] = line[286:336].strip()
        additional_data['value_two'] = line[336:536].strip()
        additional_data['blank'] = line[536:744].strip()
        additional_data['sequential_number'] = line[744:750].strip()
