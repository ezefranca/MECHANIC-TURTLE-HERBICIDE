#!/usr/bin/env python
# coding=utf8

import simplejson
import urllib

import math
import random

from turtle import *

def modTupByIndex(tup, index, ins):
    return tuple(tup[0:index]) + (ins,) + tuple(tup[index+1:])

#metodo/funcao pra segunda visualizacao tambem
def valorTotal(valores):
    total = 0
    for x in range(0, len(valores) ):
        total += valores[x]
    return total


# porcentagens dos precos de cada produto em uma data vindos do BD
def conveteEmPorcentagem(valores):
    total = valorTotal(valores)

    porcentagens = ()
    for x in range(0, len(valores) ):
        tuplaTemporaria = (valores[x]*100/total, )
        porcentagens = porcentagens + tuplaTemporaria
    return porcentagens


def converteValoresDoBancoEmPixelsPraDesenhar (valoresNumaData): #nome auto-explicativo

#    #valor total da cesta para determinar a % de cada item
#    dataTotal = valorTotal(valoresNumaData)

    # porcentagens dos precos de cada produto em uma data vindos do BD
    dataPorcentagens = conveteEmPorcentagem(valoresNumaData)


    #porcentagens aditivas dos precos em cada lugar da tupla (tipo fibonacci sqn)
    #o primeiro valor precisa ser 0%
    #exemplo: (0%, 10%, 15%, 35%, 65%, 90%, 100%)
    porcents = 0
    for x in range(0, qte):
        porcents += dataPorcentagens[x]
        dataPorcentagens = modTupByIndex(dataPorcentagens, x, porcents)

    #aki converte as %s em em valor de pixel para desenhar
    dataAlturas = (0,)
    for x in range(0, qte):
        alturaTemp = ( (alturaTabela*dataPorcentagens[x])/100.0 , )
        dataAlturas = dataAlturas+ alturaTemp

    # dataAlturas eh o que precisamos agora para desenhar com a turtle
    return dataAlturas


cor0  = (251/255.0,  16/255.0,  34/255.0)
cor1  = (253/255.0, 212/255.0,  48/255.0)
cor2  = ( 48/255.0, 190/255.0,  33/255.0)
cor3  = ( 29/255.0, 173/255.0, 250/255.0)
cor4  = (192/255.0, 113/255.0,  36/255.0)
cor5  = (108/255.0,  47/255.0,  15/255.0)
cor6  = ( 12/255.0,  91/255.0, 183/255.0)
cor7  = (237/255.0,  40/255.0, 251/255.0)
cor8  = (252/255.0,  24/255.0, 128/255.0)
cor9  = ( 30/255.0, 186/255.0, 185/255.0)
cor10 = (185/255.0, 160/255.0,  34/255.0)
cor11 = ( 14/255.0,  38/255.0, 251/255.0)
cor12 = (174/255.0, 182/255.0,  37/255.0)
cores = (cor0, cor1, cor2, cor3, cor4, cor5, cor6, cor7, cor8, cor9, cor10, cor11, cor12)


mesAno1 = ( 1900 +random.randrange(  95, 101, 1) )
mesAno2 = ( 1900 +random.randrange( 101, 108, 1) )
mesAno3 = ( 1900 +random.randrange( 108, 114, 1) )

datasPesquisa = (mesAno1, mesAno2, mesAno3)

#para datas custom
#datasPesquisa = (1994 , 2004,  2014 )


#configuragoes da tabela
alturaTabela = 700              #valor da altura em pixels               #<-valor mutavel
comprimentoTabela = 800         #valor do comprimento em pixels          #<-valor mutavel
qteColunas = len(datasPesquisa) # qte de colunas, ou datas para mostrar

divs = qteColunas - 1           # qte de "hastes" divisorias
space =  30                     # qte de pixels para transicao de nivel  #<-valor mutavel
cBase = (comprimentoTabela - (divs * space))/qteColunas  #comprimento da "base"

produtosChurrasco = ("8kg de Carne", "20 latas de Cerveja(600ml)", "8kg de Linguica", "5kg de Pao")
qte = len(produtosChurrasco)        #qte de itens na lista do churrasco


#configura e posicia a turtle original para ser copiada
screensize(1300,1000)
color('black')
pensize(1)
ht()
#showturtle()
#st()
speed(0)
tracer(1, 1)

penup()
goto(-comprimentoTabela/2, alturaTabela/2)
pendown()

# cria a copia das turtles que iram desenhar a tabela
turtles = [];

for x in range(0, qte):
    alberto = clone()
    alberto.color( "white")
    alberto.fillcolor( cores[x] )
    turtles.append( alberto )

