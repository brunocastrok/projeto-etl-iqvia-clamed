-- Criação da tabela de Dimensão (Filiais e Bricks)
CREATE TABLE IF NOT EXISTS dim_filial_brick (
    brick TEXT,
    cod_filial INTEGER,
    PRIMARY KEY (brick, cod_filial)
);

-- Criação da tabela de Fatos (Vendas IQVIA)
CREATE TABLE IF NOT EXISTS fact_vendas_iqvia (
    id SERIAL PRIMARY KEY,
    brick TEXT,
    ean TEXT,
    cod_prod_catarinense TEXT,
    vol_concorrente_indep INTEGER DEFAULT 0,
    vol_concorrente_rede INTEGER DEFAULT 0,
    vol_clamed_pp INTEGER DEFAULT 0,
    vol_total_mercado INTEGER DEFAULT 0,
    participacao_clamed FLOAT DEFAULT 0.0
);

-- Criação de índices para performance em consultas futuras
CREATE INDEX idx_fact_brick ON fact_vendas_iqvia(brick);
CREATE INDEX idx_fact_ean ON fact_vendas_iqvia(ean);