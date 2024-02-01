import pandas as pd
import streamlit as st

def extrair_dados(codigo, data_inicial, data_final):
    url = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados?formato=json&dataInicial={data_inicial}&dataFinal={data_final}'
    df = pd.read_json(url)
    df.set_index('data', inplace=True)
    df.index = pd.to_datetime(df.index, dayfirst=True)
    return df

def main():
    st.title("Consulta de Série Temporal do Banco Central")
    series_temporais = {
        "Índice volume de vendas no varejo - Total - Brasil         (Índice)":1455,
        "Índice de Confiança do Consumidor                          (Índice)":4393,
        "Índice de Confiança do Empresário Industrial - Geral       (Índice)":7341,
        "Índice nacional de preços ao consumidor (INPC)             (Var. % mensal)":188,
        "Índice geral de preços do mercado (IGP-M)                  (Var. % mensal)":189,
        "Índice nacional de preços ao consumidor-amplo (IPCA)       (Var. % mensal)":433,
        "Índice nacional de preços ao consumidor - amplo (IPCA) - em 12 meses (%)":13522,
        "Índice de Comodite - Brasil                                (Índice)":27574,
        "Índice de Commodities - Brasil - Agropecuária              (Índice)":27575,
        "Índice de Comodite Brasil- Metal                           (Índice)":27576,
        "Índice de Comodite Brasil- Energia                         (Índice)":27577,
        
        "PIB - Serviços - Taxa de variação real no ano              (Var. % anual)":7329,
        "Dívida Externa Bruta - Pública                             (US$ milhões)" :21523,

        "Taxa referencial - Primeiro dia do mês anual na base 252                            (% a.a.)":7812,
        "Taxa de juros - Selic anualizada base 252                                           (% a.a)":1178,
        "Taxa de desocupação - PNADC                                                         (%)":24369,
        "Taxa de inadimplência das operações de crédito do SFN - Região Norte - PF           (%)":15888,
        "Taxa de inadimplência das operações de crédito do SFN - Região Nordeste - PF        (%)":15889,
        "Taxa de inadimplência das operações de crédito do SFN - Região Centro-Oeste - PF    (%)":15890,
        "Taxa de inadimplência das operações de crédito do SFN - Região Sudeste  - PF        (%)":15891,
        "Taxa de inadimplência das operações de crédito do SFN - Região Sul - PF             (%)":15892,
        "Taxa de inadimplência das operações de crédito do SFN - Região Norte - PJ           (%)":15920,
        "Taxa de inadimplência das operações de crédito do SFN - Região Nordeste - PJ        (%)":15921,
        "Taxa de inadimplência das operações de crédito do SFN - Região Centro-Oeste - PJ    (%)":15922,
        "Taxa de inadimplência das operações de crédito do SFN - Região Sudeste  - PJ        (%)":15923,
        "Taxa de inadimplência das operações de crédito do SFN - Região Sul - PJ             (%)":15924,
        "Taxa de inadimplência das operações de crédito do SFN - Região Norte - Total        (%)":15952,
        "Taxa de inadimplência das operações de crédito do SFN - Região Nordeste - Total     (%)":15953,
        "Taxa de inadimplência das operações de crédito do SFN - Região Centro-Oeste - Total (%)":15954,
        "Taxa de inadimplência das operações de crédito do SFN - Região Sudeste  - Total     (%)":15955,
        "Taxa de inadimplência das operações de crédito do SFN - Região Sul - Total          (%)":15956,
        "Endividamento das famílias com o SFN em relação à renda acumulada dos últimos doze meses (%)":29037,

        "Vendas de motociclos (Unidades)":1381,
        "Vendas de veículos pelas concessionárias - Automóveis      (Unidades)":7384,
        "Vendas de veículos pelas concessionárias - Comerciais leves(Unidades)":7385,
        "Vendas de veículos pelas concessionárias - Caminhões       (Unidades)":7386,
        "Vendas de veículos pelas concessionárias - Ônibus          (Unidades)":7387,
        "Vendas de veículos pelas concessionárias - Total           (Unidades)":7389,

        "Produção total de autoveículos                             (Unidades)":1373,
        "Produção de automóveis e comerciais leves                  (Unidades)":1374,
        "Produção de caminhões                                      (Unidades)":1375,
        "Produção de ônibus                                         (Unidades)":1376,
        "Produção de motociclos                                     (Unidades)":1377,
        "Produção de máquinas agrícolas - total                     (Unidades)":1388,
        
        "Produção de derivados de petróleo - Óleo bruto             (Barris/dia/mil)":1389,
        "Produção de derivados de petróleo - LGN                    (Barris/dia/mil)":1390,
        "Produção de derivados de petróleo - Total                  (Barris/dia/mil)":1391,
        "Produção de derivados de petróleo - Gás Naturual           (Barris/dia/milhôes)":1392,

        "Consumo de derivados de petróleo - Gasolina                (Barris/dia/milhôes)":1393,
        "Consumo de derivados de petróleo - GLP                     (Barris/dia/milhôes)":1394,
        "Consumo de derivados de petróleo - Óleo combustível        (Barris/dia/milhôes)":1395,
        "Consumo de derivados de petróleo - Óleo diesel             (Barris/dia/milhôes)":1396,
        "Consumo de derivados de petróleo - Demais derivados        (Barris/dia/milhôes)":1397,
        "Consumo de derivados de petróleo - Total                   (Barris/dia/milhôes)":1398,

        "Consumo de energia elétrica -  Brasil - Comercial          (GWH) ":1402,
        "Consumo de energia elétrica -  Brasil - Residencial        (GWH)":1403,
        "Consumo de energia elétrica -  Brasil - Industrial         (GWH)":1404,
        "Consumo de Energia Eletrica -  Brasil - Outros             (GWH)":1405,
        "Consumo de Energia Eletrica -  Brasil -  Total             (GWH)":1406, 

        "Consumo de Energia Eletrica - Região Norte - Comercial     (GWH)":1407,
        "Consumo de Energia Eletrica - Região Norte - Residencial   (GWH)":1408,
        "Consumo de Energia Eletrica - Região Norte - Industrial    (GWH)":1409,
        "Consumo de Energia Eletrica - Região Norte - Outros        (GWH)":1410,
        "Consumo de Energia Eletrica - Região Norte - Total         (GWH)":1411,

        "Consumo de Energia Eletrica - Região Nordeste - Comercial  (GWH)":1412,
        "Consumo de Energia Eletrica - Região Nordeste - Residencial(GWH)":1413,
        "Consumo de Energia Eletrica - Região Nordeste - Industrial (GWH)":1414,
        "Consumo de Energia Eletrica - Região Nordeste - Outros     (GWH)":1415,
        "Consumo de Energia Eletrica - Região Nordeste - Total      (GWH)":1416,

        "Consumo de Energia Eletrica - Região Sul - Comercial       (GWH)":1417,
        "Consumo de Energia Eletrica - Região Sul - Residencial     (GWH)":1418,
        "Consumo de Energia Eletrica - Região Sul - Industrial      (GWH)":1419,
        "Consumo de Energia Eletrica - Região Sul - Outros          (GWH)":1420,
        "Consumo de Energia Eletrica - Região Sul - Total           (GWH)":1421,

        "Consumo de Energia Eletrica - Centro-Oeste - Comercial     (GWH)":1422,
        "Consumo de Energia Eletrica - Centro-Oeste - Residencial   (GWH)":1423,
        "Consumo de Energia Eletrica - Centro-Oeste - Industrial    (GWH)":1424,
        "Consumo de Energia Eletrica - Centro-Oeste - Outros        (GWH)":1425,
        "Consumo de Energia Eletrica - Centro-Oeste - Total         (GWH)":1426,

        "Consumo de Energia Eletrica - Região Sudeste - Comercial   (GWH)":1427,
        "Consumo de Energia Eletrica - Região Sudeste - Residencial (GWH)":1428,
        "Consumo de Energia Eletrica - Região Sudeste - Industrial  (GWH)":1429,
        "Consumo de Energia Eletrica - Região Sudeste - Outros      (GWH)":1430,
        "Consumo de Energia Eletrica - Região Sudeste - Total       (GWH)":1431}
    
    opcao_serie = st.selectbox("Escolha uma série temporal:", list(series_temporais.keys()))
    codigo_serie = series_temporais[opcao_serie]
    data_inicial = st.date_input("Digite a data inicial:")
    data_final = st.date_input("Digite a data final:")
    if st.button("Coletar Dados"):
        df_resultado = extrair_dados(codigo_serie, data_inicial.strftime('%d/%m/%Y'), data_final.strftime('%d/%m/%Y'))
        if not df_resultado.empty:
            col1, col2 = st.columns(2)
            with col1:
                st.subheader(f"{opcao_serie}")
                st.dataframe(df_resultado)
            with col2:
                st.subheader(f"{opcao_serie}")
                st.line_chart(df_resultado)
        else:
            st.warning("Não foi possível coletar dados para a série temporal escolhida.")
if __name__ == "__main__":
    main()






    

