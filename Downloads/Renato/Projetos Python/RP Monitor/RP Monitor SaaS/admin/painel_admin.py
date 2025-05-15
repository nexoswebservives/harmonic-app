
import streamlit as st
from utils.supabase_config import supabase
from datetime import datetime

def painel_admin():
    st.title("🔐 Painel Administrativo")

    try:
        usuarios_resp = supabase.table("usuarios").select("*").execute()
        usuarios = usuarios_resp.data
    except Exception as e:
        st.error(f"Erro ao carregar usuários: {e}")
        return

    if not usuarios:
        st.info("Nenhum usuário encontrado.")
        return

    for usuario in usuarios:
        with st.container():
            st.subheader(usuario.get("nome", "Sem Nome"))
            st.markdown(f"📧 **Email**: {usuario.get('email', 'Não informado')}")
            st.markdown(f"📦 **Plano**: `{usuario.get('plano', 'desconhecido')}`")
            st.markdown(f"📊 **Total de análises**: `{usuario.get('total_analises', 0)}`")
            ultima = usuario.get("last_active")
            ultima_fmt = datetime.fromisoformat(ultima).strftime("%d/%m/%Y %H:%M") if ultima else "Não registrado"
            st.markdown(f"🕒 **Última Atividade**: {ultima_fmt}")
            status = "🟢 Online" if ultima else "⚪ Offline"
            st.markdown(f"🔄 **Status**: {status}")
            with st.expander("⚙️ Ações"):
                plano = st.selectbox("Alterar Plano", ["gratuito", "standard", "pro"], index=["gratuito", "standard", "pro"].index(usuario.get("plano", "gratuito")), key=f"plano_{usuario['id']}")
                if st.button("Salvar Alterações", key=f"btn_{usuario['id']}"):
                    try:
                        supabase.table("usuarios").update({"plano": plano}).eq("id", usuario["id"]).execute()
                        st.success("Plano atualizado com sucesso.")
                    except Exception as e:
                        st.error(f"Erro ao atualizar plano: {e}")
