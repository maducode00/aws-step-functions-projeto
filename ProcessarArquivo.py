import json
import uuid

def lambda_handler(event, context):
    dados = json.loads(event["Records"][0]["body"])
    
    resultado = {
        "id": str(uuid.uuid4()),
        "conteudo": dados,
        "status": "processado"
    }

    return resultado
