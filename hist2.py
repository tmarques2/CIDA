#(1)Carregamneto das bibliotecas
import numpy as np
import matplotlib.pyplot as plt

#(2)Entrada de dados
#tempo de banho dos alunos
dados = [1.8, 1.9, 2.4, 3.1, 3.4, 3.8, 4.5, 4.8, 4.8, 5.2,
         7.7, 7.8, 8.0, 8.9, 9.0, 9.1, 10.1, 10.2, 11.0, 11.1,
         12.1, 12.7, 13.3, 13.9, 14.2, 14.2, 14.3, 15.1, 15.8, 17.6,
         17.8, 18.9, 20.3, 20.6, 22.9, 25.7, 26.0, 27.0, 28.4, 28.9,
         29.4, 30.0, 32.7, 34.0, 36.9, 37.5, 46.5, 46.7, 56.1, 65.4]

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
plt.show()