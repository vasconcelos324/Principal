import yfinance as yf
import numpy as np
import pandas as pd
import streamlit as st
from dateutil.relativedelta import relativedelta

st.set_page_config(layout="wide")
@st.cache_data  
def calculate_drawdown(serie):
    retorno_acumulado = (1 + serie.pct_change()).cumprod()
    max_retorno_acumulado = retorno_acumulado.cummax()
    drawdown = (retorno_acumulado / max_retorno_acumulado) - 1
    return drawdown
def calculate_beta(df, market):
    df['Return'] = df['Adj Close'].pct_change()
    df['Market Return'] = market.pct_change()
    beta = df['Return'].cov(df['Market Return']) / df['Market Return'].var()
    return beta
st.title('Consulta de Ações, Cálculo de Beta e Drawdown')
tickers = st.text_input('Insira os tickers das ações (separados por vírgula):')
start_date = st.date_input('Data de início:')
end_date = st.date_input('Data de fim:')
diferenca = relativedelta(end_date, start_date)
anos = diferenca.years
indice = yf.download('^BVSP', start=start_date, end=end_date)['Adj Close']
if st.button('Consultar'):
    tickers = tickers.split(',')
    data = {}
    betas = {}
    drawdowns = {}
    
    for ticker in tickers:
        data[ticker] = yf.download(ticker, start=start_date, end=end_date)
        betas[ticker] = calculate_beta(data[ticker], indice)
        drawdowns[ticker] = calculate_drawdown(data[ticker]['Adj Close'])
    
    fechamento_df = pd.concat({ticker: df['Adj Close'] for ticker, df in data.items()}, axis=1)
    variação_df = pd.concat({ticker: df['Adj Close'].pct_change() for ticker, df in data.items()}, axis=1).dropna()
    beta_df = pd.DataFrame(betas.items(), columns=['Ticker', 'Beta']).round(2)
    beta_df.set_index('Ticker', inplace=True)
    drawdown_df = pd.DataFrame(drawdowns)
    
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader('Fechamento Diário')
        st.dataframe(fechamento_df)
    with col2:
        st.subheader('Variação Diária')
        st.dataframe(variação_df)
    with col3:
        st.subheader(f'Beta de {anos} Anos')
        st.dataframe(beta_df)
    
    
    st.subheader('Preço')
    st.line_chart(fechamento_df)
    st.subheader('Drawdown')
    st.line_chart(drawdown_df)
else:
    st.warning("Não foi possível coletar dados das empresas ")
