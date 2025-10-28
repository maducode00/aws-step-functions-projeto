import boto3

sns = boto3.client('sns')
TOPICO_ARN = "arn:aws:sns:sa-east-1:123456789012:NotificacoesProcessamento"

def lambda_handler(event, context):
    mensagem = f"Processamento concluído para o ID: {event['id']}"
    sns.publish(TopicArn=TOPICO_ARN, Message=mensagem)
    return {
        "status": "notificado",
        "mensagem": mensagem
    }
