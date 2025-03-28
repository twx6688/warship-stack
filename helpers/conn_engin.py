# help/conn_engin.py

import configparser
from sqlalchemy import create_engine
import pandas as pd

def get_engine(config_file='.config.ini'):
    """
    Reads MySQL connection credentials from a config file and returns a SQLAlchemy engine.
    
    Args:
        config_file (str): Path to the configuration file. Default is '.config.ini'.
        
    Returns:
        engine (sqlalchemy.engine.Engine): SQLAlchemy engine for connecting to MySQL.
    """
    
    # Create a ConfigParser instance and read the configuration file.
    config = configparser.ConfigParser()
    config.read(config_file)
    
    # Get MySQL credentials from the 'ws_hub' section.
    mysql_config = config['ws_hub']
    user = mysql_config.get('user')
    password = mysql_config.get('password')
    host = mysql_config.get('host', 'localhost')
    port = mysql_config.get('port', '3307')
    database = mysql_config.get('database')
    
    # Construct the SQLAlchemy connection string.
    # This example uses pymysql as the MySQL driver.
    connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    
    # Create and return the SQLAlchemy engine.
    engine = create_engine(connection_string)
    return engine

# Example usage:
# if __name__ == "__main__":
#     # Get the SQLAlchemy engine using the credentials from .config.ini
#     engine = get_engine()
    
#     # Example: Reading data from a table using pandas
#     query = "SELECT * FROM ipg_ez LIMIT 5"
#     df = pd.read_sql(query, engine)
#     print(df)