#prepara os valores para desenhar a tabela

#------------------------ corassaum dos dados de desenho ------------------------------#
#--------------------------------------------------------------------------------------#
#coisa com o BD aki e pega os valores no banco #
datas = ()
porcentagensIndividuais = ()
for x in range(0, qteColunas):
    url = 'http://172.246.16.27/pi/churrasco.php?ano=' + str(datasPesquisa[x])

    json = simplejson.load(urllib.urlopen(url))

    carne    = json['Carne']
    cerveja  = json['Cerveja']
    linguica = json['Linguica']
    pao      = json['Pao']

    cesta_churrasco = [carne, cerveja, linguica, pao ]

    #conversao do json pra tuplas e encaixar no codigo
    dataValores = ()
    for x in range(0, qte):
        tuplaTemporaria = ( cesta_churrasco[x]['valor'], )
        dataValores = dataValores + tuplaTemporaria

    porcentagensIndividuais =  porcentagensIndividuais + (conveteEmPorcentagem(dataValores), )


    dataValores = converteValoresDoBancoEmPixelsPraDesenhar(dataValores)

    #monstrinhos pra percorrer e desenha a tabela
    datas = datas + (dataValores, )



#--------------------------------------------------------------------------------------#

#escreve encima da tabela o nome das datas dentralizado com a coluna
penup()
color("black")
alturaEscrita = alturaTabela/2 + 10
posEscrita = -comprimentoTabela/2 + cBase/2
for x in range(0, qteColunas):
    goto( posEscrita , alturaEscrita)
    texto =  str(datasPesquisa[x])
    write( texto , move=False, align="center", font=('Arial', 18, 'normal'))
    posEscrita += space + cBase

goto(0, -alturaTabela/2 - 30)
write( "Valor medio das Porcentagens de cada item do Churrasco em relação ao valor total em um certo Ano" , move=False, align="center", font=('Arial', 18, 'normal'))

#comeca a desenhar e pintar a tabela em cascata

nivel = 0
for viera in turtles:
    viera.begin_fill()

    #o primeiro valor de itens no vetor para a tabela precisa ser 0, pra fazer a borda superior bunitinho
    penup()
    viera.goto(-comprimentoTabela/2        , alturaTabela/2 -  datas[0][nivel] ) #valores 1
    pendown()
    viera.goto(-comprimentoTabela/2 + cBase, alturaTabela/2 -  datas[0][nivel] ) #valores 1
    #o espaco entre esses 2 pontos forma o retangulozinho
    
    
    distAtual = cBase
    #valorDeTeste = -10
    for coluna in range(1, qteColunas):
        distAtual += space
        viera.goto( -comprimentoTabela/2 + distAtual, alturaTabela/2 -  datas[coluna][nivel] ) #valores n
        distAtual += cBase
        viera.goto( -comprimentoTabela/2 + distAtual, alturaTabela/2 -  datas[coluna][nivel] ) #valores n


    viera.goto(  -comprimentoTabela/2 + distAtual ,  alturaTabela/2 -  datas[coluna][nivel] )#borda direita
    viera.goto(  -comprimentoTabela/2 + distAtual , -alturaTabela/2 )                        #canto inferior direito
    viera.goto( -comprimentoTabela/2 , -alturaTabela/2 )                                     #canto inferior esquerdo
    viera.goto( -comprimentoTabela/2 ,  alturaTabela/2 -  datas[0][nivel] )                  #fecha o poligono para a turtle pintar

    viera.end_fill()

    #escreve o nome do produto
    penup()
    color( cores[nivel] )
    goto(-comprimentoTabela/2 -5, alturaTabela/2 -(datas[0][nivel]+ datas[0][nivel +1])/2 -18 )
    write( produtosChurrasco[nivel], move=False, align="right", font=('Arial', 18, 'normal'))

    nivel += 1


#escreve os numeros de %s pra ficar mais legivel e bonito
#feito separado do de desenha pra nao ficar uma mistureba
nivel = 0
for viera in turtles:
    distAtual = cBase/2
    viera.penup()
    viera.color("black")
    for coluna in range(0, qteColunas):
        alturaEscrita = (datas[coluna][nivel] + datas[coluna][nivel +1])/2 + 5
        viera.goto( -comprimentoTabela/2 + distAtual, alturaTabela/2 - alturaEscrita )
        distAtual += space + cBase
        texto = str( porcentagensIndividuais[coluna][nivel] )
        viera.write( texto , move=False, align="center", font=('Arial', 10, 'normal'))

    nivel += 1


done()



