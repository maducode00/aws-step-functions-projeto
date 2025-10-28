
# Projeto AWS Step Functions

Este projeto implementa um fluxo de trabalho com AWS Step Functions para validar, processar e notificar arquivos enviados ao S3.

## 🚀 Objetivo

Automatizar o processamento de arquivos com validação, envio para fila, processamento, armazenamento e notificação.

## 🧩 Serviços Utilizados

- **AWS Lambda**: Funções para validação, processamento, armazenamento e notificação.
- **Amazon SQS**: Fila para tarefas pendentes.
- **Amazon DynamoDB**: Armazenamento dos resultados.
- **Amazon SNS**: Envio de notificações.
- **AWS Step Functions**: Orquestração do fluxo.
- **Amazon S3** (opcional): Armazenamento inicial dos arquivos.

## 📂 Estrutura de Pastas

aws-step-functions-projeto/ 
├── lambdas/
 ├── ValidarArquivo.py 
 ├── ProcessarArquivo.py 
 ├── SalvarNoDynamoDB.py 
 └── Notificar.py 
 ├── step-function.json 
 ├── README.md
 ├── .gitignore

 
## 📋 Como usar

1. Crie os recursos no Console da AWS com os nomes indicados.
2. Copie os códigos das funções Lambda para o console.
3. Importe o `step-function.json` na criação da máquina de estado.
4. Teste o fluxo enviando um arquivo para o S3 (se configurado).
5. Monitore a execução no Step Functions.

## 🛡️ Permissões

Certifique-se de que cada função Lambda tenha permissões adequadas via IAM:
- Acesso ao SQS, DynamoDB e SNS.
- Logs no CloudWatch.

## 📧 Notificações

O tópico SNS deve ter uma assinatura ativa (ex: e-mail) para receber os alertas.


