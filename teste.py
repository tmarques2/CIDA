# (1) Carregamento das bibliotecas
import numpy as np
import matplotlib.pyplot as plt

#ex1
# (2) Entrada de dados
resistencias = [348.5, 340.1, 360.8, 353.2, 357.6]

# (3) Processamento de dados
media_resistencia = np.mean(resistencias)
desvio_medio = np.mean(np.abs(np.array(resistencias) - media_resistencia))
desvio_padrao = np.std(resistencias)

# (4) Apresentação dos resultados
print("1) Tensão média do material:")
print("Média da resistência (MPa):", media_resistencia)
print("\nDesvio-médio:", desvio_medio)
print("Desvio-padrão:", desvio_padrao)

#ex2
# (2) Entrada de dados
marca_a = [153, 173, 134, 157, 149, 171, 162]
marca_b = [172, 163, 151, 146, 146]

# (3) Processamento de dados
media_a = np.mean(marca_a)
desvio_a = np.std(marca_a)

media_b = np.mean(marca_b)
desvio_b = np.std(marca_b)

# (4) a - Apresentação dos resultados
print("\n2) Comparação entre as durações das pilhas:")
print(f"Marca A - Média: {media_a:.2f} horas, Desvio-padrão: {desvio_a:.2f}")
print(f"Marca B - Média: {media_b:.2f} horas, Desvio-padrão: {desvio_b:.2f}")

# b- Consistência de uso (diretamente calculando qual marca tem o menor desvio-padrão)
consistencia = ["Marca A" if desvio_a < desvio_b else "Marca B"]

print(f"\n{consistencia[0]} tem maior consistência de uso (menor desvio-padrão).")

# c- Comparação das médias (sem if-else, apenas imprimindo diretamente)
duracao_melhor = "Ambas as marcas têm a mesma média de duração." if media_a == media_b else ("Marca A tem uma duração melhor que a Marca B." if media_a > media_b else "Marca B tem uma duração melhor que a Marca A.")
print("\n", duracao_melhor)

#ex3
# (2) Entrada de dados
dureza = [83.3, 80.7, 86.4, 88.3, 84.7, 85.2, 82.8, 87.8, 86.9, 86.2, 83.5, 84.4, 87.2, 85.5, 86.3]

# (3) Processamento de dados
media_dureza = np.mean(dureza)
mediana_dureza = np.median(dureza)
desvio_dureza = np.std(dureza)

# (4) Apresentação dos resultados
print("\n3) Dureza do aço:")
print(f"Média da dureza: {media_dureza:.2f}")
print(f"Mediana da dureza: {mediana_dureza:.2f}")
print(f"Desvio-padrão da dureza: {desvio_dureza:.2f}")

# Construção do boxplot
plt.boxplot(dureza)
plt.title("Gráfico do BoxPlot dos valores de dureza")
plt.ylabel("Dureza (unidade)")
plt.show()
