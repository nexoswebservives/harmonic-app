
import streamlit as st
import pandas as pd

def painel_agencia():
    st.title("📊 Painel da Agência")

    dados_mock = pd.DataFrame([
        {"cliente": "Cliente A", "sentimento": "Positivo", "urgencia": "Alta"},
        {"cliente": "Cliente B", "sentimento": "Negativo", "urgencia": "Baixa"},
        {"cliente": "Cliente C", "sentimento": "Neutro", "urgencia": "Média"},
    ])

    st.dataframe(dados_mock)
