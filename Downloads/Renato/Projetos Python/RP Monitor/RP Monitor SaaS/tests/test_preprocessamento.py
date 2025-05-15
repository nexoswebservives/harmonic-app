
import pytest
from processamento.preprocessamento import limpar_texto

def test_limpar_texto_remove_urls():
    texto = "Acesse http://exemplo.com"
    assert limpar_texto(texto) == "acesse"

def test_limpar_texto_remove_pontuacao():
    texto = "Bom dia!!! Como vai?"
    assert limpar_texto(texto) == "bom dia como vai"

def test_limpar_texto_espacos():
    texto = "   Isso     é   um teste.   "
    assert limpar_texto(texto) == "isso é um teste"
