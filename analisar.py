import pandas as pd
import matplotlib.pyplot as plt

#Dado variavel
dados = {
    "aluno": ["Ana", "Bruno", "Carlos", "Diana", "Eduardo",
              "Fernanda", "Gabriel", "Helena"],
    "nota":  [8.5, 4.2, 7.0, 9.1, 3.8, 6.5, 7.8, 5.0]
}
df = pd.DataFrame(dados)

#analise
df["situacao"] = df["nota"].apply(lambda n: "Aprovado" if n >= 6 else "Reprovado")
media = df["nota"].mean()
aprovados = (df["situacao"] == "Aprovado").sum()

# 3. Relatório no terminal
print(f"\n=== Relatório da Turma ===")
print(f"Média geral:  {media:.1f}")
print(f"Aprovados:    {aprovados} de {len(df)} alunos")
print(f"\n{df[['aluno','nota','situacao']].to_string(index=False)}")

