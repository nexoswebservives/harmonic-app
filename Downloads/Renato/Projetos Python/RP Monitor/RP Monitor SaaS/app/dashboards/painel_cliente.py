import streamlit as st

def painel_cliente():
    st.title("📊 Painel do Cliente")

    # Simular dados visuais
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Menções", value="342", delta="+12 hoje")
    with col2:
        st.metric("Sentimento Positivo", value="78%", delta="+3%")
    with col3:
        st.metric("Alertas Críticos", value="2", delta="1 novo")

    st.markdown("---")
    st.subheader("📌 Últimos Alertas")
    st.warning("🚨 Palavra-chave 'crise' detectada em postagem no Twitter (há 15min).")
    st.info("📝 Novo post analisado com sentimento neutro no Instagram (há 32min).")

    st.markdown("---")
    st.subheader("🧪 Simulação")
    if st.button("🔁 Gerar Nova Simulação"):
        st.success("Simulação gerada com sucesso! (dados fictícios)")