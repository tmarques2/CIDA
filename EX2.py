# (1) Carregamento das bibliotecas
import numpy as np
import matplotlib.pyplot as plt

notas = [ 7, 5, 4, 5, 6, 3, 8, 4, 5, 4, 6, 4, 5, 6, 4, 6, 6,
3, 8, 4, 5, 4, 5, 5, 6]

mediana = np.median(notas)
quartis = np.percentile(notas, [25, 50, 75])
media = np.mean(notas)

aprovados = [nota for nota in notas if nota >= 5]
reprovados = [nota for nota in notas if nota < 5]

variancia_aprovados = np.var(aprovados)
variancia_reprovados = np.var(reprovados)


print(f'Mediana: {mediana}')
print(f'Quartis (Q1, Q2, Q3): {quartis}')
print(f'Média: {media}')
print(f'Aprovados: {aprovados}')
print(f'Reprovados: {reprovados}')
print(f'Variância dos Aprovados: {variancia_aprovados}')
print(f'Variância dos Reprovados: {variancia_reprovados}')