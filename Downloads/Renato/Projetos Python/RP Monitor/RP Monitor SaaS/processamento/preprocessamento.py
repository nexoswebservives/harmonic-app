
import re

def limpar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r"http\S+|www\S+", "", texto)  # remove links
    texto = re.sub(r"[^a-zA-ZÀ-ÿ0-9\s]", "", texto)  # remove pontuação
    texto = re.sub(r"\s+", " ", texto).strip()  # remove espaços extras
    return texto
