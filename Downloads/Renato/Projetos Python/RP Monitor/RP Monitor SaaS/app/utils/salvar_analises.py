
from utils.supabase_config import supabase
from datetime import datetime

def salvar_analises_supabase(user_id, monitoramento_id, resultados):
    for resultado in resultados:
        supabase.table("analises").insert({
            "user_id": user_id,
            "monitoramento_id": monitoramento_id,
            "conteudo": resultado["conteudo"],
            "sentimento": resultado["sentimento"],
            "data": datetime.utcnow().isoformat()
        }).execute()
