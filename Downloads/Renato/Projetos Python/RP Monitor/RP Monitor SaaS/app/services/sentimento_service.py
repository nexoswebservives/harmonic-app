
import openai
import streamlit as st

def analisar_sentimento(texto):
    openai.api_key = st.secrets["openai_key"]

    prompt = f"Classifique o sentimento do seguinte texto como 'Positivo', 'Negativo' ou 'Neutro':\n\n"{texto}""

    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é um classificador de sentimentos."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=10,
            temperature=0
        )
        sentimento = resposta.choices[0].message["content"].strip()
        return sentimento
    except Exception as e:
        return f"Erro: {e}"
