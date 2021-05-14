import pygame
from random import randrange
pygame.font.init()

pygame.font.get_fonts()
['arial', 'arialblack', 'bahnschrift', 'calibri', 'cambriacambriamath', 'cambria', 'candara', 'comicsansms', 'consolas', 'constantia', 'corbel', 'couriernew', 'ebrima', 'franklingothicmedium', 'gabriola', 'gadugi', 'georgia', 'impact', 'inkfree', 'javanesetext', 'leelawadeeui', 'leelawadeeuisemilight', 'lucidaconsole', 'lucidasans', 'malgungothic', 'malgungothicsemilight', 'microsofthimalaya', 'microsoftjhengheimicrosoftjhengheiui', 'microsoftjhengheimicrosoftjhengheiuibold', 'microsoftjhengheimicrosoftjhengheiuilight', 'microsoftnewtailue', 'microsoftphagspa', 'microsoftsansserif', 'microsofttaile', 'microsoftyaheimicrosoftyaheiui', 'microsoftyaheimicrosoftyaheiuibold', 'microsoftyaheimicrosoftyaheiuilight', 'microsoftyibaiti', 'mingliuextbpmingliuextbmingliuhkscsextb', 'mongolianbaiti', 'msgothicmsuigothicmspgothic', 'mvboli', 'myanmartext', 'nirmalaui', 'nirmalauisemilight', 'palatinolinotype', 'segoemdl2assets', 'segoeprint', 'segoescript', 'segoeui', 'segoeuiblack', 'segoeuiemoji', 'segoeuihistoric', 'segoeuisemibold', 'segoeuisemilight', 'segoeuisymbol', 'simsunnsimsun', 'simsunextb', 'sitkasmallsitkatextsitkasubheadingsitkaheadingsitkadisplaysitkabanner', 'sitkasmallsitkatextboldsitkasubheadingboldsitkaheadingboldsitkadisplayboldsitkabannerbold', 'sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic', 'sitkasmallsitkatextitalicsitkasubheadingitalicsitkaheadingitalicsitkadisplayitalicsitkabanneritalic', 'sylfaen', 'symbol', 'tahoma', 'timesnewroman', 'trebuchetms', 'verdana', 'webdings', 'wingdings', 'yugothicyugothicuisemiboldyugothicuibold', 'yugothicyugothicuilight', 'yugothicmediumyugothicuiregular', 'yugothicregularyugothicuisemilight', 'dengxian', 'fangsong', 'kaiti', 'simhei', 'holomdl2assets', 'extra', 'fzshuti', 'fzyaoti', 'lisu', 'stcaiyun', 'stfangsong', 'sthupo', 'stkaiti', 'stliti', 'stsong', 'stxihei', 'stxingkai', 'stxinwei', 'stzhongsong', 'youyuan', 'haettenschweiler', 'msoutlook', 'bookantiqua', 'centurygothic', 'bookshelfsymbol7', 'msreferencesansserif', 'msreferencespecialty', 'garamond', 'monotypecorsiva', 'bookmanoldstyle', 'algerian', 'baskervilleoldface', 'bauhaus93', 'bell', 'berlinsansfb', 'berlinsansfbdemi', 'bernardcondensed', 'bodonipostercompressed', 'britannic', 'broadway', 'brushscript', 'californianfb', 'centaur', 'chiller', 'colonna', 'cooperblack', 'footlight', 'freestylescript', 'harlowsolid', 'harrington', 'hightowertext', 'jokerman', 'juiceitc', 'kristenitc', 'kunstlerscript', 'lucidabright', 'lucidacalligraphy', 'lucidafaxregular', 'lucidafax', 'lucidahandwriting', 'magneto', 'maturascriptcapitals', 'mistral', 'modernno20', 'niagaraengraved', 'niagarasolid', 'oldenglishtext', 'onyx', 'parchment', 'playbill', 'poorrichard', 'ravie', 'informalroman', 'showcardgothic', 'snapitc', 'stencil', 'tempussansitc', 'vinerhanditc', 'vivaldi', 'vladimirscript', 'widelatin', 'century', 'wingdings2', 'wingdings3', 'arialms', 'msmincho', 'acaderef', 'aigdt', 'amdtsymbols', 'geniso', 'amgdt', 'bankgothic', 'bankgothicmedium', 'cityblueprint', 'commercialpi', 'commercialscript', 'countryblueprint', 'dutch801roman', 'dutch801', 'dutch801extra', 'euroroman', 'euroromanoblique', 'monospace821', 'panroman', 'romantic', 'romans', 'sansserif', 'sansserifboldoblique', 'sansserifoblique', 'stylus', 'superfrench', 'swiss721', 'swiss721outline', 'swiss721condensed', 'swiss721condensedoutline', 'swiss721blackcondensed', 'swiss721extended', 'swiss721blackextended', 'swiss721black', 'swiss721blackoutline', 'technicbold', 'techniclite', 'technic', 'universalmath1', 'vineta', 'isocpeur', 'isocteur', 'proxy9', 'proxy8', 'proxy7', 'proxy6', 'proxy5', 'proxy4', 'proxy3', 'symusic', 'symeteo', 'symath', 'symap', 'syastro', 'romant', 'romand', 'romanc', 'italict', 'greeks', 'greekc', 'gothicg', 'gothice', 'txt', 'simplex', 'scripts', 'scriptc', 'proxy2', 'proxy1', 'monotxt', 'italicc', '', 'isoct3', 'isoct2', 'isoct', 'isocp3', 'isocp2', 'isocp', 'gothici', 'gdt', 'complex', 'thcadsymbsttf', 'thcadsymbs', 'zwadobef', 'eurosign', 'lucidabrightregular', 'lucidasansregular', 'lucidasanstypewriter', 'lucidasanstypewriterregular', 'adobeheitistdregular', 'adobemingstdlight', 'adobemyungjostdmedium', 'adobepistd', 'adobesongstdlight', 'courierstd', 'courierstdbold', 'courierstdboldoblique', 'courierstdoblique', 'kozgopr6nmedium', 'kozminpr6nregular', 'myriadcad', 'hyswlongfangsong', 'swastro', 'olfsimplesansocregular', 'swcomp', 'swgothe', 'swgothg', 'swgothi', 'swgrekc', 'swgreks', 'swisop1', 'swisop2', 'swisop3', 'swisot1', 'swisot2', 'swisot3', 'swital', 'switalc', 'switalt', 'swmap', 'swmath', 'swmeteo', 'swmono', 'swmusic', 'swromnc', 'swromnd', 'swromns', 'swromnt', 'swscrpc', 'swscrps', 'swsimp', 'swtxt', 'swgdt', 'swlink', 'dejavusansmono', 'dejavusansmonooblique', 'freesans']


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
largura=320
altura=240
tamanho=10


