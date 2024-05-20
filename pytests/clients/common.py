import random
import string

class Common:
    @staticmethod
    def incorrect_payload(incorrect_payloads):
        # Adicionado suporte para lidar com diferentes tipos de payloads incorretos
        if incorrect_payloads == "payload_vazio":
            return ""
        elif incorrect_payloads == "None":
            return None
        elif incorrect_payloads == "null":
            return "null"
        elif incorrect_payloads == "hash_vaio":
            return {}
        elif incorrect_payloads == "array_vazio":
            return []
        elif incorrect_payloads == "hash_vaio_string":
            return "{}"
        elif incorrect_payloads == "array_vazio_string":
            return "[]"
        elif incorrect_payloads == "payload_number":
            return 1
        elif incorrect_payloads == "payload_boolean_true":
            return True
        elif incorrect_payloads == "payload_boolean_false":
            return False
        else:
            # Caso nenhum dos tipos seja correspondido, retorne None ou outra ação apropriada
            return None  # Ou levante uma exceção, dependendo do comportamento desejado

    @staticmethod
    def values_change(value):
        # Adicionadas condições para alterar valores com base em padrões específicos
        if ".to_i" in value:
            return int(value.split('.')[0])
        elif "10.t_f" in value:
            return float(value.split('.')[0])
        elif value == 'None':
            return None
        elif value == 'boolean_true':
            return True
        elif value == 'boolean_false':
            return False
        elif ".characters_type_string" in value:
            letters = string.ascii_lowercase
            number = int(value.split('.')[0])
            return ''.join(random.choice(letters) for i in range(number))
        elif ".characters_type_numbers" in value:
            numbers = int(value.split('.')[0])
            return ''.join(random.choice("12346789") for i in range(numbers))
        elif value == "Array":
            return []
        elif value == "Hash":
            return {}
        else:
            return value

    @staticmethod
    def change_fields_payload(payload, field, value):
        # Adicionadas condições para alterar campos específicos em um payload
        count = field.count(".")
        if count == 1:
            fields = field.split(".")
            if type(payload.get(fields[0])) == list:
                payload[fields[0]][0][fields[1]] = Common.values_change(value)
            elif type(payload.get(fields[0])) == dict:
                payload[fields[0]][fields[1]] = Common.values_change(value)
        elif count == 2:
            fields = field.split(".")
            if type(payload.get(fields[0])) == list:
                payload[fields[0]][0][fields[1]][fields[2]] = Common.values_change(value)
            elif type(payload.get(fields[0], {}).get(fields[1])) == list:
                payload[fields[0]][fields[1]][0][fields[2]] = Common.values_change(value)
            elif type(payload.get(fields[0], {}).get(fields[1])) == dict:
                payload[fields[0]][fields[1]][fields[2]] = Common.values_change(value)
        else:
            payload[field] = Common.values_change(value)
        return payload

    @staticmethod
    def remove_fields_payload(payload, field):
        # Adicionadas condições para remover campos específicos de um payload
        count = field.count(".")
        if count == 1:
            fields = field.split(".")
            if type(payload.get(fields[0])) == list:
                del payload[fields[0]][0][fields[1]]
            elif type(payload.get(fields[0])) == dict:
                del payload[fields[0]][fields[1]]
        elif count == 2:
            fields = field.split(".")
            if type(payload.get(fields[0])) == list:
                del payload[fields[0]][0][fields[1]][fields[2]]
            elif type(payload.get(fields[0], {}).get(fields[1])) == list:
                del payload[fields[0]][fields[1]][0][fields[2]]
            elif type(payload.get(fields[0], {}).get(fields[1])) == dict:
                del payload[fields[0]][fields[1]][fields[2]]
        else:
            del payload[field]
        return payload
