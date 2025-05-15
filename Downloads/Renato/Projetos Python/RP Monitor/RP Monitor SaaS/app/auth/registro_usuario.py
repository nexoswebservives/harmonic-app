import streamlit as st
from supabase import create_client

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def registro_publico():
    st.title("📝 Criar Conta Gratuita")
    st.write("Registre-se para começar a usar o RP Monitor SaaS")

    email = st.text_input("E-mail")
    senha = st.text_input("Senha", type="password")

    if st.button("Registrar"):
        if not email or not senha:
            st.warning("Preencha todos os campos.")
            return

        try:
            result = supabase.auth.sign_up({"email": email, "password": senha})
            user = result.user
            if user:
                supabase.table("usuarios").insert({
                    "id": user.id,
                    "email": email,
                    "plano": "free",
                    "is_admin": False
                }).execute()
                st.success(f"Usuário {email} criado com sucesso! Faça login para continuar.")
            else:
                st.error("Erro ao registrar usuário.")
        except Exception as e:
            st.error(f"Erro ao registrar: {str(e)}")