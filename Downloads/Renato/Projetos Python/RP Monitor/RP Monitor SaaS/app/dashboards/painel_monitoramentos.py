
import streamlit as st
import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# Função integrada de busca de tweets com API do Twitter v2
def buscar_tweets(termo, data_inicial, data_final, max_results=10):
    url = "https://api.twitter.com/2/tweets/search/recent"
    headers = {
        "Authorization": f"Bearer {os.getenv('TWITTER_BEARER_TOKEN')}"
    }
    params = {
        "query": termo,
        "max_results": max_results,
        "tweet.fields": "created_at,text",
        "start_time": f"{data_inicial}T00:00:00Z",
        "end_time": f"{data_final}T23:59:59Z",
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get("data", [])
    else:
        st.error(f"Erro na requisição: {response.status_code} - {response.text}")
        return []

def painel_monitoramentos():
    st.title("📡 Monitoramentos")

    termo = st.text_input("Termo a Monitorar")
    data_inicial = st.date_input("Data Inicial", datetime.today()).strftime("%Y-%m-%d")
    data_final = st.date_input("Data Final", datetime.today()).strftime("%Y-%m-%d")
    limite = st.slider("Quantidade de resultados", min_value=1, max_value=100, value=10)

    if st.button("Buscar Tweets"):
        if not termo:
            st.warning("Por favor, insira um termo para monitorar.")
            return

        with st.spinner("Buscando dados..."):
            resultados = buscar_tweets(termo, data_inicial, data_final, limite)
            if resultados:
                st.success(f"{len(resultados)} resultados encontrados:")
                for post in resultados:
                    st.markdown(f"- {post['text']}")
            else:
                st.info("Nenhum resultado encontrado para o termo informado.")
