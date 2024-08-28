import yfinance as yf
import pandas as pd

class DataCollector:

    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    # Coletando dados do Yahoo Finance

    def download_data(self, ticker, start_date, end_date):
        try:
            df = yf.download(ticker, start=start_date, end=end_date)
            df.reset_index(inplace=True) 
            df['Ticker'] = ticker
            return df
        except Exception as e:
            print(f"Erro ao baixar dados para o ticker {ticker}: {e}")
            return pd.DataFrame()

    def get_dividends(self, ticker):
        ticker_obj = yf.Ticker(ticker)

        dividends = ticker_obj.dividends
        dividends = dividends.reset_index()
        dividends['Ticker'] = ticker 
        return dividends

    def get_splits(self, ticker):
        ticker_obj = yf.Ticker(ticker)

        # Obter os splits
        splits = ticker_obj.splits
        splits = splits.reset_index()
        splits['Ticker'] = ticker

        return splits

    def get_info(self, ticker):

        ticker_obj = yf.Ticker(ticker)

        info = ticker_obj.info

        info_df = pd.DataFrame([info])
        info_df['Ticker'] = ticker 

        return info_df
    

