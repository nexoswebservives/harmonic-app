
def usuario_logado():
    return "usuario" in st.session_state and st.session_state["usuario"] is not None

def obter_usuario():
    return st.session_state.get("usuario", {})
