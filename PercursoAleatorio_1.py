import numpy as np  #Importa as bibliotecas
import matplotlib.pyplot as plt #Importa as bibliotecas

def random_walk(N):
    """
    Simula um percurso aleatório discreto
    :parametro int N : O número de etapas
    """
    # espaço para eventos: conjunto de incrementos possíveis
    increments = np.array([1, -1])

    # a probabilidade de gerar 1
    p= 0.5

    # Gera os incrementos aleatórios
    random_increments = np.random.choice(increments, N, p)
    # Calcula o percurso aleatório
    random_walk = np.cumsum(random_increments)

    # retornar o percurso inteiro e os incrementos
    return random_walk, random_increments

# generate a random walk
v = []  #Inicia os vetores
X = []
N = 1000  #Número de etapas
i = 0
k = np.linspace(0 , N, N)   #conta os valores de 0 até N para o gráfico
for i in range(4):  #Gera 4 testes de percurso aleatório
    #Gerando o percurso aleatório
    X, epsilon = random_walk(N)
    v.append(X)         #A variável v recebe os valores do percruso aleatório
    plt.plot(k, X)      #plota o gráfico
    plt.xlabel('Tempo') #Eixo x
    plt.title(f'Processo de Percurso Aleatório com probabilidade p = 0.5')  #Plota o título
    plt.ylabel('Posição')   #Xeixo y
    plt.grid(True)
plt.show()