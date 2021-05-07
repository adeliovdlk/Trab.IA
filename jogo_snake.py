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
largura=640
altura=480

tamanho=10
pos_x=randint(0,(largura-tamanho)/10)*10  #com metodo randint a cobra inicia cada vez em uma posicao diferente
pos_y=randint(0,(largura-tamanho)/10)*10

velocidade_x=0
velocidade_y=0

relogio=pygame.time.Clock() #controlar os frames por segundos


fundo=pygame.display.set_mode((largura,altura))

pygame.display.set_caption("jogo_snake")



#criar um loop infinito do jogo que da sençasao que as peças estao mudando

#variavel boleana , para fazer com que o jogo continue ou qndo o usuario quiser para o jogo

sair= True
#o retangulo deve ser desenhado dentro do loop para q sempre fique visivel
while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair=False
        if event.type==pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                velocidade_y=0                  #pos_x-=10 #porem fica estatico definindo para ir para esquerda
                velocidade_x=-tamanho
            if event.key== pygame.K_RIGHT:
                velocidade_y=0 
                velocidade_x=tamanho
            if event.key== pygame.K_UP:
                velocidade_x=0 
                velocidade_y=-tamanho
            if event.key== pygame.K_DOWN:
                velocidade_x=0 
                velocidade_y=tamanho
                
    fundo.fill(white)            #preenche a tela com uma cor escolhida   
    pygame.draw.rect(fundo,black,[pos_x,pos_y,tamanho, tamanho])
    pos_x+=velocidade_x
    pos_y+=velocidade_y
    #pos_x+=0.1 teste de movimento                
    pygame.display.update()
    relogio.tick(10)
    #para que a snake atravesse a parede saia dooutro lado
   ## if pos_x >largura:
   ##       pos_x=0
    ## if pos_x < 0:
      ##    pos_x=largura-tamanho
      ##if pos_y >altura:
        ##  pos_y=0
     ## if pos_y < 0:
       ##   pos_y=altura-tamanho
    
    #para que a snake morra quando tocar a margem
    if pos_x >largura:
        sair=False
    if pos_x < 0:
        sair=False
    if pos_y >altura:
        sair=False
    if pos_y < 0:
        sair=False

pygame.quit()
quit()
