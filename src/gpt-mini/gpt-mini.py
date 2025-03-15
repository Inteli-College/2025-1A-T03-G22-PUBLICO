import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
SITE_URL = os.getenv("YOUR_SITE_URL")
SITE_NAME = os.getenv("YOUR_SITE_NAME")


response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {API_KEY}",
    "HTTP-Referer": "<YOUR_SITE_URL>",
    "X-Title": "<YOUR_SITE_NAME>",
  },
  data=json.dumps({
    "model": "openai/gpt-4o-mini",
    "messages": [
      {
        "role": "user",
        "content": "O projeto de nuvem visa a implementação de uma plataforma escalável e segura para processamento e análise de editais públicos, utilizando um modelo de LLM (Large Language Model) para extração e síntese de requisitos técnicos e financeiros. A solução será hospedada em uma infraestrutura baseada em AWS, aproveitando serviços como S3 para armazenamento de documentos, Lambda para processamento serverless e DynamoDB para persistência de metadados. O sistema contará com uma interface web intuitiva desenvolvida com Streamlit, permitindo que os usuários façam upload de arquivos em diferentes formatos (PDF, DOCX, TXT) e recebam um resumo estruturado dos principais requisitos do edital. Entre os requisitos funcionais, destaca-se a necessidade de um mecanismo de extração e análise de texto com NLP, além de um banco de dados para armazenamento de históricos de consultas e análises anteriores. O sistema deve suportar múltiplos usuários, com autenticação via OAuth 2.0 e controle de permissões para diferentes níveis de acesso. Os requisitos não funcionais incluem alta disponibilidade, segurança de dados com criptografia em trânsito e repouso, e tempos de resposta otimizados para consultas em larga escala. A arquitetura deverá ser projetada para suportar picos de carga, utilizando Auto Scaling para garantir elasticidade e um balanceador de carga para distribuir as requisições. Em termos financeiros, o projeto deve considerar um modelo de custos baseado em consumo (pay-as-you-go), buscando otimizar o uso de recursos para minimizar despesas operacionais. O orçamento inicial contempla a utilização de instâncias EC2 spot para reduzir custos computacionais, além da integração com serviços gerenciados para evitar sobrecarga operacional. A solução também prevê um plano de contingência, com backup automatizado e recuperação de desastres via AWS Backup. A viabilidade financeira do projeto será avaliada periodicamente, garantindo que o ROI (Return on Investment) esteja alinhado com as expectativas da empresa e que a solução possa escalar de forma sustentável conforme o aumento da demanda. Com base no edital fornecido, identifique e resuma os requisitos técnicos e financeiros exigidos para participação. Liste os principais critérios técnicos e as exigências financeiras, destacando valores mínimos, garantias, certificações ou outras condições obrigatórias. Apresente as informações de forma clara e organizada."
      }
    ]
  })
)

print(response.json())  # Para visualizar a resposta da API
