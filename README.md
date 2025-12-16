# Projeto ETL IQVIA - CLAMED

Este projeto automatiza o processo de Extração, Transformação e Carga (ETL) de dados de vendas de mercado (IQVIA) e filiais internas. O objetivo é permitir a análise de market share (Participação Clamed) frente aos concorrentes.

## Estrutura do Projeto
- **data/**: Arquivos brutos (.xlsx).
- **src/**: Scripts Python modularizados (Extração, Transformação, Carga).
- **sql/**: Scripts para criação do banco de dados.
- **notebooks/**: Jupyter Notebook para validação e análise exploratória.

## Requisitos
- Python 3.8+
- PostgreSQL
- Bibliotecas listadas em `requirements.txt`

## Configuração e Execução

1. **Banco de Dados**:
   - Crie um banco chamado `iqvia_clamed`.
   - Execute o script `sql/init_db.sql` para criar as tabelas.

2. **Configuração**:
   - Edite `src/config.py` com suas credenciais do PostgreSQL.

3. **Instalação**:
   ```bash
   pip install -r requirements.txt