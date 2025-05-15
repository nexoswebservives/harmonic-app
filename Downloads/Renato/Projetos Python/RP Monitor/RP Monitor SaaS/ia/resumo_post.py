
from transformers import pipeline

# Carrega pipeline de resumo do Hugging Face
summarizer = pipeline("summarization")

def resumir_texto(texto):
    resumo = summarizer(texto, max_length=50, min_length=20, do_sample=False)[0]
    return resumo['summary_text']
