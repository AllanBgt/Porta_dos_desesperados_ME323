import random
import matplotlib.pyplot as plt
import numpy as np
x = []
y = []
resposta = input("Voce deseja trocar a porta escolhida? Responda com 'sim' ou 'nao'. Resposta: ")
premios = ["ouro", "cabra", "cabra"]
ganhou = 0
tentativas = 1000
for tentativa in range(1, tentativas + 1):
    random.shuffle(premios)
    portas = {"Porta 1": premios[0], "Porta 2": premios[1], "Porta 3": premios[2]}
    porta_escolhida = random.choice(list(portas))
    for i in portas:
        if portas[i] == "cabra" and i != porta_escolhida:
            del portas[i]
            break
    if resposta == "nao":
        porta_definitiva = porta_escolhida
    if resposta == "sim":
        del portas[porta_escolhida]
        porta_definitiva = list(portas)[0]
    if portas[porta_definitiva] == "ouro":
        ganhou = ganhou + 1
    x.append(tentativa)
    y.append(ganhou/tentativa)
plt.plot(x, y, color='blue')
plt.xlabel('Tentativas')
plt.ylabel('proporção acumulada de vitórias')
plt.title('Probabilidade de vencer na Porta dos Desesperados')
plt.show()
