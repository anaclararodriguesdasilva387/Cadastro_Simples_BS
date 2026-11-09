import streamlit as st

#Inicialização das variáveis de estado 
st.title("Sistema de Cadastro")

#Tela de menu 
if st.session_state.pagina == "menu": 
    st.title("Menu Principal")
    st.write("Escolha uma opção: ")

#Tela de Cadastro 
#Tela de Login