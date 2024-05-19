#metodo contendo payload base pra a requisição

def payload_post():
    return {
        "name": {
            "name2": "teste",
            "years2": [
                {
                    "name3": "abc"
                }
            ]
        },
        "years": 20
    }