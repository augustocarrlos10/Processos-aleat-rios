import matplotlib.pyplot as plt #Importando a biblioteca para a plotagem
import numpy as np  #importando a biblioteca para as funções

colors = ['red','blue','green'] #Vetor para as cores
rates = [1,2, 5] #Vetor para os valores dos lambdas
tmax = 200  #T = 200  o tempo
plt.figure(figsize=(10,6))
aux = 0
for rate in rates:  #For para o vetor de lamdas
    N = []  #iniciando os vetores
    T = []  #Inicia os vetores
    ne = 0  #Inicia as variáveis
    I = 0
    te = 0
    while (te < tmax):  # enquanto t < T faça:

        te = te + (-np.log(np.random.uniform(0, 1))/rate)   #Gera uma um número aleatório U e t = t - log(U)/lambda ( distribuição exponencial)

        if(te < tmax):  # e se t < T
           ne = ne + 1  # vai somando ne

        N.append(ne)    #N recebe os valores de ne = Sn
        T.append(te)    #Recebe os valores da soma da distribuição exponencial = T os tempos
    #plt.step(T, N, color = colors[aux], label = "Lambda = %d"%rate) #plota  o gráfico com as cores selecionadas
    plt.step(T, N, color=colors[aux], label="Lambda = %d" % rate)  # plota  o gráfico com as cores selecionadas
    aux = aux + 1   #variável aux = 1 para o percorrer o vetor das cores
plt.legend()    #funções para a plotagem do gráfico
plt.xlabel(r'$T$', fontsize=20) #Eixo x
plt.ylabel(r'$Sn$', fontsize=20)    #Eixo y
plt.title(f'Processo de Poisson')   #Plota o título
plt.xlim(0) #Inicia (0,0)
plt.ylim(0)
plt.grid(True)
plt.show()