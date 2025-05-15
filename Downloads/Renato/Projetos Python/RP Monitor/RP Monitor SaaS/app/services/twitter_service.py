
import os
import requests
from dotenv import load_dotenv

# Carrega variáveis de ambiente do .env
load_dotenv()
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

def buscar_tweets(termo, data_inicial=None, data_final=None, max_resultados=10):
    url = "https://api.twitter.com/2/tweets/search/recent"
    
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }

    query = {
        "query": termo,
        "max_results": max_resultados,
        "tweet.fields": "created_at,text,author_id"
    }

    if data_inicial:
        query["start_time"] = f"{data_inicial}T00:00:00Z"
    if data_final:
        query["end_time"] = f"{data_final}T23:59:59Z"

    response = requests.get(url, headers=headers, params=query)

    if response.status_code == 200:
        dados = response.json()
        return [tweet["text"] for tweet in dados.get("data", [])]
    else:
        raise Exception(f"Erro na requisição: {response.status_code} - {response.text}")
