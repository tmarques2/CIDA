# (1) Carregamento das bibliotecas
import numpy as np

# (2) Entrada de dados
seguros = [33.6, 14.0, 12.9, 12.2, 5.5, 5.3, 3.1, 2.9, 1.7, 1.0, 0.9]

# (3) Processamento dos dados
media = np.mean(seguros)              #Calcula a média
variancia = np.var(seguros)           #Calcula a variância
dp = np.sqrt(variancia)               #Calcula o desvio-padrão

media = np.round(media, decimals=2)

# (4) Apresentação dos resultados
print("A média dos valores:", media)
print("A variância dos valores:", variancia)
print("O desvio-padrão dos valores:", dp)