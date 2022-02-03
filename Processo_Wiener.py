import numpy as np
import matplotlib.pyplot as plt
#%pylab inline
def wiener_process(T, N):   #função para o processo de Wiener
    """
    T: total time
    N: The total number of steps
    """
    W0 = [0]    #Inicial
    dt = T/float(N)
    # simula os incrementos pela variável aleatóia normal
    increments = np.random.normal(0, np.sqrt(2*dt), N)  #Nesse caso a = 2
    W = W0 + list(np.cumsum(increments))    #W recebe os incrementos e vai gerando o processo de Wiener
    return W    #retorna de w o processo de wiener

N = 1000    #Número de etapas
T = 1   #Tempo total
dt = T / float(N)   #dt
t = np.linspace(0.0, N*dt, N+1)  #conta os valores de 0 até N+1 para o gráfico
plt.figure(figsize=(15,10))
for i in range(4):      #Plota o gráfico com 4 funções de amostras ou seja 4 caminhos para processos de Wiener independentes
    W = wiener_process(T, N)    #A variável W recebe a função que calcula o processo de Wiener
    plt.plot(t, W)  #Plota o gráfico do processo de Wiener
    plt.xlabel('Tempo') #Eixo x
    plt.title(f'Processo aleatório de Wiener')  #Plota o título
    plt.ylabel('Posição')   #Eixo y
    plt.grid(True)

plt.show()

