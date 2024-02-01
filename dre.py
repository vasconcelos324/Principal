import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import mplcyberpunk
plt.style.use('cyberpunk')

st.title('DRE')
with st.sidebar:
        st.header("pegar planilha")
        planilhas=st.file_uploader('Carregar Planilha',type="xlsx",accept_multiple_files=True)


        if planilhas:
         selecione = st.selectbox("Escolha a Empresa a visualizar", options=[f.name for f in planilhas])
        for planilha in planilhas:
            if planilha.name == selecione:
                   df = pd.read_excel(planilha)
                   df.set_index("DRE Consolidado",inplace=True)
                   
coluna = st.multiselect("Selecione o Trimestre ", df.columns)
filtro = df[coluna] if coluna else df
indice = st.multiselect("Selecione a Conta do DRE", df.index)
if indice:
   filtros = filtro.loc[indice]


if not filtros.empty:
    st.header("Gráfico da Seleção")
    fig, ax = plt.subplots(figsize=(15, 5))  # Ajuste os valores conforme necessário
    filtros.plot(kind='bar', ax=ax)
    plt.xticks(rotation=0)  # Faz a legenda do eixo x ficar horizontal
    plt.legend(loc='upper right', fontsize=8)  # Diminui ainda mais o tamanho da legenda
    st.pyplot(fig)








