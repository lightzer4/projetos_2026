import pandas as pd
import numpy as np

def gerar_dados():
    np.random.seed(42)
    meses = ["Jan","Fev","Mar","Abr","Mai","Jun",
             "Jul","Ago","Set","Out","Nov","Dez"]
    categorias = ["Eletrônicos", "Roupas", "Alimentos", "Livros"]

    registros = []
    for mes in meses:
        for cat in categorias:
            registros.append({
                "mes": mes,
                "categoria": cat,
                "vendas": np.random.randint(5000, 50000),
                "lucro": np.random.randint(1000, 15000),
            })
    return pd.DataFrame(registros)