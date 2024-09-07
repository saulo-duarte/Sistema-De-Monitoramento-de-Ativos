import yfinance as yf
import pandas as pd
import logging

class DataCollector:
    def __init__(self, ticker, start_date, end_date, logger=None):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.logger = logger or logging.getLogger(__name__)

    # Coletando dados do Yahoo Finance

    def download_data(self, ticker, start_date, end_date):
        try:
            df = yf.download(ticker, start=start_date, end=end_date)
            if df is None or df.empty:
                self.logger.warning(f"Nenhum dado foi retornado para o ticker {ticker}.")
                return None
            df.reset_index(inplace=True)
            df['Ticker'] = ticker
            return df
        except Exception as e:
            self.logger.error(f"Erro ao extrair os dados para o ticker {ticker}: {e}")
            return None

    def get_dividends(self, ticker):
        try:
            ticker_obj = yf.Ticker(ticker)
            dividends = ticker_obj.dividends
            dividends = dividends.reset_index()
            dividends['Ticker'] = ticker
            self.logger.info(f"Dividendos coletados para o ticker {ticker}.")
            return dividends
        except Exception as e:
            self.logger.error(f"Erro ao coletar dividendos para o ticker {ticker}: {e}")
            return None

    def get_splits(self, ticker):
        try:
            ticker_obj = yf.Ticker(ticker)
            splits = ticker_obj.splits
            splits = splits.reset_index()
            splits['Ticker'] = ticker
            self.logger.info(f"Splits coletados para o ticker {ticker}.")
            return splits
        except Exception as e:
            self.logger.error(f"Erro ao coletar splits para o ticker {ticker}: {e}")
            return None

    def get_info(self, ticker):
        try:
            ticker_obj = yf.Ticker(ticker)
            info = ticker_obj.info
            info_df = pd.DataFrame.from_dict(info, orient='index').T
            info_df['Ticker'] = ticker
            self.logger.info(f"Informações fundamentais coletadas para o ticker {ticker}.")
            return info_df
        except Exception as e:
            self.logger.error(f"Erro ao coletar informações fundamentais para o ticker {ticker}: {e}")
            return None
    

