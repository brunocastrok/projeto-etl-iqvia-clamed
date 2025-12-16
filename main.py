from src.config import FILES
from src.extract import load_excel_data
from src.transform import process_filial_brick, process_vendas_iqvia
from src.load import save_to_postgres

def main():
    print(">>> INICIANDO PROCESSO ETL CLAMED IQVIA <<<")
    
    # --- FLUXO 1: Tabela Dimensão (Filiais) ---
    print("\n[Etapa 1] Processando Dimensão Filial-Brick")
    raw_filiais = load_excel_data(FILES['filiais'])
    clean_filiais = process_filial_brick(raw_filiais)
    save_to_postgres(clean_filiais, 'dim_filial_brick')
    
    # --- FLUXO 2: Tabela Fato (Vendas) ---
    print("\n[Etapa 2] Processando Fato Vendas IQVIA")
    raw_vendas = load_excel_data(FILES['vendas'])
    clean_vendas = process_vendas_iqvia(raw_vendas)
    save_to_postgres(clean_vendas, 'fact_vendas_iqvia')
    
    print("\n>>> PROCESSO FINALIZADO <<<")

if __name__ == "__main__":
    main()