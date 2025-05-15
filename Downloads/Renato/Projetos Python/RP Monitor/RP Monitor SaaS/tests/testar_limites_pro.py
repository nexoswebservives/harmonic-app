
import streamlit as st
from utils.verificador_limites import verificar_limites

st.title("🔍 Teste de Limites - Plano Pro")

# Dados fictícios do usuário com plano Pro
usuario = {
    "email": "pro_user@rpmonitor.com",
    "plano": "pro",
    "clientes_ativos": 99,
    "analises_realizadas": 9999,
    "alertas_ativos": 999,
}

limites = verificar_limites(usuario)

st.write("**Limites do plano:**", limites)
