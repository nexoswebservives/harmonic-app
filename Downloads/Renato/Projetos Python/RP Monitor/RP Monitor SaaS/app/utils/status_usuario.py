from datetime import datetime
from supabase import create_client
import streamlit as st

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def marcar_usuario_online(user_id):
    try:
        supabase.table("usuarios").update({
            "last_active": datetime.utcnow().isoformat()
        }).eq("id", user_id).execute()
    except Exception as e:
        print("Erro ao marcar usuário online:", e)
