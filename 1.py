import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(layout="wide")


@st.cache_data
def busca_titulos_tesouro_direto():
    url = 'https://www.tesourotransparente.gov.br/ckan/dataset/df56aa42-484a-4a59-8184-7676580c81e3/resource/796d2059-14e9-44e3-80c9-2d9e30b405c1/download/PrecoTaxaTesouroDireto.csv'
    df  = pd.read_csv(url, sep=';', decimal=',')
    df['Data Vencimento'] = pd.to_datetime(df['Data Vencimento'], dayfirst=True)
    df['Data Base']       = pd.to_datetime(df['Data Base'], dayfirst=True)
    multi_indice = pd.MultiIndex.from_frame(df.iloc[:, :3])
    df = df.set_index(multi_indice).iloc[: , 3:]  
    return df

titulos = busca_titulos_tesouro_direto()
titulos.sort_index(inplace=True)

# Selecionar 'Tipo do Título'
tipo_titulo = st.selectbox('Selecione o Tipo do Título', titulos.index.get_level_values(0).unique())

# Filtrar DataFrame com base no 'Tipo do Título'
titulos_filtrados = titulos[titulos.index.get_level_values(0) == tipo_titulo]

# Selecionar 'Data de Vencimento'
datas_vencimento = st.multiselect('Selecione a(s) Data(s) de Vencimento', titulos_filtrados.index.get_level_values(1).unique())

# Filtrar DataFrame com base na 'Data de Vencimento'
titulos_filtrados = titulos_filtrados[titulos_filtrados.index.get_level_values(1).isin(datas_vencimento)]

# Selecionar uma das colunas restantes
coluna_selecionada = st.selectbox('Selecione uma coluna', titulos_filtrados.columns)

# Criar colunas
col1, col2 = st.columns(2)

# Exibir DataFrame filtrado com apenas a coluna selecionada na primeira coluna
col1.dataframe(titulos_filtrados[[coluna_selecionada]])

# Exibir gráfico de linha da coluna selecionada na segunda coluna usando Plotly
fig = px.area(titulos_filtrados.reset_index(), x='Data Base', y=coluna_selecionada, color='Data Vencimento', title=coluna_selecionada)
fig.update_layout(autosize=False, width=1500, height=400)
col2.plotly_chart(fig)
col2.markdown("Fonte : Tesouro Direto")

