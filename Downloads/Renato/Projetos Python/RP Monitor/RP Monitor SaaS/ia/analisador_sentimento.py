
from transformers import pipeline

# Carrega pipeline de sentimento do Hugging Face
sentiment_pipeline = pipeline("sentiment-analysis")

def analisar_sentimento(texto):
    resultado = sentiment_pipeline(texto)[0]
    return resultado['label'], resultado['score']
