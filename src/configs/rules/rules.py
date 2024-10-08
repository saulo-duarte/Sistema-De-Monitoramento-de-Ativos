import investpy
import yfinance as yf
import pandas as pd

def get_brazil_tickers():
        
        ibov_stocks = investpy.get_stocks_list(country='brazil')        
        ticker_list = [stock + '.SA' for stock in ibov_stocks]
        return ticker_list

def get_usa_tickers():
        
        american_stocks = investpy.get_stocks_list(country='united states')        
        ticker_list = [stock for stock in american_stocks]
        return ticker_list

def get_ticker_volume(ticker):
    try:
        print(f"Obtendo dados para o ticker: {ticker}")
        stock = yf.Ticker(ticker)
        hist = stock.history(period='5d')
        if hist.empty:
            print(f"Nenhum dado encontrado para o ticker: {ticker}")
            return 0
        return hist['Volume'].mean()
    except Exception as e:
        print(f"Erro ao obter dados para o ticker {ticker}: {e}")
        return 0

def get_top_usa_tickers(total_tickers):
    usa_tickers = get_usa_tickers()
    ticker_volumes = {}
    
    for ticker in usa_tickers:
        volume = get_ticker_volume(ticker)
        if volume > 0:
            ticker_volumes[ticker] = volume
        else:
            print(f"Ticker {ticker} não foi incluído devido a volume inválido.")

    sorted_tickers = sorted(ticker_volumes.items(), key=lambda x: x[1], reverse=True)
    top_tickers = [ticker for ticker, volume in sorted_tickers[:total_tickers]]
    return top_tickers


def get_top_brazil_tickers(total_tickers):
    brazil_tickers = get_brazil_tickers()
    ticker_volumes = {}
    
    for ticker in brazil_tickers:
        volume = get_ticker_volume(ticker)
        if volume > 0:
            ticker_volumes[ticker] = volume
        else:
            print(f"Ticker {ticker} não foi incluído devido a volume inválido.")

    sorted_tickers = sorted(ticker_volumes.items(), key=lambda x: x[1], reverse=True)
    top_tickers = [ticker for ticker, volume in sorted_tickers[:total_tickers]]
    return top_tickers

expected_types_stock_dict = {
    'Date': pd.Timestamp,
    'Open': float,
    'High': float,
    'Low': float,
    'Close': float,
    'Adj Close': float,
    'Volume': int,
    'Ticker': str
}

expected_dividends_types = {
    'Date': pd.Timestamp,
    'Dividends': float,
    'Ticker': str
}

expected_splits_types = {
    'Date': pd.Timestamp,
    'Stock Splits': float,
    'Ticker': str
}     