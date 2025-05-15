import streamlit as st
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

def login():
    if "logado" not in st.session_state:
        st.session_state.logado = False

    if not st.session_state.logado:
        st.title("Login")
        email = st.text_input("Email")
        password = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            try:
                user = supabase.auth.sign_in_with_password({"email": email, "password": password})
                st.success("Login bem-sucedido!")
                st.session_state.logado = True
                st.session_state.usuario = email
                st.rerun()  # força atualização da tela para exibir o menu principal
            except Exception:
                st.error("Credenciais inválidas ou erro de conexão.")
    return st.session_state.logado
