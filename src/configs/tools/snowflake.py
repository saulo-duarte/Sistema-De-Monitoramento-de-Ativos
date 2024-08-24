import os
import snowflake.connector
from sqlalchemy import create_engine

class SnowflakeManager:
    def __init__(self, user=None, password=None, 
                 account=None, warehouse=None, database=None, schema=None):
        
        # Verifica se as variáveis de ambiente estão configuradas

        env_vars_configured = self.check_environment_variables()

        if not env_vars_configured:
            raise ValueError("As variáveis de ambiente não estão configuradas corretamente.")
        
        # Inicializa as variáveis de ambiente

        self.user = user or os.getenv("SNOWFLAKE_USER")
        self.password = password or os.getenv("SNOWFLAKE_PASSWORD")
        self.account = account or os.getenv("SNOWFLAKE_ACCOUNT")
        self.warehouse = warehouse or os.getenv("SNOWFLAKE_WAREHOUSE")
        self.database = database or os.getenv("SNOWFLAKE_DATABASE")
        self.schema = schema or os.getenv("SNOWFLAKE_SCHEMA")

    def connect(self):
        try: 
            conn = snowflake.connector.connect(
                    user=self.user,
                    password=self.password,
                    account=self.account,
                    warehouse=self.warehouse,
                    database=self.database,
                    schema=self.schema
                )

            print("Conexão estabelecida com sucesso.")
            return conn
            
        except Exception as e:
            print(f"Erro ao conectar com o Snowflake: {e}")
            return None
            
    def execute_query(self, query):
        try:
            connection = self.connect()
            if connection:
                cursor = connection.cursor()
                cursor.execute(query)
                result = cursor.fetchall()
                cursor.close()
                return result
                
            else:
                print("Não foi possível executar a query.")

        except Exception as e:
            print(f"Erro ao executar a query: {e}")
            return None
            
    @staticmethod
    def check_environment_variables():
        if (
            not os.getenv("SNOWFLAKE_USER")
            or not os.getenv("SNOWFLAKE_PASSWORD")
            or not os.getenv("SNOWFLAKE_ACCOUNT")
            or not os.getenv("SNOWFLAKE_WAREHOUSE")
            or not os.getenv("SNOWFLAKE_DATABASE")
            or not os.getenv("SNOWFLAKE_SCHEMA")
            ):

            print("Variáveis de ambiente não configuradas corretamente.")
            return False
            
        else:
            print("Variáveis de ambiente configuradas corretamente.")
            return True
            
    def alchemy(self):
        self.engine = create_engine(
            f'snowflake://{self.user}:{self.password}@{self.account}/{self.database}/{self.schema}'
            )

        return self.engine
        
                