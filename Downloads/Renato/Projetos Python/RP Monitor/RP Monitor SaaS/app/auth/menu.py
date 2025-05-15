import streamlit as st
import sys
import os

# Garante que o diretório pai esteja no sys.path para importações funcionarem corretamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dashboards.painel_cliente import painel_cliente
from admin.painel_admin import painel_admin
from boas_vindas import mostrar_boas_vindas
from auth.registro_usuario import registro_publico  # Corrigido
from utils.supabase_config import supabase

def render_menu():
    st.sidebar.title("🔍 Navegação")
    user_email = st.session_state.get("user_email")
    plano = st.session_state.get("plano", "desconhecido").lower()
    is_admin = st.session_state.get("is_admin", False)

    if user_email:
        st.sidebar.markdown(f"**Usuário:** {user_email}")
        st.sidebar.markdown(f"**Plano:** {plano.capitalize()}")

    # Menu padrão
    menu_options = ["Início"]

    # Menu por tipo de usuário
    if is_admin:
        menu_options += ["Painel Administrativo", "Gerenciar Usuários", "Relatórios"]
    elif plano == "pro":
        menu_options += ["Painel do Cliente", "Análises Avançadas", "Relatórios"]
    else:  # Free
        menu_options += ["Painel do Cliente", "Registrar Conta Pro"]

    escolha = st.sidebar.radio("Escolha uma seção", menu_options)

    # Roteamento
    if escolha == "Início":
        mostrar_boas_vindas()
    elif escolha == "Painel do Cliente":
        painel_cliente()
    elif escolha == "Painel Administrativo":
        painel_admin()
    elif escolha == "Registrar Conta Pro":
        registro_publico()
    elif escolha == "Gerenciar Usuários":
        st.info("⚙️ Funcionalidade de gerenciamento em construção.")
    elif escolha == "Análises Avançadas":
        st.info("🔍 Módulo Pro com IA avançada em desenvolvimento.")
    elif escolha == "Relatórios":
        st.info("📈 Relatórios estarão disponíveis em breve.")