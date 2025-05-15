import streamlit as st
from dashboards.painel_cliente import painel_cliente
from dashboards.painel_agencia import painel_agencia
from dashboards.painel_monitoramentos import painel_monitoramentos
from dashboards.painel_admin import painel_admin
from auth.login import login
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="RP Monitor", layout="wide")

if login():
    st.sidebar.markdown("### Menu")
    pagina = st.sidebar.radio("Escolha uma seção:", ("Painel do Cliente", "Painel da Agência", "Monitoramentos"))

    if pagina == "Painel do Cliente":
        painel_cliente()
    elif pagina == "Painel da Agência":
        painel_agencia()
    elif pagina == "Monitoramentos":
        painel_monitoramentos()

    st.sidebar.button("Logout", on_click=lambda: st.session_state.clear())
