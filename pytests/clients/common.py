import random
import string

class Common:

    @staticmethod
    def incorrect_payload(incorret_payloads):
        match incorret_payloads:
            case "payload_vazio":
                return ""
            case "None":
                return None
            case "null":
                return "null"
            case "hash_vaio":
                return {}
            case "array_vazio":
                return []
            case "hash_vaio_string":
                return "{}"
            case "array_vazio_string":
                return "[]"
            case "payload_number":
                return 1
            case "payload_boolean_true":
                return True
            case "payload_boolean_false":
                return False

    @staticmethod
    def values_change(value):
        if ".to_i" in value:
            return int(value.split('.')[0])
        elif "10.t_f" in value:
            return float(value.split('.')[0])
        elif value == 'None':
            return None
        elif value == 'numer_negative':
            return -1
        elif value == 'boolean_true':
            return True
        elif value == 'boolean_false':
            return False
        elif ".characters_type_string" in value:
            letters = string.ascii_lowercase
            number = int(value.split('.')[0])
            return (''.join(random.choice(letters) for i in range(number)))
        elif ".characters_type_numbers" in value:
            numbers = int(value.split('.')[0])
            return (''.join(random.choice("12346789") for i in range(numbers)))
        elif value == "Array":
            return []
        elif value == "Hash":
            return {}
        else:
            return value