relogio=pygame.time.Clock() #controlar os frames por segundos


fundo=pygame.display.set_mode((largura,altura))

pygame.display.set_caption("jogo_snake")
font =  pygame.font.SysFont('constantia', 14)


def texto(msg,cor):
    texto1=font.render(msg,True,cor)
    fundo.blit(texto1,[largura/12,altura/2])


#criar um loop infinito do jogo que da sençasao que as peças estao mudando

#variavel boleana , para fazer com que o jogo continue ou qndo o usuario quiser para o jogo
def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(fundo,black,[XY[0],XY[1],tamanho, tamanho])
    
def maca(pos_x, pos_y):#desenha a  maca
    pygame.draw.rect(fundo,red,[pos_x,pos_y,tamanho, tamanho])
    
def jogo():
    sair= True
    fim_de_jogo=False
    #o retangulo deve ser desenhado dentro do loop para q sempre fique visivel
    pos_x=randrange(0,largura-tamanho,10)  #com metodo randint a cobra inicia cada vez em uma posicao diferente
    pos_y=randrange(0,largura-tamanho,10)
    maca_x=randrange(0,largura-tamanho,10) 
    maca_y=randrange(0,altura-tamanho,10)

    velocidade_x=0
    velocidade_y=0
    
    CobraXY=[]  #listta
    CobraComp=1

    while sair:
        while fim_de_jogo:
            fundo.fill(white)
            texto("Fim de jogo, para continuar tecle C ou S para sair",red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair=False
                    fim_de_jogo=False
                if event.type==pygame.KEYDOWN:
                    if event.key== pygame.K_c:
                        sair= True
                        fim_de_jogo=False
                        #o retangulo deve ser desenhado dentro do loop para q sempre fique visivel
                        pos_x=randrange(0,largura-tamanho,10)  
                        pos_y=randrange(0,largura-tamanho,10)
                        maca_x=randrange(0,largura-tamanho,10) 
                        maca_y=randrange(0,altura-tamanho,10)

                        velocidade_x=0
                        velocidade_y=0
                        
                        CobraXY=[]  #listta
                        CobraComp=1
                    if event.key== pygame.K_s:
                        sair=False
                        fim_de_jogo=False          
        
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
                if event.key==pygame.K_SPACE:
                    CobraComp +=1

        if sair:
            fundo.fill(white)            #preenche a tela com uma cor escolhida   
        pos_x+=velocidade_x
        pos_y+=velocidade_y
        
        if pos_x==maca_x and pos_y == maca_y:
            maca_x=randrange(0,largura-tamanho,10) 
            maca_y=randrange(0,altura-tamanho,10)
            CobraComp +=1

        ##        #para que a snake atravesse a parede saia dooutro lado
##        if pos_x >largura:
##            pos_x=0
##        if pos_x < 0:
##            pos_x=largura-tamanho
##        if pos_y >altura:
##            pos_y=0
##        if pos_y < 0:
##            pos_y=altura-tamanho
        
        #para que a snake morra quando tocar a margem
        if pos_x >largura:
            fim_de_jogo=True
        if pos_x < 0:
            fim_de_jogo=True
        if pos_y >altura:
            fim_de_jogo=True
        if pos_y < 0:
            fim_de_jogo=True

       
        CobraInicio=[]
        CobraInicio.append(pos_x)
        CobraInicio.append(pos_y)
        CobraXY.append(CobraInicio)

        if len(CobraXY) >CobraComp:
            del CobraXY[0] #deletar o primeiro elemento

        ##colisao sem contar a cabeça senao ja da ruim 
        if any (Bloco== CobraInicio for Bloco in CobraXY[:-1]):
            fim_de_jogo=True
        
        cobra(CobraXY) #qdno a cobra come a maca
        

        
        maca(maca_x, maca_y)
        #pos_x+=0.1 teste de movimento                
        pygame.display.update()
        relogio.tick(8)                  
        
jogo()
pygame.quit()
quit()
