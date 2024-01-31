import streamlit as st
import pandas as pd
from datetime import datetime

# Criação dos dados
def extracao_bcb(codigo, inicio, fim):
    inicio_str = inicio.strftime("%Y-%m-%d")
    fim_str = fim.strftime("%Y-%m-%d")
    
    url = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados?formato=json&dataInicial={inicio_str}&dataFinal={fim_str}'
    df = pd.read_json(url)
    df.set_index('data', inplace=True)
    df.index = pd.to_datetime(df.index, dayfirst=True)
    return df

# Criação do gráfico com Streamlit
def gerar_grafico(df, nome_serie):
    st.line_chart(df["valor"], use_container_width=True)
    st.title(f"{nome_serie}")

# Criação da Imagem/Título/Lista/Caixa da Lista/
def main():
    
    st.title("Consulta de Série Temporal do Banco Central")

    # Permitindo que o usuário insira a série temporal
    codigo_serie = st.text_input("Insira o código da série temporal:")

    # Permitindo entrada manual da data inicial
    data_inicial_input = st.text_input("Digite a data inicial (DD/MM/AAAA):")
    data_inicial = datetime.strptime(data_inicial_input, "%d/%m/%Y") if data_inicial_input else None

    # Permitindo entrada manual da data final
    data_final_input = st.text_input("Digite a data final (DD/MM/AAAA):")
    data_final = datetime.strptime(data_final_input, "%d/%m/%Y") if data_final_input else None

    if st.button("Consultar Série Temporal"):
        if codigo_serie and data_inicial and data_final:
            df_resultado = extracao_bcb(codigo_serie, data_inicial, data_final)

            if not df_resultado.empty:
                # Layout em duas colunas
                col1, col2 = st.columns(2)

                # Coluna 1: Exibindo a planilha
                with col1:
                    st.dataframe(df_resultado)

                # Coluna 2: Exibindo o gráfico
                with col2:
                    gerar_grafico(df_resultado, f"Série Temporal {codigo_serie}")
            else:
                st.warning("Não foram encontrados dados para a série temporal informada.")
        else:
            st.warning("Preencha todos os campos corretamente.")

if __name__ == "__main__":
    main()
