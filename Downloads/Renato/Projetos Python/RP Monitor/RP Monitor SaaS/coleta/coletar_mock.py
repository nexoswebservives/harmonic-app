
import random

def gerar_post_fake():
    fontes = ["Twitter", "Facebook", "Instagram", "Site"]
    autores = ["João", "Maria", "Carlos", "Ana"]
    posts = [
        "A empresa está de parabéns pelo atendimento!",
        "Horrível, nunca mais compro!",
        "Serviço razoável, mas poderia melhorar.",
        "Adorei o novo produto lançado!",
        "Estou esperando retorno há dias!"
    ]
    return {
        "texto": random.choice(posts),
        "fonte": random.choice(fontes),
        "autor": random.choice(autores)
    }

def gerar_lote_posts(qtd=10):
    return [gerar_post_fake() for _ in range(qtd)]
