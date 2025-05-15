
import streamlit as st
from utils.verificador_limites import verificar_limites

st.title("🔍 Teste de Limites - Plano Standard")

# Dados fictícios do usuário com plano Standard
usuario = {
    "email": "standard_user@rpmonitor.com",
    "plano": "standard",
    "clientes_ativos": 5,
    "analises_realizadas": 2000,
    "alertas_ativos": 1,
}

limites = verificar_limites(usuario)

st.write("**Limites do plano:**", limites)
