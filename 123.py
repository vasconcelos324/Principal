import streamlit as st
import pandas as pd
from datetime import datetime

# Criação dos dados
def extracao_bcb(codigo, inicio, fim):
    # Substituir espaços por %20
    inicio = inicio.strftime("%Y-%m-%d")
    fim = fim.strftime("%Y-%m-%d")
    
    url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{}/dados?formato=json&dataInicial={}&dataFinal={}'.format(codigo, inicio, fim)
    df = pd.read_json(url)
    df.set_index('data', inplace=True)
    df.index = pd.to_datetime(df.index, dayfirst=True)
    return df

# Criação do gráfico com Streamlit
def gerar_grafico(df, nome_serie):
    st.line_chart(df["valor"], use_container_width=True)
    st.title(f"{nome_serie}")

# Criação da Imagem/Titulo/Lista/Caixa da Lista/
def main():

    st.title("Consulta de Série Temporal do Banco Central")

    series_temporais = {
        "Indice de Vendas do Varejo": 1455,
        # ... (outras séries temporais)
    }

    opcao_serie = st.selectbox("Escolha uma série temporal:", list(series_temporais.keys()))

    codigo_serie = series_temporais[opcao_serie]

    # Permitindo entrada manual da data inicial
    data_inicial_input = st.text_input("Digite a data inicial (DD/MM/AAAA):")
    data_inicial = datetime.strptime(data_inicial_input, "%d/%m/%Y") if data_inicial_input else None

    # Permitindo entrada manual da data final
    data_final_input = st.text_input("Digite a data final (DD/MM/AAAA):")
    data_final = datetime.strptime(data_final_input, "%d/%m/%Y") if data_final_input else None

    if st.button("Consultar Série Temporal"):
        if data_inicial and data_final:
            df_resultado = extracao_bcb(codigo_serie, data_inicial, data_final)

            if not df_resultado.empty:
                # Layout em duas colunas
                
                
                    gerar_grafico(df_resultado, opcao_serie)
            else:
                st.warning("Não foram encontrados dados para a série temporal informada.")
        else:
            st.warning("Preencha todos os campos.")

if __name__ == "__main__":
    main()
