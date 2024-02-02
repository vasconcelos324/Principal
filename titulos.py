import streamlit as st
import pandas as pd



st.title(" Preço do Tesouro Nacional ")
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


tipo_titulo = st.selectbox('Selecione o Tipo do Título', titulos.index.get_level_values(0).unique())
titulos_filtrados = titulos[titulos.index.get_level_values(0) == tipo_titulo]
data_vencimento = st.selectbox('Selecione a Data de Vencimento', titulos_filtrados.index.get_level_values(1).unique())
titulos_filtrados = titulos_filtrados[titulos_filtrados.index.get_level_values(1) == data_vencimento]
coluna_selecionada = st.selectbox('Selecione uma coluna', titulos_filtrados.columns)

col1, col2 = st.columns(2)
col1.dataframe(titulos_filtrados[[coluna_selecionada]])
col2.subheader(f"{coluna_selecionada}")
col2.line_chart(titulos_filtrados[coluna_selecionada].reset_index(drop=True))
col2.markdown("Fonte : Tesouro Direto ")



