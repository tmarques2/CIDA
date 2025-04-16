# (1) Carregamento das bibliotecas
import numpy as np
import matplotlib.pyplot as plt

# (2) Entrada de dados
lista = [45, 56, -89, 23.4, 1.5, 2.5, 5.5, 10.0, -50.1, 1.0]

# (3) Processamento de dados
#1-adição dos dados
lista.append(0.5)
lista.append(-12.5)
lista.append(27.0)

#2-calcular limite superior e inferior de um boxplot
q1 = np.percentile(lista, 25, method='averaged_inverted_cdf')
q2 = np.percentile(lista, 50, method='averaged_inverted_cdf')
q3 = np.percentile(lista, 75, method='averaged_inverted_cdf')

DQ = q3 - q1
menor_valor = min(lista)
maior_valor = max(lista)
LI = max(menor_valor, q1 - 1.5*DQ)
LS = min(maior_valor, q3 + 1.5*DQ)

# Busca dos valores de imposto maior ou igual a 10%
tamanho = len(lista)   # Acha o tamanho dos dados
contador =  range(tamanho)      # Cria um contador de 0 a tamanho
lista_vazia = []        # Cria uma lista vazia

for indice in contador:
    valor = lista[indice]   #carrega valor atual
    if (valor >= 10.0):
        lista_vazia.append(valor)

print( "Determinação dos valores do boxplot:")
print("q1",q1)
print("q1",q2)
print("q3",q3)

print("Alguns dados do Bloxplot")
print(" DQ =",DQ)
print(" Menor Valor = ", menor_valor)
print(" Maior Valor = ", maior_valor)
print(" limite inferior = ", LI)
print(" limite superior = ", LS)

print("Lista sem outlier:",lista_vazia)