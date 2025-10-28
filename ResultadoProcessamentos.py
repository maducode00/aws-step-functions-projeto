import boto3

dynamodb = boto3.resource('dynamodb')
tabela = dynamodb.Table('ResultadosProcessamento')

def lambda_handler(event, context):
    tabela.put_item(Item=event)
    return {
        "status": "salvo",
        "id": event["id"]
    }
