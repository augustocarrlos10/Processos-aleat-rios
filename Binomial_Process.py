import matplotlib.pyplot as plt  #Importando a biblioteca para a plotagem do gráfico
import numpy as np  #Biblioteca para as funções
r = 200 #Etapas  = n
u = 50 # Número de realizações
s = np.zeros((r, u))   #Vetor com 2 atributos, onde r número de etapas e u = 50 realizações inicializando no zero
p= 0.75  #probabilidade
n = 2
# onde sample é o número de amostras
for sample in range(u):   #u = 50 Comparando quais valores aleatórios são menores que p
    if (np.random.uniform(0, 1) < p):
        s[1, sample] = 1    #guardando os valores no vetor s
    for n in range(1, r):      # de n = até r= 200 alimentar os vetores com os processos aleatórios
	    s[n,sample]= s[n-1,sample]      #pega o vetor com o valor atual n =2 e recebe o valor anterior para a comparação
	    if (np.random.uniform(0,1) < p):  # Se o valor aleatório tiver com o parâmetro menor que a probabilidade
		    s[n,sample] = s[n-1,sample]+1   #Logo o próximo processo vai ser somado + 1 e vai contruindo o processo aleatório
# Sempre comparando o atual com o anterior e guarda o próximo, assim sucessivamente

#########################################################################################################################
#Agora para plotar outra distribuição com os mesmos parâmetros e probabilidade k = 0.4

k = 0.5
v = np.zeros((r, u))       ##Vetor com 2 atributos, onde r = 200 é o número de tentativas e u = 50 realizações inicializando no zero
for sample in range(u):    #Comparando quais valores aleatórios são menores que k
    if (np.random.uniform(0, 1) < k):
        v[1, sample] = 1    #guardando os valores no vetor v
    for n in range(1, r):      # de n = até r= 200 alimentar os vetores com os processos aleatórios
	    v[n,sample]= v[n-1,sample]      #pega o vetor com o valor atual n =2 e recebe o valor anterior para a comparação
	    if (np.random.uniform(0 ,1) < k):  # Se o valor aleatório tiver com o parâmetro menor que a probabilidade
		    v[n,sample] = v[n-1,sample]+1   #Logo o próximo processo vai ser somado + 1 e vai contruindo o processo aleatório

plt.plot(s[:, sample], 'r-', label = "prob %s" %str(p))  #Plotando a figura com o processo bonomial aleatório
plt.plot(v[:, sample], 'g-', label = "prob %s" %str(k))  #Plotando a figura com o processo bonomial aleatório
plt.legend('')
plt.title(f'Processo aleatório binomial')   #Título
plt.xlabel('N') #Eixo x
plt.ylabel('Sn')    #Eixo y
plt.legend(loc=2)   #Localização da legenda
plt.grid(True)
plt.show()