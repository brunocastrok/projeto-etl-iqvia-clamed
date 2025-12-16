# Tratamento dos arquivos do Excel

import pandas as pd
import os

def load_excel_data(filepath):
    """Lê um arquivo Excel e retorna um DataFrame."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")
    
    print(f"Extraindo dados de: {filepath}...")
    return pd.read_excel(filepath)