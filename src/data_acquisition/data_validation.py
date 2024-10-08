import pandas as pd
import logging
import numpy as np

class DataValidator:

    def __init__ (self, df: pd.DataFrame, logger=None):
        self.df = df
        self.logger = logger or logging.getLogger(__name__)

    def check_ticker_name(self) -> pd.DataFrame:
        invalid_tickers = self.df['Ticker'].apply(lambda ticker: not self._is_valid_ticker(ticker))
        
        if invalid_tickers.any():
            invalid_tickers_list = self.df[invalid_tickers]['Ticker'].tolist()
            self.logger.warning(f"Tickers inválidos encontrados: {invalid_tickers_list}")
            self.df = self.df[~invalid_tickers]
            self.logger.info("Tickers inválidos removidos.")
        self.logger.info("O nome dos tickers foram validados com sucesso.")
        return self.df

    def _is_valid_ticker(self, ticker) -> bool:
        if ticker.endswith(".SA"):
            base_ticker = ticker[:-3]
            if len(base_ticker) < 1 or len(base_ticker) > 5 or not base_ticker.isalnum():
                return False
        else:
            if len(ticker) < 1 or len(ticker) > 5 or not ticker.isalnum():
                return False
        
        return True

    def check_null_values(self) -> pd.DataFrame:
        if self.df.isnull().sum().sum() > 0:
            self.logger.warning("Valores nulos encontrados.")
            self.df = self.df.dropna()
            self.logger.info("Valores nulos removidos.")
        self.logger.info("Etapa de remoção de valores nulos concluída."),
        return self.df
    
    def check_duplicates(self) -> pd.DataFrame:
        if self.df.duplicated().sum() > 0:
            self.logger.warning("Duplicatas encontradas.")
            self.df = self.df.drop_duplicates(keep='first')
            self.logger.info("Duplicatas removidas.")
        self.logger.info("Etapa de remoção de duplicatas concluída.")
        return self.df
    
    def check_data_type(self, expected_types: dict) -> None:
        for column, expected_type in expected_types.items():
            if column in self.df.columns:
                if not isinstance(expected_type, type):
                    self.logger.error(f"Tipo esperado inválido para a coluna '{column}': {expected_type}")
                    continue

                if expected_type == pd.Timestamp:
                    self.df[column] = pd.to_datetime(self.df[column], errors='coerce')
                    incorrect_type_mask = self.df[column].isna()
                else:
                    incorrect_type_mask = ~self.df[column].apply(lambda x: isinstance(x, expected_type))

                if incorrect_type_mask.any():
                    self.logger.warning(f"Tipo de dado inesperado na coluna '{column}'. "
                                    f"Esperado: {expected_type}, Encontrado: {self.df[column].dtype}. "
                                    f"Excluindo os valores inconsistentes.")
                    
                    self.df = self.df[~incorrect_type_mask]
    
    
    def check_positive_values(self) -> pd.DataFrame:
        for column in self.df.select_dtypes(include=[np.number]).columns:
            if (self.df[column] <= 0).sum() > 0:
                self.logger.warning(f"Valores não positivos encontrados na coluna '{column}'.")
                self.df = self.df[self.df[column] > 0]
                self.logger.info(f"Valores não positivos removidos da coluna '{column}'.")
        self.logger.info("O nome dos tickers foram validados com sucesso."),
        return self.df


    def validate(self, expected_types: dict) -> pd.DataFrame:
        self.check_ticker_name()
        self.check_null_values()
        self.check_duplicates()
        self.check_data_type(expected_types)
        self.check_positive_values()
        self.logger.info("O bloco foi validado com sucesso.")
        return self.df