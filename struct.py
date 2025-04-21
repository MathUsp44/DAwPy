import pandas as pd
from sqlalchemy import create_engine

usuario = 'analyst_user'
senha = 'senha'
host = '192.168.1.100'
porta = '5432'
banco = 'comercial_db'

conexao_str = f'postgresql://{usuario}:{senha}@{host}:{porta}/{banco}'
engine = create_engine(conexao_str)

query = """
SELECT 
    categoria,
    produto_nome,
    quantidade,
    preco_unitario,
    quantidade * preco_unitario AS total_venda
FROM transacoes
WHERE data_compra >= '2024-10-01'
"""

df = pd.read_sql_query(query, engine)

resumo_categoria = df.groupby('categoria')['total_venda'].sum().sort_values(ascending=False)
media_por_produto = df.groupby('produto_nome')['total_venda'].mean().sort_values(ascending=False)

print("Resumo por categoria:\n", resumo_categoria)
print("\nMédia por produto:\n", media_por_produto)
