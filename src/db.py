# Gerencia a engine do SQLAlchemy

from sqlalchemy import create_engine
from urllib.parse import quote_plus
from .config import DB_CONFIG

def get_db_engine():
    """Retorna a engine de conexão do SQLAlchemy com tratamento de caracteres especiais."""
    
    user = quote_plus(DB_CONFIG['user'])
    password = quote_plus(DB_CONFIG['password'])
    host = DB_CONFIG['host']
    port = DB_CONFIG['port']
    dbname = DB_CONFIG['dbname']
    
    connection_str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}"
    
    engine = create_engine(connection_str)
    return engine