# (1) Carregamento das bibliotecas
import numpy as np
import matplotlib.pyplot as plt

# (2) Entrada de dados
lista_impostos = [36.9, 28.4, 25.7, 65.4, 46.7, 3.4, 15.8, 20.6, 14.2, 9.0,
                  15.1, 1.8, 1.9, 32.7, 17.6, 3.8, 4.5, 37.5, 14.3, 20.3,
                  7.7, 46.5, 12.1, 12.7, 4.8, 3.1, 10.1, 17.8, 28.9, 7.8,
                  18.9, 11.0, 11.1, 56.1, 27.0, 2.4, 5.2, 26.0, 8.0, 22.9,
                  30.0, 13.9, 8.0, 3.4, 13.3, 10.2, 14.2, 9.1, 4.8, 29.4]

# (3) Processamento de dados
# Adição de duas novas empresas que pagam 10% e 30% de imposto
lista_impostos.append(10.0)
lista_impostos.append(30.0)

#busca dos valores de imposto maior ou igual a 10%
tamanho = len(lista_impostos)
contador = range(tamanho)
lista_vazia = []

#laço sobre cada elemento da lista de imposto
for indice in contador:
    valor = lista_impostos[indice]   #carrega valor atual
    if (valor >= 10.0):
        lista_vazia.append(valor)

#segunda solução possivel
for valor in lista_impostos:
     if (valor >= 10.0):
         lista_vazia.append(valor)

#terceira solução possivel
lista_impostos.sort()
indice = 0
for indice in contador:
    valor = lista_impostos[indice]
    if (valor >= 10.0):
        break

# (4) Apresentação dos resultados
print("indice a partir do qual começa os 10%:", indice)