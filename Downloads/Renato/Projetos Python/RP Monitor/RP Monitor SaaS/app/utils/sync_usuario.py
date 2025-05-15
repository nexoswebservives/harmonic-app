
from supabase import create_client
from utils.supabase_config import supabase

def sincronizar_usuario(user_id, email, nome=None):
    dados = {
        "id": user_id,
        "email": email,
    }
    if nome:
        dados["nome"] = nome

    # Verifica se já existe
    existe = supabase.table("usuarios").select("id").eq("id", user_id).execute()

    if existe.data:
        supabase.table("usuarios").update(dados).eq("id", user_id).execute()
    else:
        supabase.table("usuarios").insert(dados).execute()
