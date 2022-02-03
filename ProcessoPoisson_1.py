import numpy as np  #Importa as bibliotecas
import matplotlib.pyplot as plt #Importa as bibliotecas

# Prepare data
N = 200  # Tempo
lambdas = [1, 2, 5] #Vetor de Lambdas
X_T = [np.random.poisson(lam, size=N) for lam in lambdas]       #N variáveis aleatórias de Poisson com os lambdas 1, 2 e 5
Soma = [[np.sum(X[0:i]) for i in range(N)] for X in X_T]           #A variável S recebe a soma dos incremenots das variáveis de Poisson com lambda 1, 2 e 5
X = np.linspace(0, N, N)         #conta os valores de 0 até N para o gráfico

# Plotando o gráfico
graphs = [plt.step(X, Soma[i], label="Lambda = %d" % lambdas[i])[0] for i in range(len(lambdas))]  #Plota o gráfico para os processos de Poisson com lamda 1,2 e 5
#Plota a legenda
plt.legend(handles=graphs, loc=2)

#plt.title("Processo de Poisson", fontdict={'fontname': 'Times New Roman', 'fontsize': 21}, y=1.03)
plt.title("Processo de Poisson", y=1.03)    #Plotando o título
plt.xlabel(r'$t$', fontsize=20) #Eixo x
plt.ylabel(r'$N(t)$', fontsize=20)  #Eixo y
plt.ylim(0) #Inicia no ponto (0,0)
plt.xlim(0)
plt.grid(True)
plt.show()