
import streamlit as st
from datetime import datetime
from supabase import create_client

# Inicializa o cliente Supabase
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Limites por plano
LIMITES_POR_PLANO = {
    "free": {
        "clientes": 1,
        "analises": 100,
        "alertas": 0  # manual
    },
    "standard": {
        "clientes": 5,
        "analises": 2000,
        "alertas": -1  # -1 = sem limite
    },
    "pro": {
        "clientes": -1,
        "analises": -1,
        "alertas": -1
    }
}

def contar_registros(tabela, filtro_coluna, filtro_valor):
    response = supabase.table(tabela).select("id", count="exact").eq(filtro_coluna, filtro_valor).execute()
    return response.count if response and response.count is not None else 0

def verificar_limite(user_id, tipo, plano):
    limites = LIMITES_POR_PLANO.get(plano.lower(), {})
    if not limites:
        return False, "Plano inválido."

    if tipo == "clientes":
        total_clientes = contar_registros("clientes", "escritorio_id", user_id)
        limite = limites["clientes"]
        if limite != -1 and total_clientes >= limite:
            return False, f"Limite de {limite} cliente(s) atingido no plano {plano.capitalize()}."
        return True, f"{total_clientes}/{limite if limite != -1 else '∞'} clientes."

    if tipo == "analises":
        mes_atual = datetime.now().strftime("%Y-%m")
        response = supabase.rpc("contar_analises_por_mes", {"mes_ref": mes_atual, "uid": user_id}).execute()
        total = response.data if response and response.data else 0
        limite = limites["analises"]
        if limite != -1 and total >= limite:
            return False, f"Limite de {limite} análises/mês atingido."
        return True, f"{total}/{limite if limite != -1 else '∞'} análises neste mês."

    if tipo == "alertas":
        if limites["alertas"] == 0:
            return False, "Alertas automáticos não disponíveis no plano Free."
        return True, "Alertas automáticos habilitados."

    return False, "Tipo de verificação desconhecido."
