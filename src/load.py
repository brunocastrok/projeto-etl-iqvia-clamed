# Insere os DataFrames tratados no PostgreSQL

from .db import get_db_engine

def save_to_postgres(df, table_name):
    """Salva o DataFrame no banco de dados usando SQLAlchemy."""
    engine = get_db_engine()
    
    print(f"Carregando dados na tabela '{table_name}'...")

    try:
        df.to_sql(name=table_name, con=engine, if_exists='append', index=False, chunksize=1000)
        print("Carga concluída com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")