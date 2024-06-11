

def distancia(xPersonagem, yPersonagem, xFantasma, yFantasma):
    """
    
    """
    distancia_cima      = ((xFantasma - xPersonagem) ** 2 + (yFantasma - yPersonagem - 32) ** 2) ** (1/2)
    distancia_baixo     = ((xFantasma - xPersonagem) ** 2 + (yFantasma - yPersonagem + 32) ** 2) ** (1/2)
    distancia_esquerda  = ((xFantasma - xPersonagem - 32) ** 2 + (yFantasma - yPersonagem) ** 2) ** (1/2)
    distancia_direita   = ((xFantasma - xPersonagem + 32) ** 2 + (yFantasma - yPersonagem) ** 2) ** (1/2)

    distancias = [distancia_cima, distancia_baixo, distancia_esquerda, distancia_direita]
    
    return distancias

        
        
def main():

    xFantasma1 = 32
    yFantasma1 = 32

    xJogador                    = 384
    yJogador                    = 384

    verificacao = distancia(xJogador, yJogador, xFantasma1, yFantasma1)

    distancia_cima      = verificacao[0]
    distancia_baixo     = verificacao[1]
    distancia_esquerda  = verificacao[2]
    distancia_direita   = verificacao[3]

    print(distancia_cima)
    print(distancia_baixo)
    print(distancia_esquerda)
    print(distancia_direita)

main()