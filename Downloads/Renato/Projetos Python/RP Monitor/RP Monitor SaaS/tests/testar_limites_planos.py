import os
from utils.verificador_limites import dentro_limites
import streamlit as st

# Simulação de sessão para testes manuais
st.session_state['user_email'] = "free_user@rpmonitor.com"
st.session_state['plano'] = "free"
st.session_state['user_id'] = "teste_free_id"

# Testando limites de cliente
print("Testando limites de clientes para o plano FREE...")
for i in range(3):
    ok, msg = dentro_limites("clientes")
    print(f"Tentativa {i+1}: {'✅ OK' if ok else '❌ BLOQUEADO'} - {msg}")

# Testando limites de análises
print("\nTestando limites de análises para o plano FREE...")
for i in range(105):
    ok, msg = dentro_limites("analises")
    if i in [0, 99, 100, 104]:
        print(f"Análise {i+1}: {'✅ OK' if ok else '❌ BLOQUEADO'} - {msg}")

# Simulações semelhantes podem ser feitas para os planos standard e pro, com ajustes