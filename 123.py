import streamlit as st
import pandas as pd

# Criação dos dados
def extracao_bcb(codigo, inicio, fim):
    url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json&dataInicial={}&dataFinal={}'.format(codigo, inicio, fim)
    df = pd.read_json(url)
    df.set_index('data', inplace=True)
    df.index = pd.to_datetime(df.index, dayfirst=True)
    return df

# Criação do gráfico com Streamlit
def gerar_grafico(df, nome_serie):
    st.title(f"{nome_serie}")
    st.line_chart(df["valor"], use_container_width=True)
    

# Criação da Imagem/Titulo/Lista/Caixa da Lista/
def main():
    
    
    st.title("Consulta de Série Temporal do Banco Central")

    series_temporais = {
        "Indice de Vendas do Varejo": 1455,
        # ... (outras séries temporais)
    }

    opcao_serie = st.selectbox("Escolha uma série temporal:", list(series_temporais.keys()))

    codigo_serie = series_temporais[opcao_serie]

    data_inicial = st.date_input("Selecione a data inicial:")
    data_final = st.date_input("Selecione a data final:")

    if st.button("Consultar Série Temporal"):
        if data_inicial and data_final:
            df_resultado = extracao_bcb(codigo_serie, data_inicial, data_final)

            if not df_resultado.empty:
                st.dataframe(df_resultado)
                gerar_grafico(df_resultado, opcao_serie)
            else:
                st.warning("Não foram encontrados dados para a série temporal informada.")
        else:
            st.warning("Preencha todos os campos.")

if __name__ == "__main__":
    main()
