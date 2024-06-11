######################################################

# Introdução a Programação (2023/2)

######################################################


#ATENÇÃO: você não pode importar o módulo PyGame neste arquivo. 
#Consequentemente, você não pode usar o métodos do módulo.
#Você pode, se precisar, importar o módulo math e/ou random.
from BaseParaJogo import *
import random

CORFUNDOJANELA = (120, 120, 128)
LARGURAJANELA = 800
ALTURAJANELA = 672
ICONE = "Recursos/imagens/icone.png"
PARADO = 0
CIMA = 1
BAIXO = 2
ESQUERDA = 3
DIREITA = 4

MAPA = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],   
[1,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,1],
[1,2,1,2,1,2,1,1,1,2,1,1,1,1,1,2,1,1,1,2,1,2,1,2,1],
[1,2,2,2,2,2,2,2,1,2,2,2,1,2,2,2,1,2,2,2,2,2,2,2,1],
[1,1,1,2,1,1,1,2,2,2,1,2,2,2,1,2,2,2,1,1,1,2,1,1,1],
[1,2,2,2,2,2,1,2,1,1,1,1,2,1,1,1,1,2,1,2,2,2,2,2,1],
[1,2,1,1,1,2,1,2,2,2,2,2,2,2,2,2,2,2,1,2,1,1,1,2,1],
[1,2,2,2,1,2,1,1,2,1,1,1,2,1,1,1,2,1,1,2,1,2,2,2,1],
[1,2,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,1,2,1],
[1,2,1,2,1,2,1,1,1,1,1,2,1,2,1,1,1,1,1,2,1,2,1,2,1],
[1,2,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,1,2,1],
[1,2,2,2,2,2,1,1,2,1,1,1,2,1,1,1,2,1,1,2,2,2,2,2,1],
[1,2,1,2,1,2,2,2,2,2,2,2,3,2,2,2,2,2,2,2,1,2,1,2,1],
[1,2,1,2,1,2,1,1,2,1,1,1,2,1,1,1,2,1,1,2,1,2,1,2,1],
[1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,1],
[1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1,1,1,1,2,1,2,1,2,1],
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
[1,2,1,2,1,2,1,1,1,2,1,1,1,1,1,2,1,1,1,2,1,2,1,2,1],
[1,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]


def desenhaMapa(parede, fundo, pilula):
    """
    Funcao responsavel por gerar o mapa para o jgo 

    Parâmetros:
        parede  :   Variavel que está carregada a arte da parede
        fundo   :   Variavel que está carregada a arte do chão
        pilula  :   Variavel que está carregada a arte do peixe

    Retorno:
        none
    """
    for l in range(len(MAPA)):
        for c in range(len(MAPA[l])):
            if MAPA[l][c]   == 0:
                desenhaImagem(fundo, c*32, l*32)
            elif MAPA[l][c] == 1:
                desenhaImagem(fundo, c*32, l*32)
                desenhaImagem(parede, c*32, l*32)
            elif MAPA[l][c] == 2:
                desenhaImagem(fundo, c*32, l*32)
                desenhaImagem(pilula, c*32, l*32)
            elif MAPA[l][c] == 3:
                desenhaImagem(fundo, c*32, l*32)
            elif MAPA[l][c] == 4:
                desenhaImagem(fundo, c*32, l*32)


