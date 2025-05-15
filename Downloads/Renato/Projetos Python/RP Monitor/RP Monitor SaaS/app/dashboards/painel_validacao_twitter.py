# app/dashboards/painel_validacao_twitter.py

import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Validação Twitter API", layout="centered")

st.title("🔐 Validação da Chave da API do Twitter")

bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

if not bearer_token:
    st.error("❌ Bearer Token não encontrado no arquivo .env.")
else:
    headers = {"Authorization": f"Bearer {bearer_token}"}
    response = requests.get("https://api.twitter.com/2/tweets/search/recent?query=twitter", headers=headers)

    if response.status_code == 200:
        st.success("✅ Chave válida! Requisição à API do Twitter realizada com sucesso.")
        st.json(response.json())
    else:
        st.error(f"❌ Erro na requisição: {response.status_code} - {response.text}")
