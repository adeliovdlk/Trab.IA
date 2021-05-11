import pygame
from random import randint


white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
gren=(0,255,0)
blue=(0,0,255)

try:
#iniciando a biblioteca pygame
    pygame.init
except:
    print("O modulo do pygame nao inicializado com sucesso")
#definindo tamanho da  tela    
largura=640
altura=480
tamanho=10


relogio=pygame.time.Clock() #controlar os frames por segundos


fundo=pygame.display.set_mode((largura,altura))

pygame.display.set_caption("jogo_snake")



#criar um loop infinito do jogo que da sençasao que as peças estao mudando

#variavel boleana , para fazer com que o jogo continue ou qndo o usuario quiser para o jogo
def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(fundo,black,[XY[0],XY[1],tamanho, tamanho])
    
def maca(pos_x, pos_y):#desenha a  maca
    pygame.draw.rect(fundo,red,[pos_x,pos_y,tamanho, tamanho])
    
def jogo():
    sair= True
    #o retangulo deve ser desenhado dentro do loop para q sempre fique visivel
    pos_x=randint(0,(largura-tamanho)/10)*10  #com metodo randint a cobra inicia cada vez em uma posicao diferente
    pos_y=randint(0,(largura-tamanho)/10)*10
    maca_x=randint(0,(largura-tamanho)/10)*10  
    maca_y=randint(0,(altura-tamanho)/10)*10

    velocidade_x=0
    velocidade_y=0
    
    CobraXY=[]  #listta
    CobraComp=1

    while sair:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair=False
            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y=0                  #pos_x-=10 #porem fica estatico definindo para ir para esquerda
                    velocidade_x=-tamanho
                if event.key== pygame.K_RIGHT and velocidade_x !=-tamanho:
                    velocidade_y=0 
                    velocidade_x=tamanho  
                if event.key== pygame.K_UP and velocidade_y !=tamanho:
                    velocidade_x=0 
                    velocidade_y=-tamanho                    
                if event.key== pygame.K_DOWN and velocidade_y !=-tamanho:                    
                    velocidade_x=0 
                    velocidade_y=tamanho
                    
        fundo.fill(white)            #preenche a tela com uma cor escolhida   
        pos_x+=velocidade_x
        pos_y+=velocidade_y

       
        CobraInicio=[]
        CobraInicio.append(pos_x)
        CobraInicio.append(pos_y)
        CobraXY.append(CobraInicio)

        if len(CobraXY) >CobraComp:
            del CobraXY[0] #deletar o primeiro elemento
        
        cobra(CobraXY) #qdno a cobra come a maca
        if pos_x==maca_x and pos_y == maca_y:
            maca_x=randint(0,(largura-tamanho)/10)*10  #a maca sempre surge em outro lugar
            maca_y=randint(0,(altura-tamanho)/10)*10
            CobraComp +=1


        
        maca(maca_x, maca_y)
        #pos_x+=0.1 teste de movimento                
        pygame.display.update()
        relogio.tick(8)
        #para que a snake atravesse a parede saia dooutro lado
        if pos_x >largura:
            pos_x=0
        if pos_x < 0:
            pos_x=largura-tamanho
        if pos_y >altura:
            pos_y=0
        if pos_y < 0:
            pos_y=altura-tamanho
        
        #para que a snake morra quando tocar a margem
##        if pos_x >largura:
##            sair=False
##        if pos_x < 0:
##            sair=False
##        if pos_y >altura:
##            sair=False
##        if pos_y < 0:
##            sair=False

jogo()
pygame.quit()
quit()
