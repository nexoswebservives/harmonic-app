
def verificar_alerta(sentimento, urgencia):
    if sentimento == "NEGATIVE" and urgencia == "Alta":
        return True
    return False

def gerar_alerta(post):
    if verificar_alerta(post.get("sentimento"), post.get("urgencia")):
        return f"🚨 ALERTA: Post crítico detectado de {post.get('autor')} na fonte {post.get('fonte')}"
    return None
