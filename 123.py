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
    st.line_chart(df["valor"], use_container_width=True)
    st.title(f"{nome_serie}")

# Criação da Imagem/Titulo/Lista/Caixa da Lista/
def main():
    image = "logo-bcb.svg"
    st.image(image, use_column_width=True)
    st.title("Consulta de Série Temporal do Banco Central")

    series_temporais = {
        "Indice de Vendas do Varejo": 1455,
         "Indice de Confiança do Consumidor":4393,
        "Indice de Confiança do Empresario Industrial":7341,
        "Indice do Preço ao consumidor":13522,
        "Indice de Comodite Brasil (IC-BR)":27574,
        "Indice de Comodite Brasil-Metal":27576,
        "Indice de Comodite Brasil- Energia":27577,
        "SELIC":1178,
        "Vendas de Veiculos - Carro Pequeno":7384,
        "Vendas de Veiculos - Comercias Leves - Hilux/Toro":7385,
        "Vendas de Veiculos - Caminhões":7386,
        "Vendas de Veiculos - Onibus":7387,
        "Vendas de Veiculos - Maquina Agrìcolas":7388,
        "Vendas de Veiculos - Motociclos":1381,
        "Vendas de Veiculos - Total - Pequeno/Comerciais/Motociclos":1377,
        "Produção de Veiculos - Comercias Leves":1374,
        "Produção de Veiculos - Caminhões":1375,
        "Produção de Veiculos - Onibus":1376,
        "Produção de Veiculos - Maquina Agrìcolas":1376,
        "Produção de Veiculos - Motociclos":1388,
        "Produção de Veiculos Automotivo Total":1373,
        "Produção de Derivado do Petroleo - Óleo Bruto Barris/dia (mil)":1389,
        "Produção de Derivado do Petroleo - LGN Barris/dia (mil)":1390,
        "Produção de Derivado do Petroleo - Gás Naturual Barris/dia (mil)":1392,
        "Produção de Derivado do Petroleo - Total Barris/dia (mil)": 1391,
        "Produção de Derivado do Petroleo - Gasolina Barris/dia (mil)":1393,
        "Produção de Derivado do Petroleo - Gás de Cozinha Barris/dia (mil)":1394,
        "Produção de Derivado do Petroleo - Óleo Combustivel Barris/dia (mil)":1395,
        "Produção de Derivado do Petroleo - Óleo Diesel Barris/dia (mil)":1396,
        "Produção de Derivado do Petroleo - Outros Barris/dia (mil)":1397,
        "Produção de Derivado do Petroleo - Total Barris/dia (mil)":1398,
        "Consumo de Energia Eletrica - comercial (GWH) ":1402,
        "Consumo de Energia Eletrica - Residencial (GWH)":1403,
        "Consumo de Energia Eletrica - Industrial (GWH)":1404,
        "Consumo de Energia Eletrica - Outros (GWH)":1405,
        "Consumo de Energia Eletrica - Total (GWH)":1406, 
        "Taxa de Desemprego- Brasil ":24369,
        "Endividamentto Familiar":29037
        
    }

    opcao_serie = st.selectbox("Escolha uma série temporal:", list(series_temporais.keys()))

    codigo_serie = series_temporais[opcao_serie]

    data_inicial = st.date_input("Selecione a data inicial:")
    data_final = st.date_input("Selecione a data final:")

    if st.button("Consultar Série Temporal"):
        if data_inicial and data_final:
            df_resultado = extracao_bcb(codigo_serie, data_inicial, data_final)

            if not df_resultado.empty:
                # Layout em duas colunas
                col1, col2 = st.beta_columns(2)

                # Coluna 1: Exibindo a planilha
                with col1:
                    st.dataframe(df_resultado)

                # Coluna 2: Exibindo o gráfico
                with col2:
                    gerar_grafico(df_resultado, opcao_serie)
            else:
                st.warning("Não foram encontrados dados para a série temporal informada.")
        else:
            st.warning("Preencha todos os campos.")

if __name__ == "__main__":
    main()

