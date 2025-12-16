# Contém toda a lógica de limpeza, renomeação e cálculos

import pandas as pd

def process_filial_brick(df):
    """Trata os dados da tabela dimensão de filiais."""
    # Renomear colunas para snake_case
    df = df.rename(columns={
        'brick': 'brick',
        'Cód. Filial': 'cod_filial'
    })
    
    # Remover duplicatas completas
    df = df.drop_duplicates()
    
    # Garantir tipos
    df['brick'] = df['brick'].astype(str)
    # Remove linhas onde cód filial possa ser nulo
    df = df.dropna(subset=['cod_filial'])
    df['cod_filial'] = df['cod_filial'].astype(int)
    
    return df

def process_vendas_iqvia(df):
    """Trata os dados da tabela fato de vendas."""
    
    # 1. Renomear colunas longas (Mapeamento definitivo)
    col_map = {
        'BRICK': 'brick',
        'EAN': 'ean',
        'Cod Prod Catarinense': 'cod_prod_catarinense',
        'Tipo Informacao SI Bandeira CONCORRENTE Unidade': 'vol_concorrente_indep',
        'Tipo Informacao SO Bandeira CONCORRENTE Unidade': 'vol_concorrente_rede',
        'Tipo Informacao SO Bandeira PRECO POPULAR Unidade': 'vol_clamed_pp'
    }
    df = df.rename(columns=col_map)
    
    # 2. Tratamento de Nulos (Preencher com 0 para cálculos numéricos)
    numeric_cols = ['vol_concorrente_indep', 'vol_concorrente_rede', 'vol_clamed_pp']
    df[numeric_cols] = df[numeric_cols].fillna(0).astype(int)
    
    # 3. Converter EAN para string
    df['ean'] = df['ean'].astype(str).str.replace(r'\.0$', '', regex=True)
    
    # 4. Criar colunas calculadas
    # vol_total_mercado = soma dos concorrentes + vendas PP
    df['vol_total_mercado'] = (
        df['vol_concorrente_indep'] + 
        df['vol_concorrente_rede'] + 
        df['vol_clamed_pp']
    )
    
    # participacao_clamed = vendas PP / vol_total_mercado
    # Tratamento para evitar divisão por zero
    df['participacao_clamed'] = df.apply(
        lambda row: row['vol_clamed_pp'] / row['vol_total_mercado'] if row['vol_total_mercado'] > 0 else 0.0,
        axis=1
    )
    
    # 5. Remover duplicatas
    df = df.drop_duplicates()
    
    return df