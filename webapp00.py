# MEU PRIMEIRO WEB APP
import streamlit as st
from ACTlib01 import *
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRHqHv4aSLz5e0n6Jm_sGmdsPjZEISusZCDDqvoO1WEetV2Afadsf10h8LG0txlOFi3Lqwg79uYXzjM/pub?gid=1409840764&single=true&output=csv"
db = Ler_GooglePlanilha(url)
Esvrever  (db)

# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("WEB APP H.H.O")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("INCTC.")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("GHOSTING")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

Divisor()
    
coluna1 = Colunas(3)
with coluna1[0]:
  Escrever("")
with coluna1[1]:
  Escrever("FEEDBACK", "titulo")
  nome = Ler(rotulo = "Nome:", nmax=30, tipo="padrao", info="NOME", autocompletar=None, na_mudanca=None, args=None, kwargs=None, placeholder="Não esqueça de preencher seu nome", desabilitada="falso", visibilidade="visivel")
  if nome:     
    Escrever("Seja Bem vinda(o), " + nome + "!")
with coluna1[2]:
  Escrever("")
