#(1)Carregamneto das bibliotecas
import numpy as np
import matplotlib.pyplot as plt

#(2)Entrada de dados
#tempo de banho dos alunos
dados = [2, 3, 4, 5, 5, 5, 5, 6, 7, 8,
        8, 8, 9, 10, 10, 12, 12, 14, 14, 14,
        16, 20, 23, 25, 25, 28, 30, 32, 35, 38]

#(3)Processamento de dados
N = len(dados)      #Identifica a qtd de amostras
k = 1 + 3.32 * np.log10(N)      #Calculo do numero de amostras
k_final = np.round(k)           #Arredonda o numero de classes

t = (max(dados) - min(dados))/k_final    #tamanho das classes

#Uso da função histogram do numpy
tabela = np.histogram(dados, int(k_final))

#Construção da freq. relativa
freq_abs = tabela[0]          #separa os dados da freq. absoluta
freq_rel = freq_abs/N * 100   #calcula a freq. relativa

#(4)Apresentação de resultados
print("Número de classes do problema:", k)
print("Quantidade final:", k_final)
print("Tamanho das classes:", t)

print(tabela)
print(freq_abs)
print(freq_rel)

figura = plt.hist(dados, int(k_final))
plt.title("Histograma dos tempos de banho")
plt.ylabel("Quantidade")
plt.xlabel("Tempo(min)")
#plt.show()