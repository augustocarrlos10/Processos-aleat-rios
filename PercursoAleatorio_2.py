import matplotlib.pyplot as plt #Importando a biblioteca para a plotagem do gráfico
import numpy as np  #Biblioteca para as funções
def Random_Walk(N):     #Função para o processo de percurso aleatório
    sample = 0  #inicia as variáveis
    n = 0   # variável de tempo
    ss = [] #Vetor que recebrá as amostras
    #nn = [] #vetor qye recebrá os tempos
    for i in range(1, N+1): #Contador variando de 0 até N
        num = np.random.uniform(0, 1)   #gera valores aleatórios
        if num < p: #Se o número aleatório for menor que a probabilidade
            #n = n + 1   #Tempo incrementa 1
            sample = sample + 1 #Amostra incrementa 1
        if num > p: #Se o número aleatório gerado for maior que a probabilidade
            #n = n + 1   #Tempo incrementa 1
            sample = sample - 1 #Amostra decrementa 1
        ss.append(sample)   #Vetor ss recebe os valores das amostras
        #nn.append(n)    #Vetor nn recebe os valores de tempo
    return ss   #Nesse caso retorna apenas os valores para as amostras
N = 1000    #Número total n
p = 0.75 #PRobabilidade
k = np.linspace(0, N, N)    #Contagem do tempo para a plotagem do gráfico, isso poderia ser feito retornando o tempo da função
plt.plot(k, Random_Walk(N), 'r-')  #Plotando a figura para o percurso aleatório
plt.plot(k, Random_Walk(N), 'g-')  #Plotando a figura para o percurso aleatório
plt.plot(k, Random_Walk(N), 'b-')  #Plotando a figura para o percurso aleatório
plt.plot(k, Random_Walk(N), 'y-')  #Plotando a figura para o percurso aleatório
plt.legend('')
plt.title(f'Percurso aleatório com probabilidade p = {p}')  #Plota o título
plt.xlabel('Tempo') #eixo x
plt.ylabel('Posição')   #Eixo y
plt.grid(True)
plt.show()