
import streamlit as st

def painel_admin():
    st.title("⚙️ Painel Administrativo")
    st.write("Gerencie usuários, planos e permissões (simulado).")

    # Dados simulados
    usuarios = [
        {
            "nome": "Alice Santos",
            "email": "alice@email.com",
            "status": "Online",
            "plano": "Free",
            "ultima_analise": "2025-05-09 14:23",
            "total_analises": 3
        },
        {
            "nome": "Bruno Lima",
            "email": "bruno@email.com",
            "status": "Offline",
            "plano": "Pro",
            "ultima_analise": "2025-05-10 08:41",
            "total_analises": 27
        },
        {
            "nome": "Clara Nogueira",
            "email": "clara@email.com",
            "status": "Online",
            "plano": "Standard",
            "ultima_analise": "2025-05-10 10:02",
            "total_analises": 12
        }
    ]

    for usuario in usuarios:
        with st.expander(f"👤 {usuario['nome']} ({usuario['email']})", expanded=False):
            st.write(f"**Status:** {usuario['status']}")
            st.write(f"**Plano atual:** {usuario['plano']}")
            st.write(f"**Última análise:** {usuario['ultima_analise']}")
            st.write(f"**Total de análises:** {usuario['total_analises']}")

            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button(f"🔼 Upgrade ({usuario['email']})"):
                    st.success(f"Plano de {usuario['nome']} atualizado (simulado).")
            with col2:
                if st.button(f"🔽 Downgrade ({usuario['email']})"):
                    st.warning(f"Plano de {usuario['nome']} reduzido (simulado).")
            with col3:
                if st.button(f"⛔ Banir ({usuario['email']})"):
                    st.error(f"{usuario['nome']} foi banido (simulado).")

    st.markdown("---")
    st.info("Futuramente: botão de suporte ou chat integrado.")