def movimentacao(xPersonagem, yPersonagem, intencao):
    """
    Verifica se a direção está indo para uma parede,
    se sim, retorna False, caso contrario True

    Parâmetros:
        xPersonagem :   Posição em relação ao eixo X do gato
        yPersonagem :   Posição em relação ao eixo Y do gato
        intencao    :   Qual tecla foi precionada/numero que foi sorteado

    Retorno:
        Valor booleano (True/False)
    """
    personagem = 32

    if intencao == CIMA:
        if MAPA[(yPersonagem - 1)//32][(xPersonagem) //32] != 1 and MAPA[(yPersonagem - 1)//32][(xPersonagem + personagem - 1)//32] != 1:
            return True
    elif intencao == BAIXO:
        if MAPA[(yPersonagem + personagem ) //32][(xPersonagem) //32] != 1 and MAPA[(yPersonagem + personagem) //32][(xPersonagem + personagem - 1) //32] != 1:
            return True
    elif intencao == ESQUERDA:
        if MAPA[(yPersonagem) //32][(xPersonagem - 1) //32] != 1 and MAPA[(yPersonagem + personagem - 1) //32][(xPersonagem - 1) //32] != 1:
            return True
    elif intencao == DIREITA:
        if MAPA[(yPersonagem) //32][(xPersonagem + personagem) //32] != 1 and MAPA[(yPersonagem + personagem - 1) //32][(xPersonagem + personagem) //32] != 1:
            return True
    return False


def sorteio_diferente(intencao):
    """
    Função responsavel por verificar qual foi a ultima intenção do sorteio 
    fantasma aleatorio, e caso o sorteio devolva uma mesma direção a função
    altera para que seja dada outra direção

    Parâmetros:
        intenção de movimentação

    Retorno:
        retorna uma intenção direfente de um novo sorteio
    """
    while True:
        sorteio = random.randint(CIMA, DIREITA)
        if sorteio == intencao:
            continue
        else:
            break
    return sorteio

def distancia(xPersonagem, yPersonagem, xFantasma, yFantasma):
    distancia_cima      = ((xFantasma - xPersonagem) ** 2 + (yFantasma - yPersonagem - 32) ** 2) ** (1/2)
    distancia_baixo     = ((xFantasma - xPersonagem) ** 2 + (yFantasma - yPersonagem + 32) ** 2) ** (1/2)
    distancia_esquerda  = ((xFantasma - xPersonagem - 32) ** 2 + (yFantasma - yPersonagem) ** 2) ** (1/2)
    distancia_direita   = ((xFantasma - xPersonagem + 32) ** 2 + (yFantasma - yPersonagem) ** 2) ** (1/2)

    direcao = [distancia_cima, distancia_baixo, distancia_esquerda, distancia_direita]

def distancia_perseguidor(xPersonagem, yPersonagem, xFantasma, yFantasma):
    """
    Verifica a distancia atual entre o gato e o cachorro perseguidor,
    e devolve a melhor jogada para menor rota entre eles  

    Parâmetros:
        xPersonagem :   Posição em relação ao eixo X do gato
        yPersonagem :   Posição em relação ao eixo Y do gato
        xFantasma   :   Posição em relação ao eixo X do cachorro
        yFantasma   :   Posição em relação ao eixo Y do cachorro

    Retorno:
        direcoes[pos][1] = melhor jogada para se ir até o gato
    """
    pos = 0

    distancia_cima      = ((xFantasma - xPersonagem) ** 2 + (yFantasma - yPersonagem - 32) ** 2) ** (1/2)
    distancia_baixo     = ((xFantasma - xPersonagem) ** 2 + (yFantasma - yPersonagem + 32) ** 2) ** (1/2)
    distancia_esquerda  = ((xFantasma - xPersonagem - 32) ** 2 + (yFantasma - yPersonagem) ** 2) ** (1/2)
    distancia_direita   = ((xFantasma - xPersonagem + 32) ** 2 + (yFantasma - yPersonagem) ** 2) ** (1/2)

    direcoes = [[distancia_cima, CIMA], 
                [distancia_baixo, BAIXO],
                [distancia_esquerda, ESQUERDA],
                [distancia_direita, DIREITA]]


    while True:
         
        minimo = direcoes[0][0]

        for l in range(len(direcoes)):
            if direcoes[l][0] < minimo:
                minimo = direcoes[l][0]
                pos = l
        
        if movimentacao(xFantasma, yFantasma, (direcoes[pos][1])):
            return direcoes[pos][1]
        else:
            del direcoes[pos]
            pos = 0
            continue


def mouseDentroRetangulo(xRetangulo, yRetangulo, larguraRetangulo, alturaRetangulo, xMouse, yMouse):
    """
    Verifica se o cursor do mouse está "dentro" do retângulo

    Parâmetros:
        xRetangulo          :   y Retangulo
        yRetangulo          :   x Retangulo
        larguraRetangulo    :   largura do retangulo
        alturaRetangulo     :   altura do retangulo
        xMouse              :   posição do mouse na tela em relação a largura
        yMouse              :   posição mouse na tela em relação a altura

    Retorno:
        none

    """
    return xRetangulo <= xMouse <= larguraRetangulo + xRetangulo and yRetangulo <= yMouse <= yRetangulo + alturaRetangulo

            
def main():
    """
    Função principal responsavel por fazer a "magica do jogo", é nela que tudo acontece!

    Retorno:
        none
    """
    criaJanela(LARGURAJANELA, ALTURAJANELA, "Pet-Man Adventure", CORFUNDOJANELA,ICONE)

    dicas = carregaImagem("Recursos/imagens/telas/dicas.png")
    tela_inicio = carregaImagem("Recursos/imagens/telas/tela_inicio.png", (800,672))
    tela_vitoria = carregaImagem("Recursos/imagens/telas/vitoriafinal.png", (800,672))
    tela_derrota = carregaImagem("Recursos/imagens/telas/gameover.png", (800,672))
    coracao = carregaImagem("Recursos/imagens/vida/coracao.png", (32, 32))  
    parede = carregaImagem("Recursos/imagens/parede/parede_teste.png", (32, 32))
    fundo  = carregaImagem("Recursos/imagens/parede/fundo_grama.png", (32,32))
    
    pilula = carregaImagem("Recursos/imagens/pilula/peixe_v01.png", (32, 32))

    # Imagens Gato
    cat_baixo = [carregaImagem("Recursos/imagens/cat/cat_baixo1.png",(32 ,32)),
                carregaImagem("Recursos/imagens/cat/cat_baixo2.png",(32,32)),
                carregaImagem("Recursos/imagens/cat/cat_baixo3.png",(32,32)),
                carregaImagem("Recursos/imagens/cat/cat_baixo4.png",(32,32))]
    
    cat_cima = [carregaImagem("Recursos/imagens/cat/cat_cima1.png",(32,32)),
                carregaImagem("Recursos/imagens/cat/cat_cima2.png",(32,32)),
                carregaImagem("Recursos/imagens/cat/cat_cima3.png",(32,32)),
                carregaImagem("Recursos/imagens/cat/cat_cima4.png",(32,32))]
     
    cat_direita = [carregaImagem("Recursos/imagens/cat/cat_direita1.png",(32,32)),
                carregaImagem("Recursos/imagens/cat/cat_direita2.png",(32,32)),
                carregaImagem("Recursos/imagens/cat/cat_direita3.png",(32,32)),
                carregaImagem("Recursos/imagens/cat/cat_direita4.png",(32,32))]
    
    cat_esquerda = [carregaImagem("Recursos/imagens/cat/cat_esquerda1.png",(32,32)),
                carregaImagem("Recursos/imagens/cat/cat_esquerda2.png",(32,32)),
                carregaImagem("Recursos/imagens/cat/cat_esquerda3.png",(32,32)),
                carregaImagem("Recursos/imagens/cat/cat_esquerda4.png",(32,32)),
                carregaImagem("Recursos/imagens/cat/cat_esquerda4.png",(32,32))]
    
    # Imagens Fantasma 1
    caramelo_baixo      = [carregaImagem("Recursos/imagens/caramelo/caramelo_baixo1.png",(32,32)),
                        carregaImagem("Recursos/imagens/caramelo/caramelo_baixo2.png",(32,32)),
                        carregaImagem("Recursos/imagens/caramelo/caramelo_baixo3.png",(32,32))]

    caramelo_cima       =  [carregaImagem("Recursos/imagens/caramelo/caramelo_cima1.png",(32,32)),
                        carregaImagem("Recursos/imagens/caramelo/caramelo_cima2.png",(32,32)),
                        carregaImagem("Recursos/imagens/caramelo/caramelo_cima3.png",(32,32))]

    caramelo_direita    = [carregaImagem("Recursos/imagens/caramelo/caramelo_direita1.png",(32,32)),
                        carregaImagem("Recursos/imagens/caramelo/caramelo_direita2.png",(32,32)),
                        carregaImagem("Recursos/imagens/caramelo/caramelo_direita3.png",(32,32))]

    caramelo_esquerda   = [carregaImagem("Recursos/imagens/caramelo/caramelo_esquerda1.png",(32,32)),
                        carregaImagem("Recursos/imagens/caramelo/caramelo_esquerda2.png",(32,32)),
                        carregaImagem("Recursos/imagens/caramelo/caramelo_esquerda3.png",(32,32))]
    
    # Imagens Fantasma 2

    husky_baixo     = [carregaImagem("Recursos/imagens/husky/husky_baixo1.png",(32,32)),
                       carregaImagem("Recursos/imagens/husky/husky_baixo2.png",(32,32)),
                       carregaImagem("Recursos/imagens/husky/husky_baixo3.png",(32,32))]

    husky_cima      = [carregaImagem("Recursos/imagens/husky/husky_cima1.png",(32,32)),
                       carregaImagem("Recursos/imagens/husky/husky_cima2.png",(32,32)),
                       carregaImagem("Recursos/imagens/husky/husky_cima3.png",(32,32))]

    husky_direita   = [carregaImagem("Recursos/imagens/husky/husky_direita1.png",(32,32)),
                       carregaImagem("Recursos/imagens/husky/husky_direita2.png",(32,32)),
                       carregaImagem("Recursos/imagens/husky/husky_direita3.png",(32,32))]

    husky_esquerda  = [carregaImagem("Recursos/imagens/husky/husky_esquerda1.png",(32,32)),
                       carregaImagem("Recursos/imagens/husky/husky_esquerda2.png",(32,32)),
                       carregaImagem("Recursos/imagens/husky/husky_esquerda3.png",(32,32))]
    
    # fantasma 3

    pastor_baixo    = [carregaImagem("Recursos/imagens/pastor/pastor_baixo1.png",(32,32)),
                       carregaImagem("Recursos/imagens/pastor/pastor_baixo2.png",(32,32)),
                       carregaImagem("Recursos/imagens/pastor/pastor_baixo3.png",(32,32))]
                                     
    pastor_cima     = [carregaImagem("Recursos/imagens/pastor/pastor_cima1.png",(32,32)),
                       carregaImagem("Recursos/imagens/pastor/pastor_cima2.png",(32,32)),
                       carregaImagem("Recursos/imagens/pastor/pastor_cima3.png",(32,32))]
                                     
    pastor_direita  = [carregaImagem("Recursos/imagens/pastor/pastor_direita1.png",(32,32)),
                       carregaImagem("Recursos/imagens/pastor/pastor_direita2.png",(32,32)),
                       carregaImagem("Recursos/imagens/pastor/pastor_direita3.png",(32,32))]

    pastor_esquerda = [carregaImagem("Recursos/imagens/pastor/pastor_esquerda1.png",(32,32)),
                       carregaImagem("Recursos/imagens/pastor/pastor_esquerda2.png",(32,32)),
                       carregaImagem("Recursos/imagens/pastor/pastor_esquerda3.png",(32,32))]
    
    # fantasma 4

    cachorro_baixo    = [carregaImagem("Recursos/imagens/cachorro4/frente1.png",(32,32)),
                       carregaImagem("Recursos/imagens/cachorro4/frente2.png",(32,32)),
                       carregaImagem("Recursos/imagens/cachorro4/frente3.png",(32,32))]
                                     
    cachorro_cima     = [carregaImagem("Recursos/imagens/cachorro4/costa1.png",(32,32)),
                       carregaImagem("Recursos/imagens/cachorro4/costa2.png",(32,32)),
                       carregaImagem("Recursos/imagens/cachorro4/costa3.png",(32,32))]
                                     
    cachorro_direita  = [carregaImagem("Recursos/imagens/cachorro4/direita1.png",(32,32)),
                       carregaImagem("Recursos/imagens/cachorro4/direita2.png",(32,32)),
                       carregaImagem("Recursos/imagens/cachorro4/direita3.png",(32,32))]

    cachorro_esquerda = [carregaImagem("Recursos/imagens/cachorro4/esquerda1.png",(32,32)),
                       carregaImagem("Recursos/imagens/cachorro4/esquerda2.png",(32,32)),
                       carregaImagem("Recursos/imagens/cachorro4/esquerda3.png",(32,32))]

    #variaveis dos sons
    som_gato_morrendo = carregaSom("Recursos/sons/gatoep.mp3")
    som_latido = carregaSom("Recursos/sons/latidoep.mp3")
    musica = carregaMusica("Recursos/sons/musicajogo.mp3")
    som_pontos = carregaSom("Recursos/sons/moedajogo.mp3")
    tocaMusica(musica)

    # Variaveis fantasma 1
    imagemFantasma1 = caramelo_baixo
    xFantasma1 = 32
    yFantasma1 = 32
    frameFantasma1 = 0
    intencao_f1 = direcao_f1 = DIREITA
    velocidadeAnimacaoFant1 = 0.1

    # Variaveis fantasma 2
    imagemFantasma2 = husky_baixo
    xFantasma2 = 736
    yFantasma2 = 576
    frameFantasma2 = 0
    direcao_f2 = intencao_f2 = CIMA
    velocidadeAnimacaoFant2 = 0.1

    # Variaveis fantasma 3 
    imagemFantasma3 = pastor_baixo
    xFantasma3 = 736
    yFantasma3 = 32
    frameFantasma3 = 0
    direcao_f3 = intencao_f3 = BAIXO
    velocidadeAnimacaoFant3 = 0.1

    # Variaveis fantasma 4 
    imagemFantasma4 = cachorro_baixo
    xFantasma4 = 32
    yFantasma4 = 576 
    frameFantasma4 = 0
    direcao_f4 = intencao_f4 = BAIXO
    velocidadeAnimacaoFant4 = 0.1

    # Variaveis Gato
    imagemJogador               = cat_baixo
    frameJogador                = 0 
    xJogador                    = 384
    yJogador                    = 384
    velocidadeAnimacaoJogador   = 0.1
    intencao                    = DIREITA
    direcao                     = DIREITA
    movimento                   = False
    pontos                      = 0
    tamanho_gato                = 32
    vitoria                     = 2670
    vida                        = 3

    # Variaveis tela abertura
    larguraRetangulo    = 100
    alturaRetangulo     = 40
    xRetangulo          = 340
    yRetangulo1         = 250
    yRetangulo2         = 380
    yRetangulo3         = 520
    larguraRetangulo4   = 200
    alturaRetangulo4    = 40
    xRetangulo4         = 290
    yRetangulo4         = 425
    opcaoEscolhida      = 0


    # if pontos < vitoria and vida > 0:
    while True:
        
        if teclaPressionada(K_ESCAPE):
            break
        
        #Limpa a janela
        limpaTela()

        desenhaImagem(tela_inicio, 0, 0)

        #Obtem as informções do clique do mouse
        xMouse, yMouse = posicaoCursorMouse() 
        opcaoEscolhida = 0

        #Define as cores dos retângulos
        corRetangulo1 = (149, 38, 9)
        if mouseDentroRetangulo(xRetangulo, yRetangulo1, larguraRetangulo, alturaRetangulo, xMouse, yMouse):
            corRetangulo1 = (255, 255, 255) 
            opcaoEscolhida = 1

        corRetangulo2 =  (149, 38, 9)
        if mouseDentroRetangulo(xRetangulo, yRetangulo2, larguraRetangulo, alturaRetangulo, xMouse, yMouse):
            corRetangulo2 = (255, 255, 255)
            opcaoEscolhida = 2

        corRetangulo3 = (149, 38, 9)
        if mouseDentroRetangulo(xRetangulo, yRetangulo3, larguraRetangulo, alturaRetangulo, xMouse, yMouse):
            corRetangulo3 = (255, 255, 255)
            opcaoEscolhida = 3

        botaoPressionado, botao, posicao = botaoMousePressionado()


        borda = 3
        desenhaRetangulo(xRetangulo-borda, yRetangulo1-borda, larguraRetangulo+2*borda, alturaRetangulo+2*borda, corRetangulo1)
        desenhaRetangulo(xRetangulo, yRetangulo1, larguraRetangulo, alturaRetangulo, (214, 147, 61))
        desenhaTexto("JOGAR", 390, 270, 40, corRetangulo1, "Recursos/fontes/PixellettersFull.ttf")

        desenhaRetangulo(xRetangulo-borda, yRetangulo2-borda, larguraRetangulo+2*borda, alturaRetangulo+2*borda, corRetangulo2)
        desenhaRetangulo(xRetangulo, yRetangulo2, larguraRetangulo, alturaRetangulo, (214, 147, 61))
        desenhaTexto("DICAS", 390, 400, 40, corRetangulo2, "Recursos/fontes/PixellettersFull.ttf")

        desenhaRetangulo(xRetangulo-borda, yRetangulo3-borda, larguraRetangulo+2*borda, alturaRetangulo+2*borda, corRetangulo3)
        desenhaRetangulo(xRetangulo, yRetangulo3, larguraRetangulo, alturaRetangulo, (214, 147, 61))
        desenhaTexto("SAIR", 390, 540, 40, corRetangulo3, "Recursos/fontes/PixellettersFull.ttf")

        #Atualiza os objetos na janela
        atualizaTelaJogo()

        if botaoPressionado and botao == 1 and opcaoEscolhida == 1:
            
            while pontos < vitoria and vida > 0:   
                
                if teclaPressionada(K_ESCAPE):
                    finalizaJogo()

                limpaTela()

                if teclaPressionada(K_UP):
                    intencao = CIMA

                elif teclaPressionada(K_DOWN):
                    intencao = BAIXO

                elif teclaPressionada(K_LEFT):
                    intencao = ESQUERDA

                elif teclaPressionada(K_RIGHT):
                    intencao = DIREITA

                
                if intencao == CIMA and movimentacao(xJogador, yJogador, intencao):
                    imagemJogador = cat_cima
                    direcao = intencao

                elif intencao == BAIXO and movimentacao(xJogador, yJogador, intencao):
                    imagemJogador = cat_baixo
                    direcao = intencao
                    
                elif intencao == ESQUERDA and movimentacao(xJogador, yJogador, intencao):
                    imagemJogador = cat_esquerda
                    direcao = intencao

                elif intencao == DIREITA and movimentacao(xJogador, yJogador, intencao):
                    imagemJogador = cat_direita
                    direcao = intencao
                    

                if direcao == CIMA and movimentacao(xJogador, yJogador, direcao):
                    yJogador -= 2
                    if MAPA[yJogador // 32][xJogador //32] == 2:
                        MAPA[yJogador // 32][xJogador //32] = 0
                        pontos += 10
                        tocaSom(som_pontos)
                
                elif direcao == BAIXO and movimentacao(xJogador, yJogador, direcao):
                    yJogador += 2
                    if MAPA[yJogador // 32][xJogador //32] == 2:
                        MAPA[yJogador // 32][xJogador //32] = 0
                        pontos += 10
                        tocaSom(som_pontos)                    

                elif direcao == ESQUERDA and movimentacao(xJogador, yJogador, direcao):
                    xJogador -= 2
                    if MAPA[yJogador // 32][xJogador //32] == 2:
                        MAPA[yJogador // 32][xJogador //32] = 0
                        pontos += 10
                        tocaSom(som_pontos)                    
                
                elif direcao == DIREITA and movimentacao(xJogador, yJogador, direcao):
                    xJogador += 2
                    if MAPA[yJogador // 32][xJogador //32] == 2:
                        MAPA[yJogador // 32][xJogador //32] = 0
                        pontos += 10
                        tocaSom(som_pontos)                    
                else:
                    direcao = PARADO
                    
                if xJogador == xFantasma1 and yJogador == yFantasma1 or xJogador == xFantasma2 and yJogador == yFantasma2 or xJogador == xFantasma3 and yJogador == yFantasma3 or xJogador == xFantasma4 and yJogador == yFantasma4:
                    vida -= 1 
                    xJogador = 384
                    yJogador = 384
                    xFantasma1 = 32
                    yFantasma1 = 32
                    xFantasma2 = 736
                    yFantasma2 = 576
                    xFantasma3 = 736
                    yFantasma3 = 32
                    xFantasma4 = 32
                    yFantasma4 = 576
                    tocaSom(som_latido)
                    tocaSom(som_gato_morrendo)


                # Fantasma aleatorio 1
                
                if intencao_f1 == CIMA and movimentacao(xFantasma1, yFantasma1, intencao_f1):
                    imagemFantasma1 = caramelo_cima
                    direcao_f1 = intencao_f1
                elif intencao_f1 == BAIXO and movimentacao(xFantasma1, yFantasma1, intencao_f1):
                    imagemFantasma1 = caramelo_baixo
                    direcao_f1 = intencao_f1
                elif intencao_f1 == ESQUERDA and movimentacao(xFantasma1, yFantasma1, intencao_f1):
                    imagemFantasma1 = caramelo_esquerda
                    direcao_f1 = intencao_f1
                elif intencao_f1 == DIREITA and movimentacao(xFantasma1, yFantasma1, intencao_f1):
                    imagemFantasma1 = caramelo_direita
                    direcao_f1 = intencao_f1

                    
                if direcao_f1 == CIMA and movimentacao(xFantasma1, yFantasma1, direcao_f1):
                    yFantasma1 -= 2
                    if xFantasma1 % 32 == 0 and yFantasma1 % 32 == 0:
                        intencao_f1 = sorteio_diferente(CIMA)
                elif direcao_f1 == BAIXO and movimentacao(xFantasma1, yFantasma1, direcao_f1):
                    yFantasma1 += 2
                    if xFantasma1 % 32 == 0 and yFantasma1 % 32 == 0:
                        intencao_f1  = sorteio_diferente(BAIXO)
                elif direcao_f1 == ESQUERDA and movimentacao(xFantasma1, yFantasma1, direcao_f1):
                    xFantasma1 -= 2
                    if xFantasma1 % 32 == 0 and yFantasma1 % 32 == 0:
                        intencao_f1 = sorteio_diferente(ESQUERDA)
                elif direcao_f1 == DIREITA and movimentacao(xFantasma1, yFantasma1, direcao_f1):
                    xFantasma1 += 2
                    if xFantasma1 % 32 == 0 and yFantasma1 % 32 == 0:
                        intencao_f1 = sorteio_diferente(DIREITA)
                else:
                    intencao_f1 = random.randint(CIMA, DIREITA)

            

                # Fantasma aleatorio 2 

                if intencao_f2 == CIMA and movimentacao(xFantasma2, yFantasma2, intencao_f2):
                    imagemFantasma2 = husky_cima
                    direcao_f2 = intencao_f2
                elif intencao_f2 == BAIXO and movimentacao(xFantasma2, yFantasma2, intencao_f2):
                    imagemFantasma2 = husky_baixo
                    direcao_f2 = intencao_f2
                elif intencao_f2 == ESQUERDA and movimentacao(xFantasma2, yFantasma2, intencao_f2):
                    imagemFantasma2 = husky_esquerda
                    direcao_f2 = intencao_f2
                elif intencao_f2 == DIREITA and movimentacao(xFantasma2, yFantasma2, intencao_f2):
                    imagemFantasma2 = husky_direita
                    direcao_f2 = intencao_f2

                if direcao_f2 == CIMA and movimentacao(xFantasma2, yFantasma2, direcao_f2):
                    yFantasma2 -= 2
                    if xFantasma2 % 32 == 0 and yFantasma2 % 32 == 0:
                        intencao_f2 = sorteio_diferente(CIMA)
                elif direcao_f2 == BAIXO and movimentacao(xFantasma2, yFantasma2, direcao_f2):
                    yFantasma2 += 2
                    if xFantasma2 % 32 == 0 and yFantasma2 % 32 == 0:
                        intencao_f2  = sorteio_diferente(BAIXO)
                elif direcao_f2 == ESQUERDA and movimentacao(xFantasma2, yFantasma2, direcao_f2):
                    xFantasma2 -= 2
                    if xFantasma2 % 32 == 0 and yFantasma2 % 32 == 0:
                        intencao_f2 = sorteio_diferente(ESQUERDA)
                elif direcao_f2 == DIREITA and movimentacao(xFantasma2, yFantasma2, direcao_f2):
                    xFantasma2 += 2
                    if xFantasma2 % 32 == 0 and yFantasma2 % 32 == 0:
                        intencao_f2 = sorteio_diferente(DIREITA)
                else:
                    intencao_f2 = random.randint(CIMA, DIREITA)

                # Fantasma 3 

                intencao_f3 = distancia_perseguidor(xJogador, yJogador, xFantasma3, yFantasma3)

                if intencao_f3 == CIMA:
                    imagemFantasma3 = pastor_cima
                    direcao_f3 = intencao_f3

                elif intencao_f3 == BAIXO:
                    imagemFantasma3 = pastor_baixo
                    direcao_f3 = intencao_f3

                elif intencao_f3 == ESQUERDA:
                    imagemFantasma3 = pastor_esquerda
                    direcao_f3 = intencao_f3

                elif intencao_f3 == DIREITA:
                    imagemFantasma3 = pastor_direita
                    direcao_f3 = intencao_f3
                
                if direcao_f3 == CIMA:
                    yFantasma3 -= 2
                    
                elif direcao_f3 == BAIXO:
                    yFantasma3 += 2
                    
                elif direcao_f3 == ESQUERDA:
                    xFantasma3 -= 2

                elif direcao_f3 == DIREITA:
                    xFantasma3 += 2

                # Fantasma 4
                    
                if distancia < 30:
                    intencao_f4 = distancia_perseguidor(xJogador, yJogador, xFantasma4, yFantasma4)


                if intencao_f4 == CIMA:
                    imagemFantasma4 = cachorro_cima
                    direcao_f4 = intencao_f4

                elif intencao_f4 == BAIXO:
                    imagemFantasma4 = cachorro_baixo
                    direcao_f4 = intencao_f4

                elif intencao_f4 == ESQUERDA:
                    imagemFantasma4 = cachorro_esquerda
                    direcao_f4 = intencao_f4

                elif intencao_f4 == DIREITA:
                    imagemFantasma4 = cachorro_direita
                    direcao_f4 = intencao_f4
                
                
                if direcao_f4 == CIMA:
                    yFantasma4 -= 2
                
                elif direcao_f4 == BAIXO:
                    yFantasma4 += 2
                
                elif direcao_f4 == ESQUERDA:
                    xFantasma4 -= 2

                elif direcao_f4 == DIREITA:
                    xFantasma4 += 2


                if xJogador == xFantasma1 and yJogador == yFantasma1 or xJogador == xFantasma2 and yJogador == yFantasma2 or xJogador == xFantasma3 and yJogador == yFantasma3 or xJogador == xFantasma4 and yJogador == yFantasma4:
                    vida -= 1 
                    xJogador = 384
                    yJogador = 384
                    xFantasma1 = 32
                    yFantasma1 = 32
                    xFantasma2 = 736
                    yFantasma2 = 576
                    xFantasma3 = 736
                    yFantasma3 = 32
                    xFantasma4 = 32
                    yFantasma4 = 576
                    tocaSom(som_latido)
                    tocaSom(som_gato_morrendo)


                #Desenha mapa
                desenhaMapa(parede,fundo,pilula)
                
                #Desenha o jogador
                if direcao != PARADO:
                    frameJogador += velocidadeAnimacaoJogador
                    if frameJogador >= 4:
                        frameJogador = 0
                    desenhaImagem(imagemJogador[int(frameJogador)], xJogador, yJogador)
                else:
                    desenhaImagem(imagemJogador[0], xJogador, yJogador)

                # Desenha o fantasma 1
                if direcao_f1 != 0:
                    frameFantasma1 += velocidadeAnimacaoFant1
                    if frameFantasma1 >= 3:
                        frameFantasma1 = 0
                    desenhaImagem(imagemFantasma1[int(frameFantasma1)], xFantasma1, yFantasma1)
                else:
                    desenhaImagem(imagemFantasma1[0], xFantasma1, yFantasma1)

                # Desenha o fantasma 2
                if direcao_f2 != 0:
                    frameFantasma2 += velocidadeAnimacaoFant2
                    if frameFantasma2 >= 3:
                        frameFantasma2 = 0
                    desenhaImagem(imagemFantasma2[int(frameFantasma2)], xFantasma2, yFantasma2)
                else:
                    desenhaImagem(imagemFantasma2[0], xFantasma2, yFantasma2)

                # Desenha fantasma 3
                if direcao_f3 != 0:
                    frameFantasma3 += velocidadeAnimacaoFant3
                    if frameFantasma3 >= 3:
                        frameFantasma3 = 0
                    desenhaImagem(imagemFantasma3[int(frameFantasma3)], xFantasma3, yFantasma3)
                else:
                    desenhaImagem(imagemFantasma3[0], xFantasma3, yFantasma3)

                # Desenha fantasma 4
                if direcao_f4 != 0:
                    frameFantasma4 += velocidadeAnimacaoFant4
                    if frameFantasma4 >= 3:
                        frameFantasma4 = 0
                    desenhaImagem(imagemFantasma4[int(frameFantasma4)], xFantasma4, yFantasma4)
                else:
                    desenhaImagem(imagemFantasma4[0], xFantasma4, yFantasma4)


                desenhaTexto(f"Pontos: {pontos}", 100, 656, 20, (255, 247, 0), "Recursos/fontes/DePixelHalbfett.ttf")


                # Painel de vida

                if vida == 3:
                    desenhaImagem(coracao, 768, 640)
                    desenhaImagem(coracao, 736, 640)
                    if intencao == PARADO:
                        desenhaImagem(coracao, 704, 640)
                elif vida == 2:
                    desenhaImagem(coracao, 768, 640)


                #Atualiza os objetos na janela
                atualizaTelaJogo()

            
            while pontos >= 2560 and vida > 0:
                
                if teclaPressionada(K_ESCAPE):
                    finalizaJogo()
                limpaTela()
                desenhaImagem(tela_vitoria, 0, 0)
                if teclaPressionada(K_SPACE):
                    finalizaJogo()
                atualizaTelaJogo()
            

            while vida == 0:
                if teclaPressionada(K_ESCAPE):
                    finalizaJogo()
                
                limpaTela()
            
                desenhaImagem(tela_derrota, 0, 0)
                if teclaPressionada(K_SPACE):
                    vida = 3
                    pontos = 0
                    xJogador = 384
                    yJogador = 384
                    intencao = direcao = DIREITA
                    intencao_f1 = direcao_f1 = DIREITA
                    direcao_f2 = intencao_f2 = CIMA
                    xFantasma1 = 32
                    yFantasma1 = 32
                    xFantasma2 = 736
                    yFantasma2 = 608
                    xFantasma3 = 736
                    yFantasma3 = 32
                    xFantasma4 = 32
                    yFantasma4 = 576
                    for l in range(len(MAPA)):
                        for c in range(len(MAPA[l])):
                            if MAPA[l][c] == 0:
                                MAPA[l][c] = 2
                    
                atualizaTelaJogo()

        if botaoPressionado and botao == 1 and opcaoEscolhida == 2:

            limpaTela()

            while True:

                if teclaPressionada(K_ESCAPE):
                    finalizaJogo()

                atualizaTelaJogo()  

                xMouse, yMouse = posicaoCursorMouse() 
                opcaoEscolhida = 0
                
                corletra = (255, 0, 0)

                desenhaImagem(dicas, 0, 0)
                corRetangulo4 = (192, 192, 192)
                if mouseDentroRetangulo(xRetangulo4, yRetangulo4, larguraRetangulo, alturaRetangulo, xMouse, yMouse):
                    corRetangulo4 = (255, 0, 0)
                    opcaoEscolhida = 4

                botaoPressionado, botao, posicao = botaoMousePressionado()

                borda = 3
                desenhaRetangulo(xRetangulo4-borda, yRetangulo4-borda, larguraRetangulo4+2*borda, alturaRetangulo4+2*borda, corRetangulo4)
                desenhaRetangulo(xRetangulo4, yRetangulo4, larguraRetangulo4, alturaRetangulo4, (192, 192, 192))
                desenhaTexto("START", 390, 445, 50, corletra, "Recursos/fontes/PixellettersFull.ttf")

                if botaoPressionado and botao == 1 and opcaoEscolhida == 4:
                    break

        if botaoPressionado and botao == 1 and opcaoEscolhida == 3:
            break

main()